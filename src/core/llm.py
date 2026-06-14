"""Thin OpenAI wrapper: chat, JSON chat, and batched embeddings."""
import json
import time
from typing import List, Optional
from openai import OpenAI
from . import config

_client = OpenAI(api_key=config.OPENAI_API_KEY)


class LLMUnavailable(RuntimeError):
    """Raised when the LLM cannot be reached (missing/invalid key, quota, network).

    Callers catch this to fall back to deterministic, analytics-only answers
    instead of crashing the app with a raw OpenAI traceback.
    """


def _friendly(exc: Exception) -> "LLMUnavailable":
    msg = str(exc)
    if "invalid_api_key" in msg or "401" in msg or "Incorrect API key" in msg:
        hint = ("OpenAI rejected the API key (401). Set a valid OPENAI_API_KEY in .env "
                "and restart. AI text answers are disabled until then; live analytics still work.")
    elif "insufficient_quota" in msg or "429" in msg:
        hint = ("OpenAI quota/rate limit hit. AI text answers are paused; live analytics still work.")
    else:
        hint = f"LLM call failed ({type(exc).__name__}). Live analytics still work."
    return LLMUnavailable(hint)


def chat(messages: List[dict], model: Optional[str] = None, temperature: float = 0.2,
         max_tokens: int = 1200) -> str:
    """Plain text chat completion."""
    try:
        resp = _client.chat.completions.create(
            model=model or config.CHAT_MODEL,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
    except Exception as e:
        raise _friendly(e)
    return resp.choices[0].message.content.strip()


def chat_json(messages: List[dict], model: Optional[str] = None, temperature: float = 0.1,
              max_tokens: int = 1500) -> dict:
    """Chat completion constrained to a JSON object."""
    try:
        resp = _client.chat.completions.create(
            model=model or config.CHAT_MODEL,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format={"type": "json_object"},
        )
    except Exception as e:
        raise _friendly(e)
    raw = resp.choices[0].message.content.strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # best-effort salvage
        start, end = raw.find("{"), raw.rfind("}")
        return json.loads(raw[start:end + 1])


def embed(texts: List[str], model: Optional[str] = None, batch_size: int = 64) -> List[List[float]]:
    """Batched embeddings with simple retry."""
    out: List[List[float]] = []
    model = model or config.EMBED_MODEL
    for i in range(0, len(texts), batch_size):
        chunk = texts[i:i + batch_size]
        for attempt in range(3):
            try:
                resp = _client.embeddings.create(model=model, input=chunk)
                out.extend([d.embedding for d in resp.data])
                break
            except Exception as e:
                if attempt == 2:
                    raise _friendly(e)
                time.sleep(1.5 * (attempt + 1))
    return out
