import time
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from search_engine.semantic_search import SemanticSearchEngine
from search_engine.reranker import NeuralReranker

print("--- Initializing Semantic Search Engine ---")
t0 = time.perf_counter()
engine = SemanticSearchEngine()
t1 = time.perf_counter()
print(f"Loaded semantic index in {t1 - t0:.4f} seconds!")

queries = [
    "device to boil water for tea",
    "33 Grade Ordinary Portland Cement",
    "plastic chairs for school classrooms",
    "vessel for brewing grape wine",
    "safety belts for construction workers falling from heights",
]

reranker = NeuralReranker()

for q in queries:
    t_start = time.perf_counter()
    results = engine.search(q, top_k=5)
    reranked = reranker.rerank(q, results, top_k=3)
    t_end = time.perf_counter()

    print(f"\nQuery: '{q}' (took {t_end - t_start:.4f}s)")
    for rank, r in enumerate(reranked, 1):
        std = r["standard"]
        print(f"  #{rank} {std['is_code']} — {std['title']} (Rerank: {r.get('rerank_score', 0):.3f}, Semantic: {r.get('semantic_score', 0):.3f})")
