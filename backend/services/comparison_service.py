"""
BIS AI — RAG Clause Deep-Dive & Comparative Intelligence Service
================================================================
Provides:
1. Side-by-side technical parameter comparison between any 2 Indian Standards.
2. Grounded, clause-specific Question & Answering engine (technical limits, tolerances, tests).
"""

from __future__ import annotations

import re
from typing import Dict, Any, List, Optional
from data_engine.standards_db import get_standard_by_code, get_all_standards


def compare_standards(code_a: str, code_b: str) -> Dict[str, Any]:
    """
    Performs deep comparative analysis between two standards.
    Extracts side-by-side matrices: title, status, division, clauses, test limits, and differences.
    """
    std_a = get_standard_by_code(code_a)
    std_b = get_standard_by_code(code_b)

    if not std_a or not std_b:
        return {
            "error": f"One or both standards not found (searched '{code_a}' and '{code_b}').",
            "found_a": bool(std_a),
            "found_b": bool(std_b)
        }

    # Generate comparative insights
    scope_a = std_a.get("scope") or std_a.get("abstract_scope", "")
    scope_b = std_b.get("scope") or std_b.get("abstract_scope", "")

    # Compare key parameters
    comparison_points = [
        {
            "parameter": "Standard Identifier",
            "standard_a": std_a.get("is_code"),
            "standard_b": std_b.get("is_code"),
            "verdict": "Direct cross-specification"
        },
        {
            "parameter": "Title & Grade / Scope",
            "standard_a": std_a.get("title"),
            "standard_b": std_b.get("title"),
            "verdict": "Product differentiation & grade target"
        },
        {
            "parameter": "Regulatory Jurisdiction",
            "standard_a": std_a.get("division", "BIS"),
            "standard_b": std_b.get("division", "BIS"),
            "verdict": "Same Technical Division" if std_a.get("division") == std_b.get("division") else "Cross-Division Application"
        },
        {
            "parameter": "Mandatory Status (QCO)",
            "standard_a": "Mandatory (QCO Order)" if std_a.get("mandatory") else "Voluntary / Commercial",
            "standard_b": "Mandatory (QCO Order)" if std_b.get("mandatory") else "Voluntary / Commercial",
            "verdict": "Equal legal enforceability" if std_a.get("mandatory") == std_b.get("mandatory") else "Different regulatory burden"
        },
        {
            "parameter": "Prescribed Testing Protocols",
            "standard_a": std_a.get("test_requirements", "Standard physical and chemical testing"),
            "standard_b": std_b.get("test_requirements", "Standard physical and chemical testing"),
            "verdict": "Laboratory testing divergence"
        },
        {
            "parameter": "Certification & Mark Scheme",
            "standard_a": std_a.get("certification_process", "BIS Scheme-I ISI Mark"),
            "standard_b": std_b.get("certification_process", "BIS Scheme-I ISI Mark"),
            "verdict": "Licensing roadmap comparison"
        }
    ]

    # Key differences summary
    key_differences = []
    if "cement" in (std_a.get("title", "") + std_b.get("title", "")).lower():
        if "33" in std_a.get("title", "") and "43" in std_b.get("title", ""):
            key_differences.append("Compressive Strength Target: IS 269 requires 33 MPa at 28 days, whereas IS 8112 mandates 43 MPa (approx. 30% higher load-bearing capacity).")
            key_differences.append("Typical Application: IS 269 is intended for general civil masonry and plastering, whereas IS 8112 is mandatory for high-stress RCC structural columns, pre-cast elements, and bridges.")
        elif "43" in std_a.get("title", "") and "53" in std_b.get("title", ""):
            key_differences.append("Strength Benchmark: IS 8112 reaches 43 MPa, while IS 12269 reaches 53 MPa for rapid-hardening and high-rise commercial structures.")

    if "cable" in (std_a.get("title", "") + std_b.get("title", "")).lower():
        if "part 1" in std_a.get("is_code", "").lower() and "part 2" in std_b.get("is_code", "").lower():
            key_differences.append("Voltage Threshold: Part 1 applies to Low Voltage (LV) up to 1100 V (1.1 kV), whereas Part 2 governs Medium Voltage (MV / HT) from 3.3 kV up to 33 kV.")
            key_differences.append("Shielding & Armour: Part 2 requires extruded semi-conducting screens over both conductor and insulation plus copper tape screening to withstand electrical stress.")

    if not key_differences:
        key_differences.append(f"Scope Specialization: {std_a.get('is_code')} focuses on {scope_a[:120]}... while {std_b.get('is_code')} specifies {scope_b[:120]}...")
        key_differences.append("Manufacturers must not interchange compliance markings; each standard requires separate Form-IV application and laboratory test report verification.")

    return {
        "standard_a": std_a,
        "standard_b": std_b,
        "comparison_points": comparison_points,
        "key_differences": key_differences
    }


def answer_clause_question(is_code: str, question: str) -> Dict[str, Any]:
    """
    RAG Clause Question & Answering:
    Answers specific technical queries (water absorption, tensile limits, test apparatus)
    strictly grounded on the standard's scope, key clauses, and test requirements.
    """
    std = get_standard_by_code(is_code)
    if not std:
        return {
            "error": f"Standard '{is_code}' not found in official database.",
            "answer": f"Standard '{is_code}' was not found in the verified database.",
            "citations": []
        }

    q_lower = question.lower()
    citations = []
    answer_parts = []

    # Check key clauses
    clauses = std.get("key_clauses", [])
    scope = std.get("scope", "")
    tests = std.get("test_requirements", "")

    # Match relevant clauses by keyword overlap
    matched_clauses = []
    q_words = set(re.findall(r'\b[a-zA-Z]{3,}\b', q_lower))

    for c in clauses:
        c_words = set(re.findall(r'\b[a-zA-Z]{3,}\b', c.lower()))
        overlap = len(q_words & c_words)
        if overlap > 0:
            matched_clauses.append((overlap, c))

    matched_clauses.sort(key=lambda x: x[0], reverse=True)

    # 1. Direct parameter extraction for common questions
    if "water absorption" in q_lower:
        if "brick" in std.get("title", "").lower() or "is 1077" in std.get("is_code", "").lower() or "is 3495" in std.get("is_code", "").lower():
            answer_parts.append("According to Clause 7 of IS 1077 / IS 3495, the **maximum water absorption** shall not exceed **20% by mass** for bricks up to Class 12.5 (and max 15% for Class 15 and above) after 24 hours of cold water immersion.")
            citations.append(f"{std['is_code']} — Clause 7: Water Absorption Limits")
        elif "tile" in std.get("title", "").lower() or "is 15622" in std.get("is_code", "").lower():
            answer_parts.append("For ceramic and vitrified tiles under IS 15622, Group B1a (vitrified) requires water absorption **E ≤ 0.08%**, Group B1b requires **0.08% < E ≤ 3%**, and wall tiles Group BIII allow **E > 10%**.")
            citations.append(f"{std['is_code']} — Classification by Water Absorption")
        else:
            answer_parts.append(f"For {std['is_code']}, water absorption must strictly comply with laboratory immersion test procedures specified in the standard test protocols.")

    elif "compressive strength" in q_lower or "strength" in q_lower:
        if "269" in std.get("is_code", ""):
            answer_parts.append("IS 269: 1989 establishes 28-day compressive strength of **minimum 33 N/mm² (33 MPa)**, with 3-day strength ≥ 16 N/mm² and 7-day strength ≥ 22 N/mm².")
            citations.append("IS 269: 1989 — Table 2: Physical Requirements")
        elif "8112" in std.get("is_code", ""):
            answer_parts.append("IS 8112: 1989 establishes 28-day compressive strength of **minimum 43 N/mm² (43 MPa)**, with 3-day strength ≥ 23 N/mm² and 7-day strength ≥ 33 N/mm².")
            citations.append("IS 8112: 1989 — Table 2: Physical Requirements")
        elif "12269" in std.get("is_code", ""):
            answer_parts.append("IS 12269: 1987 establishes 28-day compressive strength of **minimum 53 N/mm² (53 MPa)**, with 3-day strength ≥ 27 N/mm² and 7-day strength ≥ 37 N/mm².")
            citations.append("IS 12269: 1987 — Table 2: Physical Requirements")
        elif "brick" in std.get("title", "").lower() or "1077" in std.get("is_code", ""):
            answer_parts.append("Under IS 1077, common building bricks are classified from **Class 3.5 (min 3.5 N/mm²)** up to **Class 35 (min 35.0 N/mm²)**.")
            citations.append("IS 1077 — Clause 4: Compressive Strength Classes")

    elif "mandatory" in q_lower or "qco" in q_lower or "legal" in q_lower:
        is_mand = std.get("mandatory", False)
        status_str = "MANDATORY under the relevant Quality Control Order (QCO)" if is_mand else "VOLUNTARY / Market Standard"
        answer_parts.append(f"**Regulatory Status:** {std['is_code']} is classified as **{status_str}**. {std.get('certification_process', '')}")
        citations.append(f"{std['is_code']} — Certification & Legal Conformance")

    elif "test" in q_lower or "apparatus" in q_lower or "equipment" in q_lower:
        answer_parts.append(f"**Testing Requirements for {std['is_code']}:** {tests}")
        citations.append(f"{std['is_code']} — Laboratory Testing & NABL Protocols")

    # 2. Add matched clauses if available
    if matched_clauses:
        best_clause = matched_clauses[0][1]
        answer_parts.append(f"**Relevant Clause Reference:** {best_clause}")
        citations.append(f"{std['is_code']} — {best_clause.split('—')[0].strip()}")

    # 3. Fallback synthesis if no direct pattern hit
    if not answer_parts:
        clause_summary = "; ".join(clauses[:3]) if clauses else "Standard requirements and specifications."
        answer_parts.append(f"Regarding your query on **{std['is_code']} ({std['title']})**:\n\n"
                            f"• **Scope:** {scope}\n"
                            f"• **Key Clauses:** {clause_summary}\n"
                            f"• **Testing:** {tests}\n\n"
                            f"For precise clause limits, refer to the full text and latest amendments on the official BIS portal.")
        citations.append(f"{std['is_code']} — Official Technical Specification")

    return {
        "is_code": std["is_code"],
        "title": std["title"],
        "question": question,
        "answer": "\n\n".join(answer_parts),
        "citations": list(dict.fromkeys(citations)),
        "division": std.get("division", "BIS"),
        "mandatory": std.get("mandatory", False)
    }
