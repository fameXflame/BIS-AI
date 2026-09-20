"""
BM25 Lexical Search Engine for BIS Standards.
Works fully offline with zero external dependencies beyond rank-bm25.
"""

from __future__ import annotations

import re
from rank_bm25 import BM25Okapi


# Corpus stopwords: Words that appear in virtually every BIS standard document
_CORPUS_STOPWORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "shall",
    "should", "may", "might", "can", "could", "i", "me", "my", "we", "our",
    "you", "your", "he", "she", "it", "they", "them", "this", "that",
    "which", "who", "whom", "what", "where", "when", "how", "why",
    "in", "on", "at", "to", "for", "of", "with", "by", "from", "as",
    "into", "through", "about", "between", "after", "before", "during",
    "and", "or", "but", "not", "if", "so", "than", "too", "very",
    "want", "need", "like", "know", "get", "make", "find", "tell",
    # Universal BIS document terms (do not distinguish standards)
    "india", "indian", "standard", "standards", "bis", "bureau", "code", "codes",
    "specification", "specifications", "part", "section", "guidelines", "general",
    "requirements", "requirement", "prescribes", "covers", "deals"
}

# Domain-specific synonym expansions (targeted only)
_DOMAIN_SYNONYMS: dict[str, list[str]] = {
    "kettle": ["electric kettle", "liquid heater", "immersion"],
    "water": ["drinking water", "potable", "mineral water"],
    "earthquake": ["seismic", "ductile", "structural", "vibration"],
    "fire": ["flammability", "fire extinguisher", "fire resistance", "sprinkler"],
    "steel": ["structural steel", "tensile strength", "yield stress", "rebar"],
    "food": ["food packaging", "migration limit", "food contact"],
    "cement": ["portland cement", "concrete mix", "compressive strength"],
    "car": ["automotive", "vehicle", "crash test"],
    "solar": ["photovoltaic", "pv module", "solar cell", "inverter"],
    "plastic": ["polymer", "polyethylene", "polypropylene", "pvc"],
    "pipe": ["piping", "plumbing", "upvc", "hdpe", "ductile iron"],
    "textile": ["fabric", "garment", "flame retardant", "yarn"],
    "medical": ["biocompatibility", "surgical", "medical device"],
    "chemical": ["hazardous", "toxicity", "chemical safety"],
    "toy": ["toys", "toy safety", "mechanical hazards"],
    "cooker": ["pressure cooker", "burst test", "safety valve"],
    "cylinder": ["gas cylinder", "lpg", "burst pressure"],
}


def _tokenize(text: str) -> list[str]:
    """Lowercase, strip punctuation, remove corpus stopwords."""
    text = text.lower()
    tokens = re.findall(r"[a-z0-9]+(?:[\-\.][a-z0-9]+)*", text)
    tokens = [t for t in tokens if t not in _CORPUS_STOPWORDS and len(t) > 1]
    return tokens


def _standard_to_text(std: dict) -> str:
    """Flatten a standard dict into a single searchable text blob."""
    parts = [
        std.get("is_code", ""),
        std.get("title", ""),
        std.get("scope", ""),
        std.get("division", ""),
        std.get("test_requirements", ""),
        std.get("certification_process", ""),
        " ".join(std.get("key_clauses", [])),
        " ".join(std.get("keywords", [])),
    ]
    return " ".join(parts)


class BM25SearchEngine:
    """BM25-based lexical search over BIS standards."""

    def __init__(self, standards: list[dict]):
        self._standards = standards
        self._corpus_tokens: list[list[str]] = []
        self._bm25: BM25Okapi | None = None
        self._build_index()

    def _build_index(self) -> None:
        """Tokenize all standards and build the BM25 index."""
        self._corpus_tokens = [
            _tokenize(_standard_to_text(std)) for std in self._standards
        ]
        if self._corpus_tokens:
            self._bm25 = BM25Okapi(self._corpus_tokens)

    def search(self, query: str, top_k: int = 8, division: str | None = None) -> list[dict]:
        """
        Search standards by query with strict content validation and optional division filter.
        Prevents returning irrelevant standards if no core query tokens match.
        """
        if not self._bm25 or not self._standards:
            return []

        query_tokens = _tokenize(query)
        if not query_tokens:
            return []

        # Add domain synonyms to search tokens
        expanded_tokens = list(query_tokens)
        for t in query_tokens:
            if t in _DOMAIN_SYNONYMS:
                for syn in _DOMAIN_SYNONYMS[t]:
                    expanded_tokens.extend(_tokenize(syn))

        scores = self._bm25.get_scores(expanded_tokens)

        # Pair scores with indices, sort descending
        scored = [(i, float(s)) for i, s in enumerate(scores) if s > 0]
        scored.sort(key=lambda x: x[1], reverse=True)

        results = []
        core_query_set = set(query_tokens)

        # Identify substantive content tokens (skip generic verbs, adverbs, and compliance words)
        generic_tokens = {
            "test", "tests", "testing", "safety", "standard", "standards", "limits", "limit",
            "requirements", "requirement", "specification", "guidelines", "compliance", "mandatory",
            "india", "indian", "burst", "purity", "acceptable", "permissible", "allowable",
            "factory", "plant", "unit", "setup", "start", "open", "business", "needed", "wanna",
            "want", "looking", "produce", "production", "manufacture", "manufacturing"
        }
        subject_tokens = [t for t in query_tokens if t not in generic_tokens]

        for idx, score in scored:
            std = self._standards[idx]

            # If division filter is active, skip non-matching divisions
            if division and division.strip().lower() not in ["all", "all divisions", ""]:
                std_div = (std.get("division") or "").strip().lower()
                if division.strip().lower() not in std_div:
                    continue

            std_text_lower = _standard_to_text(std).lower()

            # If the user specified distinctive subject tokens (e.g., 'gold', 'cooker', 'kettle'),
            # at least one of those MUST appear in the standard text
            if subject_tokens:
                matching_subject = [t for t in subject_tokens if t in std_text_lower]
                if not matching_subject:
                    continue  # Reject spurious match

            results.append({
                "standard": std.copy(),
                "bm25_score": score,
            })

            if len(results) >= top_k:
                break

        return results
