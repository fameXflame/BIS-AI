"""
Build and persist dense semantic embeddings for all BIS standards.
Generates:
- backend/data_engine/standards_embeddings.npy
- backend/data_engine/standards_codes.json
"""

import json
import os
import sys
import time
import numpy as np
from fastembed import TextEmbedding

# Add backend root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_engine.standards_db import get_all_standards


def build_semantic_index():
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data_engine"))
    npy_path = os.path.join(data_dir, "standards_embeddings.npy")
    codes_path = os.path.join(data_dir, "standards_codes.json")

    print("[IndexBuilder] Loading standards from data_engine...")
    standards = get_all_standards()
    print(f"[IndexBuilder] Total standards loaded: {len(standards)}")

    docs = []
    codes = []
    for s in standards:
        code = s.get("is_code", "")
        title = s.get("title", "")
        div = s.get("division", "") or s.get("department", "")
        scope = s.get("scope", "")[:800]
        kw = ", ".join(s.get("keywords", []))

        doc_text = f"{code}: {title}. Domain: {div}. Keywords: {kw}. Scope: {scope}"
        docs.append(doc_text)
        codes.append(code)

    print("[IndexBuilder] Initializing BAAI/bge-small-en-v1.5 model...")
    model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

    print(f"[IndexBuilder] Computing embeddings for {len(docs)} documents...")
    t0 = time.perf_counter()
    embeddings_list = list(model.embed(docs, batch_size=64))
    t1 = time.perf_counter()

    embeddings = np.array(embeddings_list, dtype=np.float32)
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    embeddings_norm = embeddings / norms

    print(f"[IndexBuilder] Embeddings computed in {t1 - t0:.2f}s. Shape: {embeddings_norm.shape}")

    np.save(npy_path, embeddings_norm)
    with open(codes_path, "w", encoding="utf-8") as f:
        json.dump(codes, f, indent=2)

    print(f"[IndexBuilder] Successfully saved {npy_path} ({os.path.getsize(npy_path) / 1024:.1f} KB)")
    print(f"[IndexBuilder] Successfully saved {codes_path}")


if __name__ == "__main__":
    build_semantic_index()
