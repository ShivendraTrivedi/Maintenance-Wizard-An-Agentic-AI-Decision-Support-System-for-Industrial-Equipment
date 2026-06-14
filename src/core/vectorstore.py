"""Self-contained NumPy cosine-similarity vector store.

No external DB. Embeddings + metadata are persisted to .npz / .json so the
index builds once and loads instantly. Plenty fast for our corpus size and
fully transparent (good for explainability).
"""
import os
import json
import numpy as np
from typing import List, Dict, Optional


class VectorStore:
    def __init__(self, path: str):
        self.path = path
        self.emb_file = os.path.join(path, "embeddings.npz")
        self.meta_file = os.path.join(path, "metadata.json")
        self.vectors: Optional[np.ndarray] = None   # (N, d), L2-normalised
        self.metadatas: List[Dict] = []
        self.documents: List[str] = []

    # ---------- build ----------
    def build(self, documents: List[str], embeddings: List[List[float]], metadatas: List[Dict]):
        v = np.asarray(embeddings, dtype=np.float32)
        norms = np.linalg.norm(v, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        self.vectors = v / norms
        self.documents = documents
        self.metadatas = metadatas
        self.save()

    def save(self):
        os.makedirs(self.path, exist_ok=True)
        np.savez_compressed(self.emb_file, vectors=self.vectors)
        with open(self.meta_file, "w") as f:
            json.dump({"documents": self.documents, "metadatas": self.metadatas}, f)

    def load(self) -> bool:
        if not (os.path.exists(self.emb_file) and os.path.exists(self.meta_file)):
            return False
        self.vectors = np.load(self.emb_file)["vectors"]
        with open(self.meta_file) as f:
            blob = json.load(f)
        self.documents = blob["documents"]
        self.metadatas = blob["metadatas"]
        return True

    @property
    def size(self) -> int:
        return 0 if self.vectors is None else self.vectors.shape[0]

    # ---------- query ----------
    def search(self, query_embedding: List[float], k: int = 6,
               where: Optional[Dict] = None) -> List[Dict]:
        if self.vectors is None or self.size == 0:
            return []
        q = np.asarray(query_embedding, dtype=np.float32)
        q = q / (np.linalg.norm(q) or 1.0)
        sims = self.vectors @ q  # cosine since both normalised

        idx = np.arange(self.size)
        if where:
            mask = np.ones(self.size, dtype=bool)
            for key, val in where.items():
                vals = val if isinstance(val, (list, tuple, set)) else [val]
                mask &= np.array([self.metadatas[i].get(key) in vals for i in range(self.size)])
            idx = idx[mask]
            if idx.size == 0:
                idx = np.arange(self.size)  # fall back to global if filter empties

        sub = sims[idx]
        top = idx[np.argsort(-sub)[:k]]
        results = []
        for rank, i in enumerate(top):
            results.append({
                "rank": rank + 1,
                "score": float(sims[i]),
                "document": self.documents[i],
                "metadata": self.metadatas[i],
            })
        return results
