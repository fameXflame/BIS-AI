"""
Applicability & Domain Filtering Engine for BIS Standards.
Enforces the pipeline:
User query -> Product/category identification -> Applicability filtering -> Semantic ranking
Prevents cross-domain contamination (e.g. deodorant query returning pressure cookers or drinking water).
"""

from __future__ import annotations

import re
from typing import Any

# Domain definitions mapping category names to trigger keywords and forbidden standard titles/keywords
DOMAIN_TAXONOMY = {
    "cosmetics_personal_care": {
        "triggers": [
            "deodorant", "deodrant", "antiperspirant", "perfume", "fragrance", "scent",
            "body spray", "lotion", "cream", "cosmetic", "shampoo", "soap",
            "lipstick", "hair oil", "hair dye", "talcum", "body powder", "personal care",
            "shaving", "nail polish", "sunscreen", "aerosol dispenser", "aerosol can"
        ],
        "incompatible_terms": [
            "drinking water", "potable water", "water supply", "pressure cooker", "cooker",
            "structural steel", "steel pipe", "welded steel", "cement", "concrete aggregate",
            "lightweight concrete", "toy", "plaything", "fertilizer", "solar pv",
            "photovoltaic", "inverter", "medical device", "catheter", "stent"
        ]
    },
    "drinking_water": {
        "triggers": [
            "drinking water", "potable water", "tap water", "packaged water", "mineral water",
            "water quality", "tds in water", "water filter", "water purification"
        ],
        "incompatible_terms": [
            "deodorant", "cosmetic", "pressure cooker", "toy", "structural steel",
            "fertilizer", "solar pv", "inverter", "medical device", "cement"
        ]
    },
    "kitchen_appliances": {
        "triggers": [
            "kettle", "cooker", "appliance", "liquid heater", "immersion heater", "microwave",
            "induction", "mixer", "blender", "toaster", "cookware", "cooking pan"
        ],
        "incompatible_terms": [
            "deodorant", "cosmetic", "fertilizer", "structural steel", "steel pipe",
            "welded steel", "cement", "drinking water", "toy", "solar pv", "medical device"
        ]
    },
    "toys_child": {
        "triggers": [
            "toy", "doll", "playground", "child", "plaything", "puzzle toy"
        ],
        "incompatible_terms": [
            "deodorant", "cosmetic", "pressure cooker", "cement", "concrete",
            "structural steel", "fertilizer", "solar pv", "inverter", "wine"
        ]
    },
    "civil_construction": {
        "triggers": [
            "cement", "concrete", "aggregate", "masonry block", "pozzolana", "portland",
            "slag cement", "asbestos sheet", "structural steel", "mortar", "rebar"
        ],
        "incompatible_terms": [
            "deodorant", "cosmetic", "perfume", "pressure cooker", "toy",
            "solar inverter", "medical device", "wine", "beer"
        ]
    },
    "solar_electrical": {
        "triggers": [
            "solar", "photovoltaic", "power converter", "inverter", "grid-tied inverter",
            "solar module", "transformer", "switchgear"
        ],
        "incompatible_terms": [
            "deodorant", "cosmetic", "pressure cooker", "toy",
            "cement", "concrete", "fertilizer", "wine"
        ]
    },
    "food_beverages": {
        "triggers": [
            "wine", "winery", "beer", "brewery", "alcoholic beverage", "grape fermentation",
            "biscuit", "milk", "honey", "spice", "edible oil"
        ],
        "incompatible_terms": [
            "deodorant", "cosmetic", "pressure cooker", "structural steel", "cement",
            "solar inverter", "toy", "steel pipe"
        ]
    },
    "medical_devices": {
        "triggers": [
            "medical device", "syringe", "glove", "catheter", "stent", "surgical",
            "implant", "cannula", "clinical thermometer"
        ],
        "incompatible_terms": [
            "deodorant", "pressure cooker", "toy", "cement", "concrete",
            "solar inverter", "wine"
        ]
    }
}


def identify_query_domain(query: str) -> str | None:
    """
    Identifies the primary product domain of the user query.
    Returns domain key if a specific domain is detected, or None for open/unrestricted queries.
    """
    q_lower = query.lower()
    for domain, data in DOMAIN_TAXONOMY.items():
        for trigger in data["triggers"]:
            # Check for word boundary match with optional plural 's'
            if re.search(r"\b" + re.escape(trigger) + r"s?\b", q_lower):
                return domain
    return None


def filter_and_rank_by_applicability(
    query: str,
    candidates: list[dict[str, Any]],
    domain: str | None = None,
) -> list[dict[str, Any]]:
    """
    Filters out inapplicable standards that conflict with the query product category.
    Applies domain relevance scoring.
    """
    if not domain:
        domain = identify_query_domain(query)

    if not domain or domain not in DOMAIN_TAXONOMY:
        # No specific domain detected — return candidates as-is
        return candidates

    domain_data = DOMAIN_TAXONOMY[domain]
    incompatible = domain_data["incompatible_terms"]
    triggers = domain_data["triggers"]

    applicable_candidates = []

    for c in candidates:
        std = c["standard"]
        title_lower = std.get("title", "").lower()
        scope_lower = std.get("scope", "").lower()
        code_lower = std.get("is_code", "").lower()
        content = f"{code_lower} {title_lower} {scope_lower}"

        # Check if candidate contains explicitly incompatible terms in title
        is_incompatible = False
        for term in incompatible:
            if re.search(r"\b" + re.escape(term) + r"s?\b", title_lower):
                is_incompatible = True
                break

        if is_incompatible:
            continue

        # Check for positive domain alignment (matches trigger words with optional plural)
        has_direct_product_match = any(
            re.search(r"\b" + re.escape(t) + r"s?\b", content) for t in triggers
        )

        c_copy = dict(c)
        if has_direct_product_match:
            c_copy["domain_aligned"] = True
            c_copy["domain_boost"] = 1.0
        else:
            c_copy["domain_aligned"] = False
            c_copy["domain_boost"] = 0.3

        applicable_candidates.append(c_copy)

    # If domain-aligned candidates exist, strictly return ONLY domain-aligned standards
    aligned = [c for c in applicable_candidates if c.get("domain_aligned")]
    if aligned:
        return aligned

    return applicable_candidates
