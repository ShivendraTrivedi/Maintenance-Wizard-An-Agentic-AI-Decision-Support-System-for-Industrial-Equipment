"""
Maintenance Wizard — Streamlit application.

Tabs:
  Live Monitor - real-time ticking sensor feed, live risk, fault-injection demo
  Dashboard    - equipment health: sensor trends, normal bands, anomalies, RUL
  Fleet        - plant-wide health heatmap across areas
  Alerts       - real-time abnormal-alert report across the fleet (filterable)
  Chat         - conversational, multi-turn, cited answers + feedback loop
  Reports      - structured maintenance report generation (downloadable)
  Logbook      - automatic digital maintenance logbook

Run:  streamlit run app.py
"""
import os
import json
from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.core import predictive, config, stream
from src.agents import orchestrator, base, specialists as sp
from src.agents import reporting

st.set_page_config(page_title="Maintenance Wizard", page_icon="🛠️", layout="wide",
                   initial_sidebar_state="expanded")

SEV_COLOR = {"Critical": "#C0392B", "High": "#E67E22", "Medium": "#F1C40F",
             "Low": "#27AE60", "info": "#1F5C8B"}
SEV_RANK = {"Critical": 3, "High": 2, "Medium": 1, "Low": 0}

# --------------------------------------------------------------------- styling
st.markdown("""
<style>
  .block-container {padding-top: 1.4rem; padding-bottom: 2rem; max-width: 1500px;}
  /* hero header */
  .mw-hero {
    background: linear-gradient(110deg, #102A43 0%, #1F5C8B 55%, #2B7DB8 100%);
    border-radius: 16px; padding: 18px 26px; color: #fff; margin-bottom: 14px;
    box-shadow: 0 6px 22px rgba(16,42,67,.25);
  }
  .mw-hero h1 {font-size: 1.55rem; margin: 0; font-weight: 700; letter-spacing:.3px;}
  .mw-hero p  {margin: 4px 0 0; opacity: .85; font-size: .9rem;}
  /* KPI cards */
  .kpi {background:#fff; border-radius:14px; padding:14px 16px; border:1px solid #E3E8EF;
        box-shadow:0 2px 10px rgba(16,42,67,.05); height:100%;}
  .kpi .lbl {font-size:.72rem; text-transform:uppercase; letter-spacing:.6px; color:#627D98; font-weight:600;}
  .kpi .val {font-size:1.9rem; font-weight:700; line-height:1.1; margin-top:2px;}
  .kpi .sub {font-size:.76rem; color:#829AB1; margin-top:2px;}
  /* status pill */
  .pill {display:inline-block; padding:2px 11px; border-radius:999px; font-size:.74rem;
         font-weight:700; color:#fff; letter-spacing:.3px;}
  .live-dot {height:9px;width:9px;background:#27AE60;border-radius:50%;display:inline-block;
             margin-right:6px;box-shadow:0 0 0 rgba(39,174,96,.6);animation:pulse 1.6s infinite;}
  @keyframes pulse {0%{box-shadow:0 0 0 0 rgba(39,174,96,.5);}70%{box-shadow:0 0 0 8px rgba(39,174,96,0);}100%{box-shadow:0 0 0 0 rgba(39,174,96,0);}}
  .stTabs [data-baseweb="tab-list"] {gap: 4px;}
  .stTabs [data-baseweb="tab"] {border-radius:8px 8px 0 0; padding:6px 14px; font-weight:600;}
  div[data-testid="stMetricValue"] {font-size:1.6rem;}
</style>
""", unsafe_allow_html=True)


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def pill(text, color):
    return f'<span class="pill" style="background:{color}">{text}</span>'


def kpi_card(label, value, sub="", color="#1A2733"):
    return (f'<div class="kpi"><div class="lbl">{label}</div>'
            f'<div class="val" style="color:{color}">{value}</div>'
            f'<div class="sub">{sub}</div></div>')


@st.cache_data(show_spinner=False)
def fleet():
    return sp.plant_overview_agent(top_n=100)


@st.cache_data(show_spinner=False)
def analyze_cached(aid):
    return predictive.analyze(aid)


@st.cache_data(show_spinner=False)
def asset_meta():
    return base.asset_index()


asset_ids = base.all_asset_ids()
meta = asset_meta()
fl = fleet()
ranked = fl["ranked"]
rank_by_id = {r["asset_id"]: r for r in ranked}

# ---------------------------------------------------------------------- sidebar
st.sidebar.markdown("### 🛠️ Maintenance Wizard")
st.sidebar.caption("Tata Steel AI Hackathon 2026 — Agentic AI")
role = st.sidebar.selectbox("👤 Your role", ["engineer", "supervisor", "planner"], index=0)
st.sidebar.divider()

crit_n = sum(1 for r in ranked if r.get("severity") == "Critical")
high_n = sum(1 for r in ranked if r.get("severity") == "High")
avg_risk = sum(r.get("risk", 0) for r in ranked) / max(1, len(ranked))
sc1, sc2 = st.sidebar.columns(2)
sc1.metric("Assets", len(asset_ids))
sc2.metric("Avg risk", f"{int(avg_risk*100)}%")
sc1.metric("🔴 Critical", crit_n)
sc2.metric("🟠 High", high_n)
if st.sidebar.button("🔄 Refresh fleet scan", use_container_width=True):
    st.cache_data.clear()
    st.rerun()

# LLM key status (live analytics never need it; Chat/Reports do)
_key = config.OPENAI_API_KEY or ""
if not _key or _key.startswith("your-"):
    st.sidebar.warning("⚠️ No OpenAI key set — AI Chat/Reports disabled. Add OPENAI_API_KEY to .env. "
                       "Live Monitor, Dashboard, Fleet & Alerts work without it.")
else:
    st.sidebar.caption(f"🔑 OpenAI key: …{_key[-4:]} (validated on first AI call)")
st.sidebar.divider()
st.sidebar.caption("Top risk right now")
for r in ranked[:5]:
    st.sidebar.markdown(
        f"{pill(r['severity'], SEV_COLOR.get(r['severity'], '#999'))} "
        f"**{r['asset_id']}** · {int(r['risk']*100)}%", unsafe_allow_html=True)

# ------------------------------------------------------------------- hero + KPI
st.markdown(
    '<div class="mw-hero"><h1>🛠️ Maintenance Wizard — Plant Command Centre</h1>'
    '<p>Agentic AI for diagnosis, root-cause, failure prediction & live equipment health '
    'across the steel plant.</p></div>', unsafe_allow_html=True)

p1_est = sum(1 for r in ranked if r.get("risk", 0) >= 0.7)
worst = ranked[0] if ranked else {"asset_id": "—", "severity": "info"}
k = st.columns(5)
k[0].markdown(kpi_card("Assets monitored", len(asset_ids), "across 7 plant areas"), unsafe_allow_html=True)
k[1].markdown(kpi_card("Critical alerts", crit_n, "immediate attention", SEV_COLOR["Critical"]),
              unsafe_allow_html=True)
k[2].markdown(kpi_card("High alerts", high_n, "monitor closely", SEV_COLOR["High"]),
              unsafe_allow_html=True)
k[3].markdown(kpi_card("Avg failure risk", f"{int(avg_risk*100)}%", "fleet mean"), unsafe_allow_html=True)
k[4].markdown(kpi_card("Top risk asset", worst["asset_id"],
                       f"{worst.get('severity','')}", SEV_COLOR.get(worst.get("severity"), "#1A2733")),
              unsafe_allow_html=True)
st.write("")

tab_live, tab_dash, tab_fleet, tab_alerts, tab_chat, tab_reports, tab_log = st.tabs(
    ["📡 Live Monitor", "📊 Dashboard", "🗺️ Fleet", "🚨 Alerts",
     "💬 Chat", "📑 Reports", "📒 Logbook"])

# ============================================================== LIVE MONITOR
with tab_live:
    lc1, lc2, lc3 = st.columns([2, 1, 1])
    with lc1:
        live_asset = st.selectbox("Asset under live watch", asset_ids,
                                  index=asset_ids.index(worst["asset_id"]) if worst["asset_id"] in asset_ids else 0,
                                  key="live_asset")
    with lc2:
        speed = st.select_slider("Refresh", options=["1s", "2s", "3s", "5s"], value="2s")
    with lc3:
        st.write("")
        playing = st.toggle("▶ Stream live", value=True, key="live_playing")

    bc1, bc2, _ = st.columns([1, 1, 3])
    if bc1.button("⚡ Simulate fault escalation", use_container_width=True):
        st.session_state.setdefault("buffers", {})
        if live_asset in st.session_state.get("buffers", {}):
            stream.inject_fault(st.session_state["buffers"][live_asset])
        st.toast(f"Injecting escalating fault on {live_asset}", icon="⚡")
    if bc2.button("↺ Reset stream", use_container_width=True):
        st.session_state.setdefault("buffers", {})
        st.session_state["buffers"].pop(live_asset, None)
        st.toast("Stream reset to baseline", icon="↺")

    interval = {"1s": 1, "2s": 2, "3s": 3, "5s": 5}[speed]

    # the live fragment re-runs every `interval` seconds on its own, leaving the
    # rest of the page untouched (Streamlit fragments)
    @st.fragment(run_every=interval if playing else None)
    def live_panel():
        st.session_state.setdefault("buffers", {})
        buffers = st.session_state["buffers"]
        if live_asset not in buffers:
            buffers[live_asset] = stream.init_buffer(live_asset)
        buf = buffers[live_asset]
        if playing:
            stream.tick(buf)
        df = buf["df"]
        a = predictive.analyze(live_asset, df=df)
        fr = a["failure_risk"]
        atype = a["asset_type"]

        status_txt = ("🟢 LIVE" if playing else "⏸ PAUSED")
        st.markdown(
            f'<span class="live-dot"></span>**{status_txt}** · {live_asset} · {atype} · '
            f'area: {meta.get(live_asset, {}).get("area","—")} · '
            f'tick #{buf["ticks"]} · last sample {df["timestamp"].iloc[-1]:%H:%M}',
            unsafe_allow_html=True)

        # live metric strip with deltas (current vs previous reading)
        sensors = a["per_sensor"]
        cols = st.columns(len(sensors) + 1)
        cols[0].markdown(kpi_card("Failure risk", f"{int(fr['probability']*100)}%",
                                  fr["severity"], SEV_COLOR.get(fr["severity"], "#1A2733")),
                         unsafe_allow_html=True)
        for i, s in enumerate(sensors, start=1):
            col = s["sensor"]
            prev = float(df[col].iloc[-2]) if len(df) > 1 else s["current"]
            delta = s["current"] - prev
            badge = {"normal": "🟢", "warning": "🟡", "out_of_band": "🔴"}.get(s["status"], "⚪")
            cols[i].metric(f"{badge} {col}", f"{s['current']}{s['unit']}", f"{delta:+.2f}")

        gcol, ccol = st.columns([1, 2])
        with gcol:
            gauge = go.Figure(go.Indicator(
                mode="gauge+number", value=fr["probability"] * 100,
                number={"suffix": "%"},
                title={"text": "Live failure risk"},
                gauge={"axis": {"range": [0, 100]},
                       "bar": {"color": SEV_COLOR.get(fr["severity"], "#1F5C8B")},
                       "steps": [{"range": [0, 25], "color": "#E8F8F0"},
                                 {"range": [25, 50], "color": "#FEF9E7"},
                                 {"range": [50, 75], "color": "#FDEBD0"},
                                 {"range": [75, 100], "color": "#FADBD8"}]}))
            gauge.update_layout(height=260, margin=dict(t=50, b=10, l=20, r=20))
            st.plotly_chart(gauge, use_container_width=True, key=f"gauge_{buf['ticks']}")
            rul = a["rul_days_estimate"]
            st.markdown(kpi_card("Est. remaining useful life",
                                 f"{rul} d" if rul is not None else "—",
                                 "trend-projected to band edge"), unsafe_allow_html=True)

        with ccol:
            # normalised multi-sensor live trace (each sensor scaled 0-100% of its band)
            fig = go.Figure()
            win = df.tail(120)
            for s in sensors:
                col = s["sensor"]
                lo, hi = s["normal_low"], s["normal_high"]
                norm = (win[col] - lo) / (hi - lo) * 100
                fig.add_trace(go.Scatter(x=win["timestamp"], y=norm, mode="lines", name=col))
            fig.add_hrect(y0=0, y1=100, fillcolor="green", opacity=0.05, line_width=0)
            fig.add_hline(y=100, line_dash="dot", line_color="#C0392B")
            fig.add_hline(y=0, line_dash="dot", line_color="#C0392B")
            fig.update_layout(height=340, margin=dict(t=30, b=10),
                              title="Live sensor trace (% of normal band — 0–100 = healthy)",
                              legend=dict(orientation="h", y=-0.18), yaxis_title="% of band")
            st.plotly_chart(fig, use_container_width=True, key=f"trace_{buf['ticks']}")

        if buf["events"]:
            st.markdown("**🔔 Live band-breach feed**")
            ev = pd.DataFrame(reversed(buf["events"]))
            st.dataframe(ev, use_container_width=True, hide_index=True, height=160)
        else:
            st.success("All sensors within their normal operating band.")

    live_panel()

# ================================================================= DASHBOARD
with tab_dash:
    st.subheader("Equipment Health Dashboard")
    dc1, dc2 = st.columns([1, 1])
    aid = dc1.selectbox("Select asset", asset_ids, key="dash_asset")
    m = meta.get(aid, {})
    dc2.markdown(
        f"**{m.get('type','')}** · {m.get('area','')} · {m.get('manufacturer','')} "
        f"· installed {m.get('install_year','')}")
    a = analyze_cached(aid)
    fr = a["failure_risk"]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Failure risk", f"{int(fr['probability']*100)}%", fr["severity"])
    c2.metric("RUL estimate (days)", a["rul_days_estimate"] if a["rul_days_estimate"] is not None else "—")
    c3.metric("Anomaly rate (recent)", f"{int(a['anomaly']['rate']*100)}%")
    c4.metric("Criticality", a["criticality"])

    gauge = go.Figure(go.Indicator(
        mode="gauge+number", value=fr["probability"] * 100, number={"suffix": "%"},
        title={"text": f"{aid} — Failure Risk"},
        gauge={"axis": {"range": [0, 100]},
               "bar": {"color": SEV_COLOR.get(fr["severity"], "#1F5C8B")},
               "steps": [{"range": [0, 25], "color": "#E8F8F0"},
                         {"range": [25, 50], "color": "#FEF9E7"},
                         {"range": [50, 75], "color": "#FDEBD0"},
                         {"range": [75, 100], "color": "#FADBD8"}]}))
    gauge.update_layout(height=240, margin=dict(t=40, b=10))
    st.plotly_chart(gauge, use_container_width=True)

    st.markdown("**Per-sensor status**")
    st.dataframe(pd.DataFrame(a["per_sensor"]), use_container_width=True, hide_index=True)

    df = predictive.load_sensor_df(aid)
    st.markdown("**Sensor trends** (shaded = normal operating band)")
    grid = st.columns(2)
    for i, s in enumerate(a["per_sensor"]):
        col = s["sensor"]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["timestamp"], y=df[col], mode="lines", name=col,
                                 line=dict(color="#1F5C8B")))
        fig.add_hrect(y0=s["normal_low"], y1=s["normal_high"], fillcolor="green",
                      opacity=0.08, line_width=0)
        fig.add_hline(y=s["normal_high"], line_dash="dot", line_color="#C0392B")
        fig.add_hline(y=s["normal_low"], line_dash="dot", line_color="#C0392B")
        fig.update_layout(height=240, margin=dict(t=34, b=10),
                          title=f"{col} ({s['unit']}) — {s['status']}", showlegend=False)
        grid[i % 2].plotly_chart(fig, use_container_width=True)

# ===================================================================== FLEET
with tab_fleet:
    st.subheader("🗺️ Plant-wide Health Map")
    st.caption("Every monitored asset, grouped by area. Size = process criticality, colour = live failure risk.")
    crit_w = {"Critical": 4, "High": 3, "Medium": 2, "Low": 1}
    fdf = pd.DataFrame(ranked)
    fdf["area"] = fdf["asset_id"].map(lambda x: meta.get(x, {}).get("area", "Other"))
    fdf["size"] = fdf["criticality"].map(crit_w).fillna(1)
    fdf["risk_pct"] = (fdf["risk"] * 100).round(0)
    fig = px.treemap(fdf, path=[px.Constant("Plant"), "area", "asset_id"],
                     values="size", color="risk_pct",
                     color_continuous_scale=["#27AE60", "#F1C40F", "#E67E22", "#C0392B"],
                     range_color=[0, 100],
                     custom_data=["severity", "rul_days"])
    fig.update_traces(hovertemplate="<b>%{label}</b><br>risk %{color:.0f}%<br>"
                                    "severity %{customdata[0]}<br>RUL %{customdata[1]} d<extra></extra>")
    fig.update_layout(height=520, margin=dict(t=20, b=10, l=10, r=10),
                      coloraxis_colorbar=dict(title="Risk %"))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("**Risk by plant area**")
    area_df = fdf.groupby("area").agg(assets=("asset_id", "count"),
                                      avg_risk=("risk", "mean"),
                                      critical=("severity", lambda s: (s == "Critical").sum())).reset_index()
    area_df["avg_risk"] = (area_df["avg_risk"] * 100).round(0)
    bar = px.bar(area_df.sort_values("avg_risk"), x="avg_risk", y="area", orientation="h",
                 color="avg_risk", color_continuous_scale=["#27AE60", "#E67E22", "#C0392B"],
                 range_color=[0, 100], text="avg_risk")
    bar.update_layout(height=320, margin=dict(t=10, b=10), xaxis_title="Avg failure risk %",
                      yaxis_title="", coloraxis_showscale=False)
    st.plotly_chart(bar, use_container_width=True)

# ==================================================================== ALERTS
with tab_alerts:
    st.subheader("🚨 Real-time Abnormal Alert Report")
    st.caption("Generated from the live sensor stream across the fleet, ranked by failure risk.")

    fcol1, fcol2 = st.columns([1, 1])
    areas = ["All areas"] + sorted({meta.get(r["asset_id"], {}).get("area", "Other") for r in ranked})
    sel_area = fcol1.selectbox("Filter by area", areas)
    sel_sev = fcol2.multiselect("Severity", ["Critical", "High", "Medium", "Low"],
                                default=["Critical", "High"])

    rows = []
    for r in ranked:
        r2 = dict(r)
        r2["area"] = meta.get(r["asset_id"], {}).get("area", "Other")
        rows.append(r2)
    if sel_area != "All areas":
        rows = [r for r in rows if r["area"] == sel_area]
    if sel_sev:
        rows = [r for r in rows if r["severity"] in sel_sev]

    crit = [r for r in rows if r["severity"] in ("Critical", "High")]
    if crit:
        st.error(f"⚠️ {len(crit)} assets require attention (Critical/High) in this view.")
    else:
        st.success("✅ No critical alerts in this view.")

    if rows:
        adf = pd.DataFrame(rows)
        cols = ["asset_id", "area", "type", "severity", "risk", "rul_days", "anomaly_rate",
                "delay_min_30d", "max_lead_days", "min_stock"]
        show = adf[[c for c in cols if c in adf.columns]].rename(columns={
            "risk": "failure_risk", "rul_days": "RUL_days", "anomaly_rate": "anomaly",
            "delay_min_30d": "delay_min", "max_lead_days": "spare_lead_d", "min_stock": "min_spare"})

        def hl(row):
            return [f"background-color: {SEV_COLOR.get(row['severity'], '#fff')}22"] * len(row)

        sty = show.style.apply(hl, axis=1).format({"failure_risk": "{:.2f}", "anomaly": "{:.2f}"})
        st.dataframe(sty, use_container_width=True, hide_index=True)
    else:
        st.info("No assets match the current filters.")

    st.markdown("**Role-based notification preview**")
    if role == "supervisor":
        st.info("Supervisor view: focus on P1 downtime risk and spares with long lead time.")
    elif role == "planner":
        st.info("Planner view: prioritise spare procurement for zero-stock, long-lead items below.")
        for r in [r for r in rows if r.get("min_stock") == 0 and r["severity"] in ("Critical", "High")]:
            st.write(f"• Order spares for **{r['asset_id']}** ({r['type']}) — "
                     f"lead {r.get('max_lead_days')}d, stock 0")
    else:
        st.info("Engineer view: open the Chat tab and ask about the top-ranked asset for full diagnosis.")

# ====================================================================== CHAT
with tab_chat:
    st.subheader("Ask the Maintenance Wizard")
    st.caption("Natural-language, multi-turn. Mention an asset id (e.g. HSM-M-06) or ask a plant-wide question.")

    st.session_state.setdefault("history", [])
    st.session_state.setdefault("last_bundle", None)

    for turn in st.session_state.history:
        with st.chat_message(turn["role"]):
            st.markdown(turn["content"])

    with st.form("chat_form", clear_on_submit=True):
        colA, colB = st.columns([3, 1])
        q = colA.text_input("Your question",
                            placeholder="e.g. CCM-OSC-01 oil temp is high — diagnose, root cause, risk and what to do",
                            label_visibility="collapsed")
        sel_asset = colB.selectbox("Focus asset (optional)", ["(auto-detect)"] + asset_ids,
                                   label_visibility="collapsed")
        submitted = st.form_submit_button("Ask", use_container_width=True)

    if submitted and q:
        st.session_state.history.append({"role": "user", "content": q})
        with st.chat_message("user"):
            st.markdown(q)
        with st.chat_message("assistant"):
            with st.spinner("Agents reasoning (diagnose → root cause → predict → risk → recommend)…"):
                aid_c = None if sel_asset == "(auto-detect)" else sel_asset
                try:
                    bundle = orchestrator.run(q, now(), asset_id=aid_c, role=role,
                                              history=st.session_state.history)
                except Exception as e:  # last-resort guard — never crash the UI
                    bundle = {"answer": f"⚠️ Could not complete the request: {e}", "citations": []}
            if bundle.get("answer", "").startswith("###") or "⚠️" in bundle.get("answer", ""):
                st.info("AI narrative unavailable — showing analytics-engine results below.")
            st.markdown(bundle["answer"])
            st.session_state.last_bundle = bundle
            st.session_state.history.append({"role": "assistant", "content": bundle["answer"]})

            if bundle.get("citations"):
                with st.expander(f"🔎 Sources / explainability ({len(bundle['citations'])} documents)"):
                    for c in bundle["citations"]:
                        st.markdown(f"- `{c['doc_type']}` · **{c.get('asset_id')}** · {c['source']}")
            with st.expander("🧩 Agent outputs (structured)"):
                for key in ["prediction", "diagnosis", "root_cause", "risk_priority", "recommendation"]:
                    if key in bundle:
                        st.markdown(f"**{key}**")
                        st.json(bundle[key], expanded=False)

    if st.session_state.last_bundle:
        st.divider()
        st.caption("Was this helpful? Your feedback improves future answers (feedback loop).")
        fc1, fc2, fc3 = st.columns([1, 1, 4])
        b = st.session_state.last_bundle
        if fc1.button("👍 Helpful"):
            reporting.record_feedback(b.get("answer", "")[:120], b.get("asset_id"),
                                      b["answer"][:300], "helpful", "", now())
            st.success("Thanks — recorded.")
        nh = fc2.button("👎 Not helpful")
        corr = fc3.text_input("Add a correction (optional)", key="corr")
        if nh or (corr and st.button("Submit correction")):
            reporting.record_feedback(b.get("answer", "")[:120], b.get("asset_id"),
                                      b["answer"][:300], "not_helpful", corr, now())
            st.warning("Recorded — the Wizard will honour this correction for this asset next time.")

# =================================================================== REPORTS
with tab_reports:
    st.subheader("📑 Structured Maintenance Report")
    raid = st.selectbox("Asset", asset_ids, key="rep_asset")
    rquery = st.text_input("Context / question for the report",
                           value=f"Full maintenance assessment for {raid}", key="rep_q")
    if st.button("Generate report"):
        with st.spinner("Running full agent pipeline and composing report…"):
            try:
                bundle = orchestrator.run(rquery, now(), asset_id=raid, role=role, want_report=True)
            except Exception as e:
                bundle = {"report": {"title": "Report unavailable",
                                     "executive_summary": f"⚠️ {e}"}}
        rep = bundle.get("report", {})
        if rep.get("_llm_error"):
            st.info("AI narrative unavailable — report contains analytics-engine results only.")
        st.markdown(f"### {rep.get('title','Maintenance Report')}")
        st.caption(f"Asset {rep.get('asset_id')} · generated {rep.get('generated_at')}")
        for sec in ["executive_summary", "diagnosis", "root_cause", "risk_and_priority",
                    "recommended_actions", "spares_note"]:
            if rep.get(sec):
                st.markdown(f"**{sec.replace('_',' ').title()}**")
                st.write(rep[sec])
        st.download_button("⬇️ Download report (JSON)", json.dumps(bundle, default=str, indent=2),
                           file_name=f"report_{raid}.json")

# =================================================================== LOGBOOK
with tab_log:
    st.subheader("📒 Digital Maintenance Logbook")
    st.caption("Auto-populated by the Wizard on every interaction; the searchable plant memory.")
    if os.path.exists(config.LOGBOOK):
        entries = [json.loads(l) for l in open(config.LOGBOOK) if l.strip()]
        entries = list(reversed(entries))[:200]
        ldf = pd.DataFrame(entries)
        srch = st.text_input("🔎 Search logbook", placeholder="asset id, severity or keyword")
        if srch:
            mask = ldf.apply(lambda r: srch.lower() in str(r.to_dict()).lower(), axis=1)
            ldf = ldf[mask]
        cols = [c for c in ["timestamp", "asset_id", "severity", "summary"] if c in ldf.columns]
        st.dataframe(ldf[cols], use_container_width=True, hide_index=True, height=480)
    else:
        st.info("No logbook entries yet — ask something in the Chat tab.")
