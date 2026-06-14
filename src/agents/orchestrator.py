"""Orchestrator: the manager agent.

Plans which specialist agents to invoke for a query, runs them, injects
feedback hints (closed loop), synthesises one explainable answer, writes a
logbook entry, and returns the full structured bundle for the UI.
"""
from typing import Dict, List, Optional, Callable
from ..core import llm
from ..core.llm import LLMUnavailable
from . import base, specialists as sp
from . import reporting


def _safe(fn: Callable, *args) -> Dict:
    """Run a specialist agent; if the LLM is down, return a stub instead of crashing."""
    try:
        return fn(*args)
    except LLMUnavailable as e:
        return {"_llm_error": str(e)}


def run(query: str, timestamp: str, asset_id: Optional[str] = None,
        role: str = "engineer", history: Optional[List[dict]] = None,
        want_report: bool = False) -> Dict:
    history = history or []
    convo = _recent_convo(history)
    # resolve asset: explicit arg -> current query -> carried forward from history
    asset_id = asset_id or base.resolve_asset_id(query) or _asset_from_history(history)
    # context-aware intent detection (a bare "what about the bearing?" still classifies)
    intents = base.detect_intents((convo + "\n" + query) if convo else query)

    # plant-wide question shortcut
    if "plant_overview" in intents or (asset_id is None and any(
            w in query.lower() for w in ["plant", "fleet", "bottleneck", "priorit", "which equipment"])):
        overview = sp.plant_overview_agent()
        answer = _synthesize_overview(query, overview, role)
        reporting.write_logbook(None, answer[:400], "info", timestamp)
        return {"asset_id": None, "intents": intents, "plant_overview": overview,
                "answer": answer, "citations": [], "role": role}

    bundle: Dict = {"asset_id": asset_id, "intents": intents}
    feedback_hint = reporting.load_feedback_hints(asset_id)

    # sensor summary first (feeds the other agents)
    sensor_summary = ""
    if asset_id:
        try:
            sensor_summary = sp.sensor_summary_text(asset_id)
        except Exception:
            sensor_summary = ""

    run_all = "general_qa" not in intents or len(intents) > 1

    if asset_id and ("predict" in intents or run_all):
        bundle["prediction"] = _safe(sp.prediction_agent, asset_id)

    if "diagnose" in intents or run_all:
        bundle["diagnosis"] = _safe(sp.diagnostic_agent, query, asset_id, sensor_summary)

    if "root_cause" in intents or run_all:
        faults_text = str(bundle.get("diagnosis", {}).get("probable_faults", ""))
        bundle["root_cause"] = _safe(sp.root_cause_agent, query, asset_id, faults_text)

    if asset_id and ("risk_priority" in intents or run_all):
        # risk/priority is fully deterministic (no LLM) — keep it raw so it always works
        bundle["risk_priority"] = sp.risk_priority_agent(asset_id)

    if "recommend" in intents or run_all:
        ctx_blob = _bundle_context(bundle) + (f"\nENGINEER FEEDBACK TO HONOUR:\n{feedback_hint}" if feedback_hint else "")
        bundle["recommendation"] = _safe(sp.recommendation_agent, query, asset_id, ctx_blob)

    # final synthesis (explainable, role-aware, conversation-aware)
    answer = _synthesize(query, bundle, role, feedback_hint, convo)
    citations = _collect_citations(bundle)
    bundle["answer"] = answer
    bundle["citations"] = citations
    bundle["role"] = role

    severity = "info"
    if "risk_priority" in bundle:
        severity = bundle["risk_priority"].get("failure_risk", {}).get("severity", "info")
    elif "prediction" in bundle and "analysis" in bundle["prediction"]:
        severity = bundle["prediction"]["analysis"]["failure_risk"]["severity"]

    actions = bundle.get("recommendation", {}).get("immediate_actions", [])
    reporting.write_logbook(asset_id, answer[:400], severity, timestamp, actions)

    if want_report:
        bundle["report"] = reporting.report_agent(query, asset_id, bundle, timestamp)

    return bundle


# ---------------------------------------------------------------- helpers
def _recent_convo(history: List[dict], max_turns: int = 6) -> str:
    """Render the last few turns as context for the LLM (excludes the current query)."""
    turns = [h for h in history if h.get("role") in ("user", "assistant")][-max_turns:]
    return "\n".join(f"{h['role'].upper()}: {h['content'][:400]}" for h in turns)


def _asset_from_history(history: List[dict]) -> Optional[str]:
    """Carry forward the most recently mentioned asset for follow-up questions."""
    for h in reversed(history):
        aid = base.resolve_asset_id(h.get("content", ""))
        if aid:
            return aid
    return None


def _bundle_context(bundle: Dict) -> str:
    parts = []
    if "diagnosis" in bundle:
        parts.append(f"DIAGNOSIS: {bundle['diagnosis'].get('summary','')} | "
                     f"faults={bundle['diagnosis'].get('probable_faults','')}")
    if "root_cause" in bundle:
        parts.append(f"ROOT CAUSE: {bundle['root_cause'].get('root_causes','')}")
    if "risk_priority" in bundle:
        rp = bundle["risk_priority"]
        parts.append(f"RISK/PRIORITY: {rp.get('priority_band')} ({rp.get('urgency')}), "
                     f"score={rp.get('priority_score')}, {rp.get('rationale')}")
    if "prediction" in bundle:
        parts.append(f"PREDICTION: {bundle['prediction'].get('health_summary','')}")
    return "\n".join(parts)


def _collect_citations(bundle: Dict) -> List[Dict]:
    seen, out = set(), []
    for key in ("diagnosis", "root_cause", "recommendation"):
        for c in bundle.get(key, {}).get("_citations", []):
            sig = c["source"]
            if sig not in seen:
                seen.add(sig)
                out.append(c)
    return out


def _synthesize(query: str, bundle: Dict, role: str, feedback_hint: str, convo: str = "") -> str:
    sys = (f"You are the Maintenance Wizard orchestrator answering a {role}. Synthesise ONE clear, "
           "explainable answer from the specialist outputs below. Structure it with short headed sections: "
           "Diagnosis, Root Cause, Health & Prediction, Risk & Priority, Recommended Actions. Reference asset "
           "ids and keep it practical. If a section has no data, omit it. Do not invent facts beyond the bundle. "
           "Use the conversation so far to resolve follow-up references (e.g. 'it', 'that bearing').")
    if role == "supervisor":
        sys += " Keep it brief and decision-focused (priority, downtime risk, spares)."
    if feedback_hint:
        sys += f"\nIncorporate these prior engineer corrections where relevant:\n{feedback_hint}"
    convo_block = f"CONVERSATION SO FAR:\n{convo}\n\n" if convo else ""
    user = f"{convo_block}CURRENT QUERY: {query}\n\nSPECIALIST OUTPUTS:\n{_bundle_context(bundle)}\n\nFULL: {str(bundle)[:5000]}"
    try:
        return llm.chat([{"role": "system", "content": sys}, {"role": "user", "content": user}], max_tokens=900)
    except LLMUnavailable as e:
        return _fallback_answer(bundle, str(e))


def _fallback_answer(bundle: Dict, note: str) -> str:
    """Deterministic answer built from the analytics engine when the LLM is down."""
    aid = bundle.get("asset_id")
    lines = [f"### Maintenance summary — {aid or 'plant'}",
             "_AI narrative is unavailable; showing the analytics-engine results._\n"]
    pred = bundle.get("prediction", {})
    analysis = pred.get("analysis") if isinstance(pred, dict) else None
    if analysis:
        fr = analysis["failure_risk"]
        lines.append(f"**Health & Prediction** — failure risk **{fr['severity']}** "
                     f"({int(fr['probability']*100)}%), anomaly rate {int(analysis['anomaly']['rate']*100)}%, "
                     f"RUL {analysis['rul_days_estimate']} d.")
        oob = [s for s in analysis["per_sensor"] if s["status"] != "normal"]
        if oob:
            lines.append("Sensors of concern: " + ", ".join(
                f"`{s['sensor']}`={s['current']}{s['unit']} ({s['status']}, band {s['normal_low']}–{s['normal_high']})"
                for s in oob))
    rp = bundle.get("risk_priority")
    if isinstance(rp, dict) and "priority_band" in rp:
        lines.append(f"**Risk & Priority** — {rp['priority_band']} ({rp['urgency']}), "
                     f"score {rp['priority_score']}/100. {rp['rationale']}")
        sp_info = rp.get("spares", {})
        lines.append(f"**Spares** — min stock {sp_info.get('min_stock')}, "
                     f"max lead {sp_info.get('max_lead_time_days')} d.")
    lines.append(f"\n> ⚠️ {note}")
    return "\n\n".join(lines)


def _synthesize_overview(query: str, overview: Dict, role: str) -> str:
    sys = ("You are the Maintenance Wizard. Summarise the plant-level health and give a prioritised "
           "bottleneck list (asset, severity, risk, RUL, spares lead time). Recommend where to focus first. "
           "Be concise and practical.")
    try:
        return llm.chat([{"role": "system", "content": sys},
                         {"role": "user", "content": f"QUERY: {query}\nFLEET: {str(overview)[:4000]}"}],
                        max_tokens=700)
    except LLMUnavailable as e:
        return _fallback_overview(overview, str(e))


def _fallback_overview(overview: Dict, note: str) -> str:
    """Deterministic plant-wide bottleneck report (no LLM needed)."""
    ranked = overview.get("ranked", [])
    top = ranked[:8]
    lines = [f"### Plant-wide priorities — {overview.get('total_assets', len(ranked))} assets monitored",
             f"**{overview.get('critical_count', 0)} critical** alert(s) right now. "
             "Ranked by failure risk:\n",
             "| # | Asset | Type | Severity | Risk | RUL (d) | Spare lead (d) | Min stock | Delay (min/30d) |",
             "|---|-------|------|----------|------|---------|----------------|-----------|-----------------|"]
    for i, r in enumerate(top, 1):
        lines.append(f"| {i} | **{r['asset_id']}** | {r.get('type','')} | {r.get('severity','')} | "
                     f"{int(r.get('risk',0)*100)}% | {r.get('rul_days','—')} | "
                     f"{r.get('max_lead_days','—')} | {r.get('min_stock','—')} | {r.get('delay_min_30d','—')} |")
    focus = [r['asset_id'] for r in top[:3]]
    lines.append(f"\n**Where to focus this week:** {', '.join(focus)} — highest failure risk; "
                 "prioritise assets that also show zero spare stock and long procurement lead time.")
    lines.append(f"\n> ⚠️ {note}")
    return "\n".join(lines)
