"""Report generation, digital logbook, and feedback capture."""
import os
import json
from typing import Dict, Optional
from ..core import config, llm


def _append_jsonl(path: str, record: Dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")


def report_agent(query: str, asset_id: Optional[str], bundle: Dict, timestamp: str) -> Dict:
    """Compose a structured maintenance report from the agent bundle."""
    sys = ("You are the REPORT agent. Write a concise structured maintenance report for engineers and "
           "supervisors from the provided analysis bundle. Return JSON: {\"title\":str,\"executive_summary\":str,"
           "\"diagnosis\":str,\"root_cause\":str,\"risk_and_priority\":str,\"recommended_actions\":str,"
           "\"spares_note\":str}. Keep it factual and reference asset ids.")
    user = f"ASSET: {asset_id}\nQUERY: {query}\nANALYSIS BUNDLE:\n{json.dumps(bundle, default=str)[:6000]}"
    try:
        out = llm.chat_json([{"role": "system", "content": sys}, {"role": "user", "content": user}])
    except llm.LLMUnavailable as e:
        out = {"title": f"Maintenance Report — {asset_id}",
               "executive_summary": bundle.get("answer", "")[:1200] or str(e),
               "risk_and_priority": str(bundle.get("risk_priority", {}).get("rationale", "")),
               "_llm_error": str(e)}
    out["asset_id"] = asset_id
    out["generated_at"] = timestamp
    return out


def write_logbook(asset_id: Optional[str], summary: str, severity: str, timestamp: str,
                  actions: Optional[list] = None) -> Dict:
    """Automatic digital logbook entry."""
    entry = {
        "timestamp": timestamp,
        "asset_id": asset_id,
        "severity": severity,
        "summary": summary,
        "actions": actions or [],
        "source": "maintenance_wizard_auto",
    }
    _append_jsonl(config.LOGBOOK, entry)
    return entry


def record_feedback(query: str, asset_id: Optional[str], answer_summary: str,
                    rating: str, correction: str, timestamp: str) -> Dict:
    """Persist engineer feedback for feedback-driven improvement."""
    rec = {
        "timestamp": timestamp,
        "query": query,
        "asset_id": asset_id,
        "answer_summary": answer_summary,
        "rating": rating,            # 'helpful' | 'not_helpful'
        "correction": correction,    # engineer's correction text (optional)
    }
    _append_jsonl(config.FEEDBACK, rec)
    return rec


def load_feedback_hints(asset_id: Optional[str], limit: int = 5) -> str:
    """Retrieve recent engineer corrections to inject into future reasoning (closed loop)."""
    if not os.path.exists(config.FEEDBACK):
        return ""
    hints = []
    with open(config.FEEDBACK) as f:
        for line in f:
            try:
                r = json.loads(line)
            except Exception:
                continue
            if r.get("correction") and (asset_id is None or r.get("asset_id") == asset_id):
                hints.append(f"- ({r.get('asset_id')}) {r['correction']}")
    return "\n".join(hints[-limit:])
