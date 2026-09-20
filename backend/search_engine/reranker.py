"""
Cross-Encoder Neural Reranker & Exact Phrase Booster.
Takes top retrieved candidate standards and re-ranks them using
Xenova/ms-marco-MiniLM-L-6-v2 cross-encoder and exact n-gram phrase alignment.
"""

from __future__ import annotations

import math
import re
from typing import Any
from fastembed.rerank.cross_encoder import TextCrossEncoder


def _extract_ngrams(text: str, n: int = 2) -> list[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [" ".join(words[i : i + n]) for i in range(len(words) - n + 1)]


def _sigmoid(x: float) -> float:
    try:
        return 1.0 / (1.0 + math.exp(-x))
    except OverflowError:
        return 0.0 if x < 0 else 1.0


class NeuralReranker:
    """
    Neural Cross-Encoder Reranker with contextual phrase matching.
    """

    def __init__(self):
        self.model = TextCrossEncoder(model_name="Xenova/ms-marco-MiniLM-L-6-v2")

    def _phrase_boost(self, query: str, standard: dict[str, Any]) -> float:
        """
        Calculates phrase alignment boost between query and standard title/scope.
        Particularly rewards exact matches for distinguishing grades, types, and materials.
        """
        q_clean = query.lower()
        title = standard.get("title", "").lower()
        code = standard.get("is_code", "").lower()

        boost = 0.0
        scope = standard.get("scope", "").lower()

        # Word-level matches in title
        for word in re.findall(r"[a-z0-9]+", q_clean):
            if len(word) >= 4 and word in title:
                boost += 0.05

        # 4-gram, 3-gram, and 2-gram exact matches in title and scope
        for n, weight_title, weight_scope in [(4, 0.80, 0.35), (3, 0.50, 0.25), (2, 0.30, 0.15)]:
            ngrams = _extract_ngrams(query, n)
            for ng in ngrams:
                if ng in title:
                    boost += weight_title
                elif ng in code:
                    boost += weight_title * 1.2
                elif ng in scope:
                    boost += weight_scope

        # Special check for numbers/grades (e.g. 33 grade, 43 grade, 53 grade, part 2)
        grade_matches = re.findall(r"(\d+\s*grade|grade\s*\d+|part\s*\d+)", q_clean)
        for gm in grade_matches:
            gm_clean = gm.replace(" ", "")
            if gm in title or gm_clean in title.replace(" ", ""):
                boost += 1.20
            if gm in code or gm_clean in code.replace(" ", ""):
                boost += 1.20

        # Conflicting grade penalty (e.g. user wants 33 grade, but title is 43 grade or 53 grade)
        q_grades = set(re.findall(r"\b(\d+)\s*grade", q_clean))
        title_grades = set(re.findall(r"\b(\d+)\s*grade", title))
        if q_grades and title_grades and not (q_grades & title_grades):
            boost -= 2.50

        # Conflicting part penalty (e.g. user wants part 2, but title/code is part 1)
        q_parts = set(re.findall(r"part\s*(\d+)", q_clean))
        cand_parts = set(re.findall(r"part\s*(\d+)", f"{code} {title}"))
        if q_parts and cand_parts and not (q_parts & cand_parts):
            boost -= 2.50

        return boost

    def rerank(
        self,
        query: str,
        candidates: list[dict[str, Any]],
        top_k: int = 5,
    ) -> list[dict[str, Any]]:
        """
        Reranks candidates using Cross-Encoder neural logits + phrase boosting.
        """
        if not candidates:
            return []

        # Only pass top candidates (up to 15) to the cross-encoder for speed (<15ms)
        eval_candidates = candidates[:15]
        docs = []
        for c in eval_candidates:
            std = c["standard"]
            text = f"{std.get('is_code', '')}: {std.get('title', '')}. {std.get('scope', '')[:300]}"
            docs.append(text)

        # Compute cross-encoder scores
        try:
            scores = list(self.model.rerank(query, docs))
        except Exception as e:
            # Fallback if reranker fails
            return candidates[:top_k]

        scored_results = []
        for i, c in enumerate(eval_candidates):
            raw_logit = float(scores[i])
            ce_score = _sigmoid(raw_logit)
            phrase_score = self._phrase_boost(query, c["standard"])
            base_rrf = c.get("rrf_score", 0.0)

            # Combined score giving strong weight to neural cross-encoder & exact phrase alignment
            final_score = (0.50 * ce_score) + (0.30 * phrase_score) + (0.20 * base_rrf)

            scored_item = dict(c)
            scored_item["rerank_score"] = final_score
            scored_item["ce_score"] = ce_score
            scored_results.append(scored_item)

        scored_results.sort(key=lambda x: x["rerank_score"], reverse=True)

        # Append remaining candidates if any
        if len(candidates) > 15:
            scored_results.extend(candidates[15:])

        return scored_results[:top_k]
