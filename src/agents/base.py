"""Shared helpers for agents: asset resolution, spares lookup, intent detection."""
import re
import json
import functools
import pandas as pd
from typing import Optional, List, Dict
from ..core import config, llm

ASSET_RE = re.compile(r"\b([A-Z]{2,}(?:-[A-Z]+)?-\d{1,2})\b")


@functools.lru_cache(maxsize=1)
def _manifest() -> Dict:
    with open(config.MANIFEST) as f:
        return json.load(f)


@functools.lru_cache(maxsize=1)
def asset_index() -> Dict[str, Dict]:
    return {a["asset_id"]: a for a in _manifest()["assets"]}


def all_asset_ids() -> List[str]:
    return list(asset_index().keys())


def resolve_asset_id(text: str) -> Optional[str]:
    """Find a known asset id mentioned in the text (case-insensitive)."""
    idx = asset_index()
    up = text.upper()
    for m in ASSET_RE.finditer(up):
        cand = m.group(1)
        if cand in idx:
            return cand
    # loose match: id without leading zero (e.g. HSM-M-1 -> HSM-M-01)
    for aid in idx:
        if aid.replace("-0", "-") in up.replace("-0", "-"):
            return aid
    return None


@functools.lru_cache(maxsize=1)
def spares_df() -> pd.DataFrame:
    return pd.read_csv(config.SPARES)


def spares_for_type(equipment_type: str) -> List[Dict]:
    df = spares_df()
    sub = df[df["equipment_type"] == equipment_type]
    return sub.to_dict(orient="records")


@functools.lru_cache(maxsize=1)
def delays_df() -> pd.DataFrame:
    import os
    if not os.path.exists(config.DELAYS):
        return pd.DataFrame(columns=["asset_id", "delay_minutes", "date", "reason", "severity"])
    return pd.read_csv(config.DELAYS)


def delay_profile(asset_id: str) -> Dict:
    """Recent production-delay profile for an asset + a 0..1 delay-severity score.

    Severity normalises ~4 hours of cumulative recent delay to 1.0.
    """
    df = delays_df()
    sub = df[df["asset_id"] == asset_id]
    total_min = int(sub["delay_minutes"].sum()) if not sub.empty else 0
    events = int(len(sub))
    severity = min(1.0, total_min / 240.0)  # 240 min (4h) -> max
    worst = sub["severity"].tolist() if not sub.empty else []
    band = "Critical" if "Critical" in worst else "High" if "High" in worst else \
           "Medium" if "Medium" in worst else "Low" if "Low" in worst else "None"
    return {"total_delay_minutes_30d": total_min, "event_count": events,
            "delay_severity": round(severity, 3), "worst_event_severity": band,
            "events": sub.to_dict(orient="records")}


INTENTS = ["diagnose", "root_cause", "predict", "risk_priority", "recommend",
           "report", "plant_overview", "general_qa"]


def detect_intents(query: str) -> List[str]:
    """LLM-based multi-intent detection with a keyword fallback."""
    sys = ("Classify the maintenance engineer's query into one or more intents. "
           f"Valid intents: {INTENTS}. "
           "Return JSON {\"intents\": [...], \"asset_mentioned\": bool}. "
           "Use 'plant_overview' for fleet/bottleneck/priority-across-plant questions. "
           "Use 'general_qa' only if none of the specific intents apply.")
    try:
        out = llm.chat_json([{"role": "system", "content": sys},
                             {"role": "user", "content": query}])
        intents = [i for i in out.get("intents", []) if i in INTENTS]
        return intents or ["general_qa"]
    except Exception:
        q = query.lower()
        hits = []
        if any(w in q for w in ["diagnos", "what is wrong", "fault", "issue", "problem"]):
            hits.append("diagnose")
        if any(w in q for w in ["root cause", "why", "caused"]):
            hits.append("root_cause")
        if any(w in q for w in ["predict", "rul", "remaining", "fail", "life"]):
            hits.append("predict")
        if any(w in q for w in ["risk", "priorit", "urgent", "critical"]):
            hits.append("risk_priority")
        if any(w in q for w in ["recommend", "what should", "action", "fix", "repair", "plan"]):
            hits.append("recommend")
        if any(w in q for w in ["report", "summary", "logbook"]):
            hits.append("report")
        if any(w in q for w in ["plant", "fleet", "bottleneck", "across", "all equipment"]):
            hits.append("plant_overview")
        return hits or ["general_qa"]
