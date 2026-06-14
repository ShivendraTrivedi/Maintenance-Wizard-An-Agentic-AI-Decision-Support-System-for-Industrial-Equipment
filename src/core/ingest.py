"""Ingest the document corpus into the vector store.

Walks data/documents/**, chunks each markdown file, tags it with metadata
(source path, doc_type, asset_id), embeds all chunks, and persists the index.
"""
import os
import re
import glob
from typing import List, Dict
from . import config, llm
from .vectorstore import VectorStore

DOC_TYPE_DIRS = {
    "manuals": "manual",
    "sops": "sop",
    "failure_reports": "failure_report",
    "maintenance_logs": "maintenance_log",
    "delay_logs": "delay_log",
}

ASSET_RE = re.compile(r"([A-Z]+(?:-[A-Z]+)?-\d{2})")


def _chunk(text: str, max_chars: int = 1100, overlap: int = 150) -> List[str]:
    """Chunk on blank lines, packing paragraphs up to max_chars with small overlap."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if len(cur) + len(p) + 2 <= max_chars:
            cur = f"{cur}\n\n{p}" if cur else p
        else:
            if cur:
                chunks.append(cur)
            if len(p) > max_chars:  # very long paragraph -> hard split
                for i in range(0, len(p), max_chars - overlap):
                    chunks.append(p[i:i + max_chars])
                cur = ""
            else:
                cur = p
    if cur:
        chunks.append(cur)
    return chunks


def collect_documents() -> List[Dict]:
    items = []
    for sub, dtype in DOC_TYPE_DIRS.items():
        for path in sorted(glob.glob(os.path.join(config.DOCS, sub, "*.md"))):
            with open(path) as f:
                text = f.read()
            fname = os.path.basename(path)
            m = ASSET_RE.search(fname)
            asset_id = m.group(1) if m else None
            for ci, chunk in enumerate(_chunk(text)):
                items.append({
                    "text": chunk,
                    "meta": {
                        "source": os.path.relpath(path, config.ROOT),
                        "doc_type": dtype,
                        "asset_id": asset_id,
                        "chunk": ci,
                        "title": text.splitlines()[0].lstrip("# ").strip(),
                    },
                })
    return items


def build_index(verbose: bool = True) -> VectorStore:
    items = collect_documents()
    texts = [it["text"] for it in items]
    metas = [it["meta"] for it in items]
    if verbose:
        print(f"Embedding {len(texts)} chunks from {len(set(m['source'] for m in metas))} documents...")
    embeddings = llm.embed(texts)
    store = VectorStore(config.VECTORSTORE)
    store.build(texts, embeddings, metas)
    if verbose:
        print(f"Vector store built: {store.size} chunks -> {config.VECTORSTORE}")
    return store


def load_index() -> VectorStore:
    store = VectorStore(config.VECTORSTORE)
    if not store.load():
        store = build_index()
    return store


if __name__ == "__main__":
    build_index()
