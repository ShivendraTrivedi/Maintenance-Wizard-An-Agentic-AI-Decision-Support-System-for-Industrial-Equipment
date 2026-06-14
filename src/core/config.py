"""Central configuration. Loads .env and exposes paths + model names."""
import os
from dotenv import load_dotenv

load_dotenv()

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "data")
DOCS = os.path.join(DATA, "documents")
SENSORS = os.path.join(DATA, "sensors")
SPARES = os.path.join(DATA, "spares", "spares_catalogue.csv")
DELAYS = os.path.join(DATA, "delays", "delay_events.csv")
VECTORSTORE = os.path.join(DATA, "vectorstore")
FEEDBACK = os.path.join(DATA, "feedback", "feedback.jsonl")
LOGBOOK = os.path.join(DATA, "logbook", "logbook.jsonl")
MANIFEST = os.path.join(DATA, "manifest.json")

def _setting(name: str, default: str = "") -> str:
    """Read config from environment first, then Streamlit secrets.

    Locally this reads from .env (via load_dotenv). On Streamlit Community Cloud
    you set the same keys under "Secrets", which works either way: Streamlit
    exposes them as env vars, and we also fall back to st.secrets directly.
    """
    val = os.getenv(name)
    if val:
        return val
    try:
        import streamlit as st  # available wherever the app runs
        if name in st.secrets:
            return str(st.secrets[name])
    except Exception:
        pass
    return default


OPENAI_API_KEY = _setting("OPENAI_API_KEY", "")
CHAT_MODEL = _setting("OPENAI_MODEL", "gpt-4o-mini")
EMBED_MODEL = _setting("OPENAI_EMBED_MODEL", "text-embedding-3-small")

os.makedirs(VECTORSTORE, exist_ok=True)
os.makedirs(os.path.dirname(FEEDBACK), exist_ok=True)
os.makedirs(os.path.dirname(LOGBOOK), exist_ok=True)
