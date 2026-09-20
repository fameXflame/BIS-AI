import asyncio
from search_engine.hybrid_search import HybridSearchEngine
from data_engine import get_all_standards

async def main():
    engine = HybridSearchEngine(get_all_standards())
    test_queries = [
        # Non-BIS queries (Out of scope)
        "what is the recipe for chicken biryani",
        "who is the best cricket captain in IPL",
        "tell me a funny joke to make me laugh",
        
        # Real BIS queries
        "I want to manufacture an electric kettle in India. What tests are required?",
        "safety standards for domestic pressure cookers and burst tests",
        "gold hallmarking purity standards in India",
        "drinking water permissible limits for lead and nitrate"
    ]

    for q in test_queries:
        print("=" * 80)
        print("INPUT QUERY:", q)
        res = await engine.search(q, top_k=2)
        print("IS BIS RELATED:", res.get("is_bis_related"))
        print("SUMMARY:", res["summary"])
        print("AI WALK-ALONG:\n", res.get("ai_walkalong"))
        print("STANDARDS COUNT:", len(res["standards"]))
        for s in res["standards"]:
            print(f"  * [{s['is_code']}] {s['title']} ({s['confidence']}%)")
        print()

if __name__ == "__main__":
    asyncio.run(main())
