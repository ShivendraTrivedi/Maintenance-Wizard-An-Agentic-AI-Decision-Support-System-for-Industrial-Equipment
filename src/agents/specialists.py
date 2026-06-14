"""Specialist agents. Each returns a structured, explainable dict.

All grounding (manuals/SOPs/history) flows through RAG so outputs carry
citations; sensor reasoning flows through the predictive engine.
"""
from typing import Dict, List, Optional
from ..core import rag, predictive, llm
from ..core.llm import LLMUnavailable
from . import base


def _cites(results: List[Dict]) -> List[Dict]:
    return [{"n": r["rank"], "source": r["metadata"]["source"],
             "doc_type": r["metadata"]["doc_type"], "asset_id": r["metadata"]["asset_id"]}
            for r in results]


# ---------------------------------------------------------------- Diagnostic
def diagnostic_agent(query: str, asset_id: Optional[str], sensor_summary: str = "") -> Dict:
    results = rag.retrieve(query, k=6, asset_id=asset_id,
                           doc_types=["manual", "failure_report"])
    context = rag.format_context(results)
    sys = ("You are the DIAGNOSTIC agent for steel-plant equipment. From the context (manuals + past "
           "failure reports) and any sensor summary, identify the most probable fault(s). "
           "Return JSON: {\"probable_faults\":[{\"fault\":str,\"confidence\":\"low|medium|high\","
           "\"evidence\":str,\"citations\":[int]}],\"summary\":str}. Cite context bracket numbers.")
    user = f"CONTEXT:\n{context}\n\nSENSOR SUMMARY:\n{sensor_summary or 'n/a'}\n\nQUERY: {query}"
    out = llm.chat_json([{"role": "system", "content": sys}, {"role": "user", "content": user}])
    out["_citations"] = _cites(results)
    return out


# --------------------------------------------------------------- Root cause
def root_cause_agent(query: str, asset_id: Optional[str], faults_text: str = "") -> Dict:
    results = rag.retrieve(query + " root cause", k=6, asset_id=asset_id,
                           doc_types=["failure_report", "manual", "maintenance_log"])
    context = rag.format_context(results)
    sys = ("You are the ROOT-CAUSE agent. Using past failure reports, manuals and logs, determine the most "
           "likely underlying root cause(s) (not just symptoms). Return JSON: "
           "{\"root_causes\":[{\"cause\":str,\"mechanism\":str,\"likelihood\":\"low|medium|high\","
           "\"citations\":[int]}],\"reasoning\":str}. Cite bracket numbers.")
    user = f"CONTEXT:\n{context}\n\nIDENTIFIED FAULTS:\n{faults_text or 'n/a'}\n\nQUERY: {query}"
    out = llm.chat_json([{"role": "system", "content": sys}, {"role": "user", "content": user}])
    out["_citations"] = _cites(results)
    return out


# --------------------------------------------------------------- Prediction
def prediction_agent(asset_id: str) -> Dict:
    """Wrap the predictive engine and add a plain-language LLM explanation."""
    analysis = predictive.analyze(asset_id)
    if "error" in analysis:
        return analysis
    sys = ("You are the PREDICTION agent. Given quantitative sensor analysis (anomaly rate, per-sensor "
           "trends/status, RUL, failure-risk), explain the equipment health in 3-4 sentences for an engineer. "
           "Be specific about which sensor is driving risk and the early-warning. Return JSON: "
           "{\"health_summary\":str,\"early_warning\":str|null,\"key_driver_sensor\":str}.")
    try:
        out = llm.chat_json([{"role": "system", "content": sys},
                             {"role": "user", "content": str(analysis)}])
    except LLMUnavailable as e:
        # keep the deterministic analysis; skip only the prose explanation
        worst = max(analysis["per_sensor"], key=lambda s: s["recent_breaches"], default=None)
        return {"analysis": analysis, "_llm_error": str(e),
                "health_summary": (f"{asset_id}: failure risk {analysis['failure_risk']['severity']} "
                                   f"({int(analysis['failure_risk']['probability']*100)}%), "
                                   f"anomaly rate {int(analysis['anomaly']['rate']*100)}%, "
                                   f"RUL {analysis['rul_days_estimate']} d."),
                "early_warning": None,
                "key_driver_sensor": worst["sensor"] if worst else None}
    return {"analysis": analysis, **out}


def sensor_summary_text(asset_id: str) -> str:
    """Compact sensor summary string for feeding into other agents."""
    a = predictive.analyze(asset_id)
    if "error" in a:
        return "no sensor data"
    parts = [f"risk={a['failure_risk']['severity']}({a['failure_risk']['probability']}), "
             f"anomaly_rate={a['anomaly']['rate']}, RUL_days={a['rul_days_estimate']}"]
    for s in a["per_sensor"]:
        if s["status"] != "normal":
            parts.append(f"{s['sensor']}={s['current']}{s['unit']} [{s['status']}, band {s['normal_low']}-{s['normal_high']}]")
    return "; ".join(parts)


# ------------------------------------------------------------- Risk & priority
def risk_priority_agent(asset_id: str) -> Dict:
    """Combine process criticality, failure risk, spares stock & lead time into a priority score."""
    a = predictive.analyze(asset_id)
    if "error" in a:
        return a
    atype = a["asset_type"]
    spares = base.spares_for_type(atype)
    min_stock = min((s["stock_qty"] for s in spares), default=99)
    max_lead = max((s["procurement_lead_time_days"] for s in spares), default=0)
    crit_w = {"Critical": 1.0, "High": 0.75, "Medium": 0.5, "Low": 0.25}.get(a["criticality"], 0.5)
    delay = base.delay_profile(asset_id)

    risk = a["failure_risk"]["probability"]
    spares_factor = 1.0 if min_stock == 0 else (0.5 if min_stock <= 1 else 0.1)
    lead_factor = min(1.0, max_lead / 45.0)
    delay_factor = delay["delay_severity"]
    # weighted priority 0..100 — covers the four spec factors (criticality, delay
    # severity, spares availability, procurement lead time) plus failure risk.
    priority = 100 * (0.30 * risk + 0.20 * crit_w + 0.20 * delay_factor
                      + 0.15 * spares_factor + 0.15 * lead_factor)

    if priority >= 70:
        band, urgency = "P1", "Immediate"
    elif priority >= 50:
        band, urgency = "P2", "Within 24h"
    elif priority >= 30:
        band, urgency = "P3", "This week"
    else:
        band, urgency = "P4", "Scheduled"

    return {
        "asset_id": asset_id, "asset_type": atype, "process_criticality": a["criticality"],
        "failure_risk": a["failure_risk"], "rul_days": a["rul_days_estimate"],
        "delay": {"total_minutes_30d": delay["total_delay_minutes_30d"],
                  "events": delay["event_count"], "severity_score": delay["delay_severity"],
                  "worst_event": delay["worst_event_severity"]},
        "spares": {"min_stock": min_stock, "max_lead_time_days": max_lead, "items": spares},
        "priority_score": round(priority, 1), "priority_band": band, "urgency": urgency,
        "rationale": (f"risk={risk}, criticality={a['criticality']}, "
                      f"delay={delay['total_delay_minutes_30d']}min/{delay['event_count']}evt, "
                      f"min_spare_stock={min_stock}, max_lead={max_lead}d"),
    }


# ------------------------------------------------------------- Recommendation
def recommendation_agent(query: str, asset_id: Optional[str], context_blob: str) -> Dict:
    results = rag.retrieve((query or "maintenance procedure repair steps"), k=6, asset_id=asset_id,
                           doc_types=["sop", "manual", "failure_report"])
    context = rag.format_context(results)
    sys = ("You are the RECOMMENDATION agent. Produce actionable maintenance guidance grounded in the SOPs/"
           "manuals provided and the diagnostic/risk context. Always reference LOTO safety where physical work "
           "is involved. Return JSON: {\"immediate_actions\":[str],\"step_by_step\":[str],"
           "\"long_term_monitoring\":[str],\"spare_procurement\":str,\"citations\":[int]}. Cite bracket numbers.")
    user = f"CONTEXT (SOPs/manuals):\n{context}\n\nDIAGNOSIS/RISK CONTEXT:\n{context_blob}\n\nQUERY: {query}"
    out = llm.chat_json([{"role": "system", "content": sys}, {"role": "user", "content": user}])
    out["_citations"] = _cites(results)
    return out


# ------------------------------------------------------------- Plant overview
def plant_overview_agent(top_n: int = 8) -> Dict:
    fleet = predictive.fleet_scan()
    ok = [f for f in fleet if "error" not in f]
    # enrich with spares lead time + delay severity for bottleneck view
    for f in ok:
        sp = base.spares_for_type(f["type"])
        f["max_lead_days"] = max((s["procurement_lead_time_days"] for s in sp), default=0)
        f["min_stock"] = min((s["stock_qty"] for s in sp), default=99)
        dp = base.delay_profile(f["asset_id"])
        f["delay_min_30d"] = dp["total_delay_minutes_30d"]
        f["delay_severity"] = dp["delay_severity"]
    return {"ranked": ok[:top_n], "total_assets": len(ok),
            "critical_count": sum(1 for f in ok if f.get("severity") == "Critical")}
