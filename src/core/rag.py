"""Retrieval-Augmented Generation helper: retrieve cited context for a query."""
from typing import List, Dict, Optional
from . import llm
from .ingest import load_index

_store = None


def _get_store():
    global _store
    if _store is None:
        _store = load_index()
    return _store


def retrieve(query: str, k: int = 6, asset_id: Optional[str] = None,
             doc_types: Optional[List[str]] = None) -> List[Dict]:
    """Return top-k cited chunks for a query, optionally filtered."""
    store = _get_store()
    where = {}
    if asset_id:
        where["asset_id"] = asset_id
    if doc_types:
        where["doc_type"] = doc_types
    q_emb = llm.embed([query])[0]
    return store.search(q_emb, k=k, where=where or None)


def format_context(results: List[Dict]) -> str:
    """Format retrieved chunks into a numbered, citable context block."""
    blocks = []
    for r in results:
        m = r["metadata"]
        cite = f"[{r['rank']}] {m.get('title','')} | type={m.get('doc_type')} | asset={m.get('asset_id')} | src={m.get('source')}"
        blocks.append(f"{cite}\n{r['document']}")
    return "\n\n---\n\n".join(blocks)


def answer(query: str, k: int = 6, asset_id: Optional[str] = None) -> Dict:
    """Simple grounded Q&A used as a baseline / sanity check."""
    results = retrieve(query, k=k, asset_id=asset_id)
    context = format_context(results)
    sys = ("You are a maintenance assistant for a steel plant. Answer ONLY from the provided context. "
           "Cite sources inline using their bracket numbers like [1], [2]. If the context is insufficient, "
           "say so clearly.")
    user = f"CONTEXT:\n{context}\n\nQUESTION: {query}"
    text = llm.chat([{"role": "system", "content": sys}, {"role": "user", "content": user}])
    return {
        "answer": text,
        "citations": [{"n": r["rank"], "source": r["metadata"]["source"],
                       "doc_type": r["metadata"]["doc_type"], "asset_id": r["metadata"]["asset_id"],
                       "score": round(r["score"], 3)} for r in results],
    }
