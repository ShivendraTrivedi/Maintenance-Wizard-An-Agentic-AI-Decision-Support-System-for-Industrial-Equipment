# 🛠️ Maintenance Wizard for Industrial Equipment
### Tata Steel AI Hackathon 2026 — Round 2: Agentic AI Challenge

An **agentic AI decision-support system** that helps steel-plant maintenance engineers
**diagnose** equipment issues, find **root causes**, **predict** failures and remaining
useful life, **assess risk & priority**, and generate **explainable, actionable
recommendations** — all from natural-language conversation, grounded in the plant's own
manuals, SOPs, failure reports and sensor data.

---

## 1. What it does (mapped to the problem statement)

| Requirement | How it is met |
|---|---|
| Contextual reasoning (LLM) | OpenAI GPT powers every agent's reasoning and synthesis. |
| Knowledge integration | RAG over manuals, SOPs, maintenance logs, failure reports & delay logs (cited). |
| Natural-language, multi-turn | Streamlit chat with conversation history and role awareness. |
| Explainable recommendations | Every answer cites the exact source documents + shows structured agent outputs. |
| Abnormality detection & failure prediction | Isolation-Forest anomaly detection + trend-based RUL + failure-risk scoring. |
| Feedback-driven improvement | 👍/👎 + corrections stored and re-injected into future answers (closed loop). |
| Real-time alerting | Fleet-wide abnormal-alert report, ranked by risk, with role-based notifications. |
| **Live IoT streaming** | ✅ Live Monitor tab: sensor feed *ticks in real time* (auto-refresh), live failure-risk gauge, on-demand fault-injection demo, live band-breach feed. |
| **Plant health map** | ✅ Fleet tab: interactive treemap of all assets by area, sized by criticality, coloured by live risk. |
| **Optional: chat UI** | ✅ Conversational interface. |
| **Optional: dashboard** | ✅ Health/anomaly/trend dashboard (Plotly). |
| **Optional: simulated IoT** | ✅ Synthetic sensor streams per asset. |
| **Optional: dynamic KB** | ✅ Re-indexable vector store; logbook grows per asset. |
| **Optional: digital logbook** | ✅ Auto-written on every interaction. |
| **Optional: role-based alerts** | ✅ Engineer / Supervisor / Planner views. |

---

## 2. Architecture (5 layers)

```
Presentation     Streamlit: Live Monitor · Dashboard · Fleet map · Alerts · Chat ·
      │                      Reports · Logbook  (role-aware, real-time auto-refresh)
      │
Agentic layer    Orchestrator → Diagnostic · Root-Cause · Prediction · Risk/Priority ·
      │                          Recommendation · Report/Logbook · Feedback
      │
Knowledge (RAG)  NumPy cosine vector store over OpenAI embeddings  +  Predictive ML engine
      │                                                               (Isolation Forest, RUL)
Data layer       Manuals · SOPs · Failure reports · Maintenance logs · Spares · Sensors · Feedback
```

**Why a NumPy vector store?** The environment runs Python 3.8, where current ChromaDB
builds fail. A self-contained cosine-similarity store (`src/core/vectorstore.py`) over
OpenAI embeddings has zero dependency risk, is fully transparent, and is more than fast
enough for this corpus — the retrieval interface is drop-in replaceable with Chroma/FAISS.

---

## 3. Technology stack

- **Language:** Python 3
- **LLM:** OpenAI GPT (`gpt-4o-mini` by default) — chat + embeddings
- **RAG:** custom NumPy cosine vector store + OpenAI `text-embedding-3-small`
- **Predictive ML:** scikit-learn (Isolation Forest), pandas, numpy
- **UI:** Streamlit + Plotly
- **Config:** python-dotenv (`.env`)

---

## 4. Install & run

```bash
# 1. From the project folder, install dependencies
pip3 install --user -r requirements.txt

# 2. Configure your key  (copy the template, then edit .env)
cp .env.example .env
#   -> set OPENAI_API_KEY=sk-...   (NEVER commit the real .env)

# 3. Generate the synthetic plant corpus  (483 docs, 37 assets, sensor streams)
python3 scripts/generate_corpus.py

# 4. Build the RAG vector index
python3 -m src.core.ingest

# 5a. Run the web app
streamlit run app.py
#    -> open http://localhost:8501

# 5b. OR run the no-UI demo (sample input/output)
python3 scripts/demo.py
```

> **Security:** the `.env` file is git-ignored. If a key was ever shared in plain text,
> rotate it at platform.openai.com.

---

## 5. Try these queries (in the Chat tab)

- `HSM-M-02 has high vibration and a hot bearing — diagnose, root cause, risk and what to do.`
- `CCM-OSC-02 oscillation is unstable and causing delays. What's the remaining useful life?`
- `Which equipment across the plant should we prioritise this week? Show the bottlenecks.`
- `What is the LOTO procedure for the BOF lance hoist?`

Switch the **role** (engineer / supervisor / planner) in the sidebar to see tailored
answers and alerts.

---

## 6. Project layout

```
.
├── app.py                      # Streamlit application (5 tabs)
├── requirements.txt
├── .env.example                # copy to .env and add your key
├── scripts/                    # tooling (not needed at runtime)
│   ├── generate_corpus.py      # synthetic plant document + sensor generator
│   ├── demo.py                 # CLI sample input/output demonstration
│   └── build_doc.py            # regenerates the .docx plan document
├── src/
│   ├── core/                   # config, llm, vectorstore, ingest, rag, predictive, stream, equipment_kb
│   └── agents/                 # base, specialists, reporting, orchestrator
└── data/
    ├── documents/{manuals,sops,failure_reports,maintenance_logs,delay_logs}/
    ├── sensors/                # per-asset sensor CSVs (simulated IoT)
    ├── delays/delay_events.csv # structured production-delay events
    ├── spares/spares_catalogue.csv
    ├── vectorstore/            # built index (git-ignored)
    ├── feedback/ logbook/      # feedback loop + digital logbook
    └── manifest.json
```

---

## 7. Assumptions & limitations

- Data is realistic **synthetic** (no live plant feed); IoT is **simulated** but the
  ingestion interface is ready for real sensors/MQTT.
- RUL and risk models demonstrate the **method** on sample data, not plant-certified accuracy.
- RAG grounding + citations reduce hallucination but do not eliminate it.
- The system is **decision support** — a human engineer makes the final call.
```
