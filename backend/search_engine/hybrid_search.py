"""
Hybrid Search Engine for BIS Standards.
Combines:
1. Product / Domain Identification & Applicability Filtering
2. BM25 sparse lexical search (exact keyword / code precision)
3. BGE-small dense semantic vector search (concept & intent matching)
4. Reciprocal Rank Fusion (RRF) for rank-invariant score combination
5. Neural Cross-Encoder & Phrase Reranker for top-K contextual ranking
6. Grounded Confidence Scoring & AI synthesis
"""

from __future__ import annotations

import os
import re
import sys
from typing import Any

from search_engine.bm25_search import BM25SearchEngine
from search_engine.semantic_search import SemanticSearchEngine
from search_engine.reranker import NeuralReranker
from search_engine.applicability_filter import (
    identify_query_domain,
    filter_and_rank_by_applicability,
)
from services.llm_service import (
    analyze_and_magnify_query,
    synthesize_response,
    calculate_confidence,
    get_confidence_tier,
)


class HybridSearchEngine:
    """
    State-of-the-art hybrid search engine integrating BM25 lexical search,
    BGE dense vector embeddings, RRF fusion, domain applicability filtering,
    and Cross-Encoder neural reranking.
    """

    def __init__(self, standards: list[dict[str, Any]]):
        self._standards = standards
        self._bm25 = BM25SearchEngine(standards)
        self._semantic = SemanticSearchEngine(standards)
        self._reranker = NeuralReranker()

    def search_candidates(
        self,
        query: str,
        top_k: int = 5,
        division: str | None = None,
    ) -> list[dict[str, Any]]:
        """
        Pure search pipeline returning top_k ranked standards without LLM synthesis.
        Enforces product identification and domain applicability filtering.
        """
        # 1. Sparse BM25 retrieval
        bm25_hits = self._bm25.search(query, top_k=60, division=division)

        # 2. Dense Semantic retrieval
        semantic_hits = self._semantic.search(query, top_k=60, division=division)

        # 3. Reciprocal Rank Fusion (RRF)
        fused = self._rrf_fusion(bm25_hits, semantic_hits, k=60)

        # 4. Domain & Product Applicability Filtering
        applicable = filter_and_rank_by_applicability(query, fused)

        # 5. Neural Cross-Encoder & Phrase Reranker
        reranked = self._reranker.rerank(query, applicable, top_k=top_k)

        return reranked

    async def search(
        self,
        query: str,
        top_k: int = 8,
        division: str | None = None,
    ) -> dict[str, Any]:
        """
        Full intelligent search pipeline with query magnification,
        classification, applicability filtering, hybrid retrieval,
        neural reranking, and AI synthesis.
        """
        # Step 1: Query classification & magnification
        analysis = await analyze_and_magnify_query(query)
        is_bis_related = analysis.get("is_bis_related", True)

        # Retrieve top candidates with hybrid search
        reranked = self.search_candidates(query, top_k=top_k * 2, division=division)

        # Check if database has authentic matches to override false negatives
        if not is_bis_related and reranked:
            top_cand = reranked[0]
            if top_cand.get("semantic_score", 0.0) >= 0.60 or top_cand.get("bm25_score", 0.0) >= 2.5:
                is_bis_related = True

        # Handle out-of-scope queries
        if not is_bis_related or not reranked:
            synthesis = await synthesize_response(query, [], is_bis_related=False)
            return {
                "query_original": query,
                "query_magnified": "",
                "is_bis_related": False,
                "summary": synthesis["summary"],
                "ai_walkalong": synthesis["ai_walkalong"],
                "standards": [],
                "total_results": 0,
            }

        # Select top_k
        final_candidates = reranked[:top_k]

        # Step 2: Realistic, defensible confidence scoring & metadata enrichment
        q_lower = query.lower()
        q_words = [w for w in re.findall(r"[a-z0-9]+", q_lower) if len(w) >= 4]

        for item in final_candidates:
            std = item["standard"]
            rerank_score = item.get("rerank_score", 0.5)
            semantic_score = item.get("semantic_score", 0.5)
            title_lower = std.get("title", "").lower()
            code_lower = std.get("is_code", "").lower()

            exact_title_match = any(w in title_lower or w in code_lower for w in q_words)
            domain_aligned = item.get("domain_aligned", True)

            if exact_title_match and rerank_score > 0.35:
                conf = min(98.0, 93.0 + min(5.0, rerank_score * 3.0))
            elif domain_aligned and (rerank_score > 0.20 or semantic_score > 0.65):
                conf = min(92.0, 84.0 + min(8.0, rerank_score * 5.0))
            elif domain_aligned:
                conf = min(84.0, 75.0 + min(8.0, rerank_score * 4.0))
            else:
                conf = max(42.0, min(65.0, 50.0 + rerank_score * 10.0))

            conf = round(conf, 1)
            std["confidence"] = conf
            std["confidence_tier"] = get_confidence_tier(conf)
            if not std.get("highlight_reason"):
                std["highlight_reason"] = std.get("scope", "")[:200]
            std["abstract_scope"] = std.get("scope", "")
            std["test_requirements"] = std.get("test_requirements", "")
            std["certification_process"] = std.get("certification_process", "")
            std["mandatory"] = bool(std.get("mandatory", False))

        standards_list = [c["standard"] for c in final_candidates]

        # Step 3: AI synthesis & walk-along advisory
        synthesis = await synthesize_response(query, standards_list, is_bis_related=True)

        return {
            "query_original": query,
            "query_magnified": ", ".join(analysis.get("keywords", [])),
            "is_bis_related": True,
            "summary": synthesis["summary"],
            "ai_walkalong": synthesis["ai_walkalong"],
            "standards": standards_list,
            "total_results": len(standards_list),
        }

    def _rrf_fusion(
        self,
        bm25_hits: list[dict[str, Any]],
        semantic_hits: list[dict[str, Any]],
        k: int = 60,
    ) -> list[dict[str, Any]]:
        """
        Reciprocal Rank Fusion (RRF) combining BM25 sparse hits and dense semantic hits.
        """
        scores: dict[str, float] = {}
        entries: dict[str, dict[str, Any]] = {}

        # Process BM25 hits
        for rank, hit in enumerate(bm25_hits):
            code = hit["standard"]["is_code"]
            rrf_val = 1.0 / (k + rank + 1)
            scores[code] = scores.get(code, 0.0) + rrf_val
            if code not in entries:
                entries[code] = {
                    "standard": hit["standard"],
                    "bm25_score": hit.get("bm25_score", 0.0),
                    "semantic_score": 0.0,
                    "is_code": code,
                }
            else:
                entries[code]["bm25_score"] = hit.get("bm25_score", 0.0)

        # Process Semantic hits
        for rank, hit in enumerate(semantic_hits):
            code = hit["standard"]["is_code"]
            rrf_val = 1.0 / (k + rank + 1)
            scores[code] = scores.get(code, 0.0) + rrf_val
            if code not in entries:
                entries[code] = {
                    "standard": hit["standard"],
                    "bm25_score": 0.0,
                    "semantic_score": hit.get("semantic_score", 0.0),
                    "is_code": code,
                }
            else:
                entries[code]["semantic_score"] = hit.get("semantic_score", 0.0)

        # Sort entries by fused RRF score
        sorted_codes = sorted(scores.keys(), key=lambda c: scores[c], reverse=True)
        fused_results = []
        for code in sorted_codes:
            item = entries[code]
            item["rrf_score"] = scores[code]
            fused_results.append(item)

        return fused_results
