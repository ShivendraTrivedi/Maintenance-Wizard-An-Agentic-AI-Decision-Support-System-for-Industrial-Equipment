"""Predictive analytics engine: anomaly detection, RUL estimation, failure risk.

Reads a sensor CSV for an asset and produces structured, explainable outputs:
  - per-sensor health vs the manual's normal band
  - Isolation Forest anomaly score + flagged timestamps
  - linear-trend Remaining Useful Life (time-to-threshold)
  - an overall failure-risk probability and severity
"""
import os
import json
import numpy as np
import pandas as pd
from typing import Dict, List, Optional
from sklearn.ensemble import IsolationForest
from . import config

# normal bands come from the equipment-type KB (mirrors the manual tables)
from .equipment_kb import EQUIP_TYPES  # single source of truth


def _asset_type(asset_id: str) -> Optional[str]:
    with open(config.MANIFEST) as f:
        man = json.load(f)
    for a in man["assets"]:
        if a["asset_id"] == asset_id:
            return a["type"]
    return None


def _bands(asset_type: str) -> Dict[str, tuple]:
    return {name: (lo, hi) for name, unit, lo, hi in EQUIP_TYPES[asset_type]["sensors"]}


def load_sensor_df(asset_id: str) -> pd.DataFrame:
    path = os.path.join(config.SENSORS, f"{asset_id}.csv")
    df = pd.read_csv(path, parse_dates=["timestamp"])
    return df


def analyze(asset_id: str, df: Optional[pd.DataFrame] = None) -> Dict:
    """Analyse an asset.

    By default reads the historical CSV. Pass ``df`` to analyse a live
    streaming buffer instead (used by the Live Monitor) — the maths is
    identical, only the data source changes.
    """
    atype = _asset_type(asset_id)
    if atype is None:
        return {"error": f"Unknown asset {asset_id}"}
    if df is None:
        df = load_sensor_df(asset_id)
    bands = _bands(atype)
    sensor_cols = [c for c in df.columns if c in bands]
    X = df[sensor_cols].values
    n = len(X)

    # ---- anomaly detection ----
    # Train the detector on the BASELINE window (first 50%, assumed healthy) and
    # measure how anomalous the RECENT window (last 25%) is. This makes the
    # anomaly rate discriminate degraded assets instead of being pinned by a
    # fixed contamination fraction.
    base_end = max(20, int(n * 0.5))
    recent_start = int(n * 0.75)
    iso = IsolationForest(contamination="auto", random_state=42)
    iso.fit(X[:base_end])
    recent_pred = iso.predict(X[recent_start:])
    anom_rate = float((recent_pred == -1).mean())
    raw_recent = iso.score_samples(X[recent_start:])
    base_scores = iso.score_samples(X[:base_end])
    # severity: how far recent scores drifted below the baseline mean
    drift = (base_scores.mean() - raw_recent.mean())
    sev = float(np.clip(drift / (abs(base_scores.std()) * 3 or 1), 0, 1))

    # ---- per-sensor health + trend-based RUL ----
    per_sensor = []
    worst_rul_days = None
    sample_min = (df["timestamp"].iloc[1] - df["timestamp"].iloc[0]).total_seconds() / 60.0
    pts_per_day = (24 * 60) / sample_min
    for c in sensor_cols:
        lo, hi = bands[c]
        y = df[c].values
        x = np.arange(len(y))
        # robust recent trend (last 30%)
        tail = max(10, int(len(y) * 0.3))
        slope, intercept = np.polyfit(x[-tail:], y[-tail:], 1)
        last = float(y[-1])
        recent_breaches = int(((y[-tail:] < lo) | (y[-tail:] > hi)).sum())
        status = "normal"
        if last > hi or last < lo:
            status = "out_of_band"
        elif (last > lo + 0.85 * (hi - lo)) or (last < lo + 0.15 * (hi - lo)):
            status = "warning"

        # RUL: project current trend to the nearest band edge
        rul_days = None
        if slope > 1e-9 and last < hi:
            steps = (hi - last) / slope
            rul_days = max(0.0, steps / pts_per_day)
        elif slope < -1e-9 and last > lo:
            steps = (lo - last) / slope
            rul_days = max(0.0, steps / pts_per_day)
        if rul_days is not None:
            if worst_rul_days is None or rul_days < worst_rul_days:
                worst_rul_days = rul_days

        per_sensor.append({
            "sensor": c, "unit": next(u for n, u, l, h in EQUIP_TYPES[atype]["sensors"] if n == c),
            "normal_low": lo, "normal_high": hi,
            "current": round(last, 2), "trend_per_day": round(slope * pts_per_day, 4),
            "status": status, "recent_breaches": recent_breaches,
            "rul_days": None if rul_days is None else round(rul_days, 1),
        })

    # ---- overall failure risk ----
    breach_factor = min(1.0, sum(s["recent_breaches"] for s in per_sensor) / (len(sensor_cols) * 20))
    rul_factor = 0.0
    if worst_rul_days is not None:
        rul_factor = float(np.clip(1 - (worst_rul_days / 30.0), 0, 1))  # <30d ramps risk
    oob = any(s["status"] == "out_of_band" for s in per_sensor)
    risk_prob = float(np.clip(
        0.35 * min(1.0, anom_rate)          # recent-window anomaly fraction
        + 0.25 * breach_factor              # how often sensors left their band
        + 0.20 * rul_factor                 # short remaining-useful-life ramps risk
        + 0.20 * (1.0 if oob else 0.0),     # currently out of band
        0, 1))
    if risk_prob >= 0.75:
        severity = "Critical"
    elif risk_prob >= 0.5:
        severity = "High"
    elif risk_prob >= 0.25:
        severity = "Medium"
    else:
        severity = "Low"

    full_pred = iso.predict(X)
    flagged_idx = np.where(full_pred == -1)[0]
    flagged = df.iloc[flagged_idx[-5:]]["timestamp"].dt.strftime("%Y-%m-%d %H:%M").tolist() if len(flagged_idx) else []

    return {
        "asset_id": asset_id,
        "asset_type": atype,
        "criticality": EQUIP_TYPES[atype]["criticality"],
        "window": {"from": df["timestamp"].iloc[0].strftime("%Y-%m-%d %H:%M"),
                   "to": df["timestamp"].iloc[-1].strftime("%Y-%m-%d %H:%M"),
                   "samples": len(df)},
        "anomaly": {"rate": round(anom_rate, 4), "severity_score": round(sev, 3),
                    "recent_flagged_timestamps": flagged},
        "per_sensor": per_sensor,
        "rul_days_estimate": None if worst_rul_days is None else round(worst_rul_days, 1),
        "failure_risk": {"probability": round(risk_prob, 3), "severity": severity},
    }


def list_assets() -> List[str]:
    with open(config.MANIFEST) as f:
        man = json.load(f)
    return [a["asset_id"] for a in man["assets"]]


def fleet_scan() -> List[Dict]:
    """Run analysis across all assets for the plant-level bottleneck/priority view."""
    out = []
    for aid in list_assets():
        try:
            r = analyze(aid)
            out.append({
                "asset_id": aid, "type": r["asset_type"], "criticality": r["criticality"],
                "risk": r["failure_risk"]["probability"], "severity": r["failure_risk"]["severity"],
                "rul_days": r["rul_days_estimate"], "anomaly_rate": r["anomaly"]["rate"],
            })
        except Exception as e:
            out.append({"asset_id": aid, "error": str(e)})
    out.sort(key=lambda x: x.get("risk", 0), reverse=True)
    return out


if __name__ == "__main__":
    import sys
    aid = sys.argv[1] if len(sys.argv) > 1 else "HSM-M-01"
    print(json.dumps(analyze(aid), indent=2))
