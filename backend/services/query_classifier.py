"""
Query classifier and intent analyzer for BIS AI.
Determines whether a user query is related to the Bureau of Indian Standards,
engineering specifications, product manufacturing, testing, or regulatory compliance.
"""

from __future__ import annotations

import re
from typing import TypedDict


class QueryClassification(TypedDict):
    is_bis_related: bool
    confidence: float
    category: str
    detected_entities: list[str]
    reason: str


# Positive technical & compliance keywords indicative of BIS domain
_BIS_INDICATORS = {
    # BIS specific
    "bis", "is", "isi", "isi mark", "manakonline", "crs", "qco", "quality control order",
    "bureau of indian standards", "gazette", "hallmark", "hallmarking",
    # Compliance & Regulatory
    "standard", "standards", "compliance", "compliant", "certification", "certificate",
    "certified", "license", "licensing", "conformity", "regulation", "regulatory",
    "mandatory", "voluntary", "specification", "specifications", "norm", "norms",
    "nabl", "nabl accredited", "lab test", "audit", "inspection",
    # Engineering & Quality
    "test", "testing", "tests", "tolerance", "threshold", "limit", "limits",
    "permissible", "allowable", "quality", "parameter", "parameters",
    "tensile", "compressive", "dielectric", "insulation", "leakage", "flammability",
    "durability", "endurance", "corrosion", "ingress", "ipx", "ip65", "ip67",
    # Manufacturing & Construction
    "manufacture", "manufacturing", "manufacturer", "fabricate", "fabrication",
    "produce", "production", "raw material", "grade", "alloy", "formulation",
    "design", "structural", "construction", "concrete", "steel", "cement",
    "safety", "hazard", "protection", "protective", "factory", "plant", "unit", "industry", "industrial",
    # Common regulated products in India
    "kettle", "heater", "iron", "appliance", "appliances", "wire", "cable", "cables",
    "water", "drinking water", "mineral water", "bottled water", "water bottle",
    "pipe", "pipes", "plumbing", "pvc", "upvc", "hdpe",
    "earthquake", "seismic", "building", "buildings", "fire", "extinguisher", "sprinkler",
    "helmet", "helmets", "pressure cooker", "cooker", "gas stove", "cylinder", "lpg",
    "toy", "toys", "battery", "batteries", "lithium", "inverter", "solar", "photovoltaic",
    "food", "packaging", "packaged", "container", "plastic", "milk", "oil",
    "wine", "winery", "wines", "alcoholic", "beverage", "beverages", "distillery", "brewery", "liquor",
    "chair", "chairs", "furniture", "table", "seating",
    "footwear", "shoes", "boots", "leather", "rubber",
    "soap", "detergent", "sanitizer", "disinfectant", "cosmetic", "cosmetics",
    "timber", "plywood", "wood", "laminate",
    "led", "lamp", "bulb", "switch", "socket", "plug", "fuse", "mcb", "transformer", "motor", "pump",
    "medical", "mask", "gloves", "syringe", "automotive", "vehicle", "tyre", "tyres",
    "glass", "door", "window", "textile", "fabric", "cloth", "garment",
    "fertilizer", "pesticide", "chemical", "paint", "cement", "concrete",
    "cybersecurity", "iso", "iec", "gold", "silver", "jewellery", "jewelry"
}

# Negative non-technical/conversational indicators
_OUT_OF_SCOPE_PATTERNS = [
    r"\b(recipe|cook|bake|ingredients|dish|biryani|pizza|burger|curry)\b",
    r"\b(joke|funny|laugh|story|poem|song|lyrics|movie|actor|cricket|football|ipl)\b",
    r"\b(capital of|who is|president of|prime minister of|weather in|temperature today)\b",
    r"\b(write a code|python script|javascript loop|debug this code|css animation)\b",
    r"\b(love|dating|girlfriend|boyfriend|astrology|horoscope|relationship)\b",
    r"\b(math homework|solve this equation|derivative of|integral of)\b",
]

# IS code regex (e.g., IS 302, IS 10500, IS 1893-1, IS/ISO 9001)
_IS_CODE_REGEX = re.compile(r"\b(IS|is)\s*(?:/?[A-Z]+)*\s*\d+(?:[-/]\d+)*\b", re.IGNORECASE)


def classify_query(query: str) -> QueryClassification:
    """
    Classify whether a query is related to BIS / technical standards or out-of-scope.
    """
    clean_query = query.strip()
    q_lower = clean_query.lower()

    # Rule 1: Empty or extremely short query
    if len(clean_query) < 2:
        return {
            "is_bis_related": False,
            "confidence": 0.99,
            "category": "empty_or_too_short",
            "detected_entities": [],
            "reason": "Query is too short or empty to determine technical intent."
        }

    # Rule 1.5: Conversational greetings (e.g. hi, hii, hello, hey)
    if re.match(r"^(hi+|hello+|hey+|hola|howdy|good\s+(?:morning|afternoon|evening)|namaste|greetings)\b", q_lower):
        return {
            "is_bis_related": False,
            "confidence": 0.99,
            "category": "greeting",
            "detected_entities": [],
            "reason": "Greeting message detected."
        }

    # Rule 2: Explicit IS Code reference (e.g. IS 302, IS 10500)
    is_code_match = _IS_CODE_REGEX.search(clean_query)
    if is_code_match:
        return {
            "is_bis_related": True,
            "confidence": 0.99,
            "category": "is_code_lookup",
            "detected_entities": [is_code_match.group(0)],
            "reason": f"Explicit Indian Standard code detected: {is_code_match.group(0)}."
        }

    # Rule 3: Check for obvious out-of-scope conversational patterns
    for pattern in _OUT_OF_SCOPE_PATTERNS:
        if re.search(pattern, q_lower):
            # Double check if user asked something like "food packaging recipe" (still might be food)
            # but if general cooking/celebrity/jokes, classify as out of scope
            matched_bis_words = [w for w in _BIS_INDICATORS if re.search(rf"\b{re.escape(w)}\b", q_lower)]
            if not any(w in matched_bis_words for w in ["standard", "bis", "isi", "certification", "compliance", "test"]):
                return {
                    "is_bis_related": False,
                    "confidence": 0.95,
                    "category": "out_of_scope",
                    "detected_entities": [],
                    "reason": "Query belongs to general non-technical or casual topics."
                }

    # Rule 4: Match against domain indicator lexicon
    words = re.findall(r"[a-z0-9]+", q_lower)
    matched_indicators: list[str] = []

    # Check multi-word indicators first
    for ind in _BIS_INDICATORS:
        if " " in ind and ind in q_lower:
            matched_indicators.append(ind)

    # Check single-word indicators
    for w in words:
        if w in _BIS_INDICATORS and w not in matched_indicators:
            matched_indicators.append(w)

    if len(matched_indicators) >= 1:
        return {
            "is_bis_related": True,
            "confidence": min(0.95, 0.5 + 0.15 * len(matched_indicators)),
            "category": "technical_or_product_compliance",
            "detected_entities": matched_indicators,
            "reason": f"Detected technical/compliance indicators: {', '.join(matched_indicators[:4])}."
        }

    # Rule 5: Fallback if no indicators matched
    return {
        "is_bis_related": False,
        "confidence": 0.85,
        "category": "unrelated",
        "detected_entities": [],
        "reason": "No Indian Standards, product safety, testing, or manufacturing indicators found."
    }
