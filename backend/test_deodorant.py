import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
sys.stdout.reconfigure(encoding='utf-8')

from data_engine.standards_db import get_all_standards
from search_engine.hybrid_search import HybridSearchEngine

stds = get_all_standards()
engine = HybridSearchEngine(stds)

async def test():
    res = await engine.search("deodrant manufacturing", top_k=8)
    print("=== DEODORANT SEARCH RESULTS ===")
    print("Query:", res["query_original"])
    print("Summary:", res["summary"])
    print("Walk-along:", res["ai_walkalong"])
    print(f"Total results: {res['total_results']}\n")
    for idx, s in enumerate(res["standards"], 1):
        print(f"#{idx} {s['is_code']} ({s['confidence']}%) — {s['title']}")

asyncio.run(test())
