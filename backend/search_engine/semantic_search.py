"""
Dense Semantic Vector Search Engine for BIS Standards.
Uses BAAI/bge-small-en-v1.5 embeddings with precomputed normalized index
for sub-15ms semantic matching against all 668 Indian Standards.
"""

from __future__ import annotations

import json
import os
import sys
import time
from typing import Any
import numpy as np
from fastembed import TextEmbedding

# Add backend root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_engine.standards_db import get_all_standards


class SemanticSearchEngine:
    """
    Dense semantic search engine powered by BGE-small-en-v1.5 (ONNX Runtime).
    Loads precomputed normalized embedding matrix for instant vector similarity.
    """

    def __init__(self, standards: list[dict[str, Any]] | None = None):
        self.standards = standards or get_all_standards()
        self.standards_by_code: dict[str, dict[str, Any]] = {
            s["is_code"]: s for s in self.standards
        }

        data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data_engine"))
        self.npy_path = os.path.join(data_dir, "standards_embeddings.npy")
        self.codes_path = os.path.join(data_dir, "standards_codes.json")

        self.model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
        self.embeddings: np.ndarray | None = None
        self.codes: list[str] = []

        self._load_or_build_index()

    def _load_or_build_index(self):
        """Loads precomputed index or computes it if missing or size mismatched."""
        if os.path.exists(self.npy_path) and os.path.exists(self.codes_path):
            try:
                self.embeddings = np.load(self.npy_path)
                with open(self.codes_path, "r", encoding="utf-8") as f:
                    self.codes = json.load(f)

                if len(self.codes) == len(self.standards) and self.embeddings.shape[0] == len(self.standards):
                    return
            except Exception as e:
                print(f"[SemanticSearch] Error loading cached embeddings: {e}. Recomputing...")

        # If cache invalid or missing, build it
        print("[SemanticSearch] Computing dense embeddings for standards corpus...")
        docs = []
        codes = []
        for s in self.standards:
            code = s.get("is_code", "")
            title = s.get("title", "")
            div = s.get("division", "") or s.get("department", "")
            scope = s.get("scope", "")[:800]
            kw = ", ".join(s.get("keywords", []))
            docs.append(f"{code}: {title}. Domain: {div}. Keywords: {kw}. Scope: {scope}")
            codes.append(code)

        embeddings_list = list(self.model.embed(docs, batch_size=64))
        mat = np.array(embeddings_list, dtype=np.float32)
        norms = np.linalg.norm(mat, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        self.embeddings = mat / norms
        self.codes = codes

        np.save(self.npy_path, self.embeddings)
        with open(self.codes_path, "w", encoding="utf-8") as f:
            json.dump(self.codes, f, indent=2)

    def search(
        self,
        query: str,
        top_k: int = 25,
        division: str | None = None,
    ) -> list[dict[str, Any]]:
        """
        Execute dense semantic search using cosine similarity against precomputed vectors.
        """
        if self.embeddings is None or len(self.codes) == 0:
            return []

        # Embed query text
        query_emb_list = list(self.model.embed([query]))
        if not query_emb_list:
            return []

        q_vec = np.array(query_emb_list[0], dtype=np.float32)
        norm = np.linalg.norm(q_vec)
        if norm > 0:
            q_vec = q_vec / norm

        # Fast cosine similarity: dot product with all normalized standard vectors
        scores = np.dot(self.embeddings, q_vec)

        # Get top candidate indices
        sorted_indices = np.argsort(scores)[::-1]

        results = []
        for idx in sorted_indices:
            code = self.codes[idx]
            std = self.standards_by_code.get(code)
            if not std:
                continue

            # Optional division filter
            if division and division.strip():
                std_div = (std.get("division") or std.get("department") or "").lower()
                if division.lower() not in std_div:
                    continue

            results.append({
                "standard": std,
                "semantic_score": float(scores[idx]),
                "is_code": code,
            })

            if len(results) >= top_k:
                break

        return results
