"""
BIS AI — Official Hackathon Inference Benchmark Script
======================================================
CLI entry point conforming to the SIH / BIS Hackathon evaluation specification.
Uses Hybrid Dense Semantic Vector Search + BM25 + Neural Cross-Encoder Reranking.

Usage:
    python inference.py --input <path_to_test_set.json> --output <path_to_results.json>
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

# Ensure backend path is available
sys.path.insert(0, os.path.dirname(__file__))

from data_engine import get_all_standards
from search_engine.hybrid_search import HybridSearchEngine


def run_inference(input_path: str, output_path: str, top_k: int = 5):
    if not os.path.exists(input_path):
        print(f"[Error] Input file not found: {input_path}")
        sys.exit(1)

    print(f"[BIS AI Benchmark] Loading official standards database...")
    standards = get_all_standards()
    print(f"[BIS AI Benchmark] Indexed {len(standards)} standards into search engine.")

    print(f"[BIS AI Benchmark] Initializing Hybrid Dense Semantic & Reranking Engine...")
    t_init_start = time.perf_counter()
    engine = HybridSearchEngine(standards)
    t_init_end = time.perf_counter()
    print(f"[BIS AI Benchmark] Search engine ready in {t_init_end - t_init_start:.2f}s.")

    print(f"[BIS AI Benchmark] Reading test set from: {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        test_queries = json.load(f)

    results = []
    total_latency = 0.0

    print(f"[BIS AI Benchmark] Evaluating {len(test_queries)} queries...")
    for idx, item in enumerate(test_queries, start=1):
        q_id = item.get("id", f"Q-{idx:02d}")
        query_text = item.get("query", "")
        expected = item.get("expected_standards", [])

        t0 = time.perf_counter()
        hits = engine.search_candidates(query_text, top_k=top_k)
        t1 = time.perf_counter()

        latency = round(t1 - t0, 4)
        total_latency += latency

        retrieved_codes = [h["standard"]["is_code"] for h in hits]

        results.append({
            "id": q_id,
            "query": query_text,
            "expected_standards": expected,
            "retrieved_standards": retrieved_codes,
            "latency_seconds": latency,
        })

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    avg_latency = total_latency / max(1, len(test_queries))
    print(f"[BIS AI Benchmark] Wrote {len(results)} outputs to {output_path}")
    print(f"[BIS AI Benchmark] Avg Latency: {avg_latency:.4f}s per query.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BIS AI Hackathon Inference Runner")
    parser.add_argument("--input", type=str, required=True, help="Path to input test queries JSON")
    parser.add_argument("--output", type=str, required=True, help="Path to write output results JSON")
    parser.add_argument("--top_k", type=int, default=5, help="Number of standards to retrieve per query")

    args = parser.parse_args()
    run_inference(args.input, args.output, args.top_k)
