import asyncio
from dotenv import load_dotenv
load_dotenv()
from search_engine.hybrid_search import HybridSearchEngine
from data_engine import get_all_standards

async def test():
    engine = HybridSearchEngine(get_all_standards())
    q = "i wanna open a wine factory what are the requiremnets and standards needed for it ."
    print("Searching query:", q)
    res = await engine.search(q, top_k=2)
    print("\n--- LIVE GEMINI 3.6 FLASH SYNTHESIS ---")
    print("Summary:\n", res["summary"])
    print("\n--- AI WALK-ALONG ADVISORY ---")
    print(res.get("ai_walkalong"))
    print("\n--- MATCHED STANDARDS ---")
    for s in res["standards"]:
        print(f"  * [{s['is_code']}] {s['title']} ({s.get('confidence')}% match)")

if __name__ == "__main__":
    asyncio.run(test())
