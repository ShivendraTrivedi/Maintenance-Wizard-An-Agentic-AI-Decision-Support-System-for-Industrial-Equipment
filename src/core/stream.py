"""Real-time sensor stream simulator.

Turns the static historical sensor CSVs into a live, ticking data feed so the
dashboard actually *moves*. Each asset gets an in-memory ring buffer that grows
on every :func:`tick`:

* new readings continue the recent value with mean-reverting noise (realistic
  jitter around the operating point),
* the asset's *degraded* sensor (from the manifest) drifts steadily toward — and
  eventually past — its normal band, so a failure visibly emerges over time,
* a ``fault_boost`` knob lets the UI inject an escalating fault on demand for a
  live demo.

The module is pure (no Streamlit import) so it stays testable; the app owns the
buffers via ``st.session_state``.
"""
import json
import functools
from typing import Dict

import numpy as np
import pandas as pd

from . import config, predictive
from .equipment_kb import EQUIP_TYPES


def _bands(atype: str) -> Dict[str, tuple]:
    return {name: (lo, hi) for name, unit, lo, hi in EQUIP_TYPES[atype]["sensors"]}


@functools.lru_cache(maxsize=1)
def _manifest() -> Dict:
    with open(config.MANIFEST) as f:
        return json.load(f)


def _degraded_sensor(asset_id: str):
    for a in _manifest()["assets"]:
        if a["asset_id"] == asset_id:
            return a.get("sensor", {}).get("degraded_sensor")
    return None


def init_buffer(asset_id: str, history: int = 160) -> Dict:
    """Create a fresh live buffer seeded from the tail of the historical CSV."""
    atype = predictive._asset_type(asset_id)
    df = predictive.load_sensor_df(asset_id).tail(history).reset_index(drop=True)
    return {
        "asset_id": asset_id,
        "atype": atype,
        "df": df,
        "degraded": _degraded_sensor(asset_id),
        "ticks": 0,
        "fault_boost": 0.0,    # extra drift injected by the UI ("simulate fault")
        "fault_sensor": None,  # which sensor the injected fault drives
        "events": [],          # live anomaly log (timestamp, sensor, value, band)
    }


def _interval(df: pd.DataFrame):
    if len(df) >= 2:
        return df["timestamp"].iloc[-1] - df["timestamp"].iloc[-2]
    return pd.Timedelta(hours=1)


def next_reading(buf: Dict) -> Dict:
    """Generate the next synthetic reading for every sensor on the asset."""
    atype, df = buf["atype"], buf["df"]
    bands = _bands(atype)
    last = df.iloc[-1]
    ts = df["timestamp"].iloc[-1] + _interval(df)
    row = {"timestamp": ts, "asset_id": buf["asset_id"]}
    for s, (lo, hi) in bands.items():
        span = hi - lo
        center = (lo + hi) / 2.0
        val = float(last[s])
        # mean-reverting random walk keeps healthy sensors lively but in-band
        val += (center - val) * 0.03 + np.random.normal(0, span * 0.018)
        if s == buf["degraded"]:
            val += span * 0.0035  # steady baseline degradation
        if s == (buf.get("fault_sensor") or buf["degraded"]):
            val += span * buf["fault_boost"]  # UI-injected fault escalation
        row[s] = round(val, 2)
    return row


def tick(buf: Dict, maxlen: int = 360) -> Dict:
    """Append one new reading; trim to a ring buffer; record band breaches."""
    row = next_reading(buf)
    buf["df"] = pd.concat([buf["df"], pd.DataFrame([row])], ignore_index=True).tail(maxlen).reset_index(drop=True)
    buf["ticks"] += 1
    bands = _bands(buf["atype"])
    for s, (lo, hi) in bands.items():
        v = row[s]
        if v > hi or v < lo:
            buf["events"].append({
                "time": row["timestamp"].strftime("%H:%M"),
                "sensor": s, "value": v, "low": lo, "high": hi,
            })
    buf["events"] = buf["events"][-12:]
    # let an injected fault decay gradually so it escalates over many ticks
    # (crosses the band) before fading, rather than being a single transient spike
    if buf["fault_boost"] > 0:
        buf["fault_boost"] = round(buf["fault_boost"] * 0.93, 5)
    return buf


def inject_fault(buf: Dict, magnitude: float = 0.06) -> Dict:
    """UI hook: kick a sensor into an escalating fault.

    Targets the asset's natural degraded sensor when it has one; otherwise picks
    the sensor currently closest to a band edge so the injected fault is always
    visible regardless of which asset the user is watching.
    """
    target = buf["degraded"]
    if target is None:
        bands = _bands(buf["atype"])
        last = buf["df"].iloc[-1]
        # sensor whose current value sits highest within its band (nearest upper edge)
        target = max(bands, key=lambda s: (float(last[s]) - bands[s][0]) / (bands[s][1] - bands[s][0]))
    buf["fault_sensor"] = target
    buf["fault_boost"] = magnitude
    return buf
