"""
Gemini-powered services for BIS AI:
  - Query classification & intent analysis (is it BIS related?)
  - Autonomous dynamic reasoning with Gemini 1.5 Flash
  - Fallback domain reasoning & walk-along guidance
  - Confidence scoring
"""

from __future__ import annotations

import os
import json
import re
from typing import Optional
from services.query_classifier import classify_query


def _get_gemini_model():
    """Lazy-load the Gemini generative model. Returns None if no API key."""
    api_key = os.getenv("GEMINI_API_KEY", "")
    if not api_key:
        return None
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        for m_name in ["gemini-1.5-flash", "gemini-2.0-flash", "gemini-3.5-flash-lite", "gemini-flash-latest"]:
            try:
                return genai.GenerativeModel(m_name)
            except Exception:
                continue
        return genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        print(f"[LLM] Gemini init failed: {e}")
        return None


async def analyze_and_magnify_query(query: str) -> dict:
    """
    Intelligently analyze query:
    1. Determine if it is related to BIS / technical standards.
    2. If NOT related: return early with is_bis_related=False and walk-along guide.
    3. If related: extract technical keywords and expand terms.
    """
    model = _get_gemini_model()

    if model is not None:
        prompt = f"""You are the Bureau of Indian Standards (BIS) AI Intelligence Engine.
Evaluate the following user query:
"{query}"

Determine:
1. Is this query related to Bureau of Indian Standards (BIS), Indian Standards (IS codes), manufacturing, factory setups, industrial products, consumer goods, food & beverage standards, electrical/mechanical safety, or quality compliance in India?
2. If YES (or if it mentions products manufactured in India like wine, chairs, cookers, cement, water, electronics, etc.):
   - Identify the technical engineering terms, relevant IS codes (e.g. IS 302, IS 10500, IS 456, IS 2347, IS 7058, IS 9873), and required testing parameters.
3. If NO (only for pure casual greetings, recipes, movies, coding, jokes, sports, or completely unrelated trivia):
   - Set is_bis_related to false.
   - Explain politely why it's out of scope and provide guidance on what BIS covers.

Respond in this exact JSON format only:
{{
  "is_bis_related": true,
  "magnified_query": "expanded technical search string",
  "keywords": ["keyword1", "keyword2", "...up to 8"],
  "out_of_scope_message": ""
}}
or if NOT related:
{{
  "is_bis_related": false,
  "magnified_query": "",
  "keywords": [],
  "out_of_scope_message": "Explanation of why this is not related to BIS and what BIS AI covers."
}}"""
        try:
            response = model.generate_content(prompt)
            text = response.text.strip()
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                data = json.loads(json_match.group())
                return {
                    "is_bis_related": bool(data.get("is_bis_related", True)),
                    "original": query,
                    "magnified": data.get("magnified_query", query),
                    "keywords": data.get("keywords", []),
                    "out_of_scope_message": data.get("out_of_scope_message", "")
                }
        except Exception as e:
            print(f"[LLM] Live query evaluation failed, falling back to local classifier: {e}")

    # Fallback to local rule-based classifier
    classification = classify_query(query)

    if not classification["is_bis_related"]:
        return {
            "is_bis_related": False,
            "original": query,
            "magnified": "",
            "keywords": [],
            "out_of_scope_message": (
                f"Your query \"{query}\" does not appear to be related to the Bureau of Indian Standards (BIS), "
                "product safety specifications, testing norms, or technical certification."
            )
        }

    # BIS related: expand keywords
    return _fallback_magnify(query)


magnify_query = analyze_and_magnify_query


async def synthesize_response(
    query: str,
    standards: list[dict],
    is_bis_related: bool = True
) -> dict:
    """
    Generate an AI summary grounding the search results in clause-level detail
    or providing walk-along guidance when out-of-scope or no standard is matched.

    Returns:
        {
            "summary": str,
            "ai_walkalong": str,
            "has_direct_match": bool
        }
    """
    # Try live Gemini generation first for all queries
    model = _get_gemini_model()
    if model is not None:
        matched_codes = ", ".join(s.get("is_code", "") for s in standards[:3]) if standards else "None in local index"

        prompt = f"""You are BIS AI, a helpful, intelligent assistant for the Bureau of Indian Standards in India.

User query: "{query}"
Relevant standards found: {matched_codes}

Write a SHORT, CONCISE, natural follow-up response (strictly 2 sentences maximum):
1. Directly acknowledge and answer the user's specific query in clear, friendly, human language.
2. If the user is just saying hello, greeting, or asking general questions, greet warmly and ask what product, Indian Standard, or manufacturing requirement they'd like to check today.
3. If the query is technical (e.g. plastic chairs, wine factory, water, kettles), give a direct 2-sentence summary of the compliance context.
4. Do NOT list standard numbers, clause breakdowns, or step-by-step procedures in this text (they will appear in the interactive cards below).
5. Do NOT use markdown headers (###), bullet points, bold asterisks (**), or separator lines (---). Output clean, readable plain sentences only."""

        try:
            response = model.generate_content(prompt)
            summary = response.text.strip()
            summary = re.sub(r'#{1,6}\s*', '', summary)
            summary = summary.replace('**', '').replace('---', '').strip()
            if len(summary) > 10:
                walkalong = "Relevant BIS standards identified through semantic search. Verify applicability and current status before regulatory use." if standards else ""
                return {
                    "summary": summary,
                    "ai_walkalong": walkalong,
                    "has_direct_match": len(standards) > 0
                }
        except Exception as e:
            print(f"[LLM] Live synthesis failed, using fallback: {e}")

    # Fallback if no LLM key or LLM call failed
    if not is_bis_related:
        q_clean = query.strip().lower()
        is_greeting = bool(re.match(r"^(hi+|hello+|hey+|hola|howdy|good\s+(?:morning|afternoon|evening)|namaste|greetings)\b", q_clean))
        
        if is_greeting:
            return {
                "summary": "Hello! I am BIS AI — your intelligent assistant for Bureau of Indian Standards (BIS) regulations, product safety norms, and manufacturing compliance in India.",
                "ai_walkalong": (
                    "**How I can assist you:**\n\n"
                    "• **Find Indian Standards:** Search by product name (e.g. electric kettles, toys, helmets, steel, water) or directly by IS code (e.g. IS 302, IS 10500, IS 2347).\n"
                    "• **Testing & Tolerances:** Discover mandatory test protocols (dielectric, burst pressure, tensile, chemical leaching).\n"
                    "• **Certification Roadmap:** Step-by-step guidance for Scheme-I (ISI Mark) and Scheme-II (CRS) licensing.\n\n"
                    "💡 *Click any of the suggested topics below to explore!*"
                ),
                "has_direct_match": False
            }

        return {
            "summary": "This query is not related to Bureau of Indian Standards (BIS) or product certification.",
            "ai_walkalong": (
                "**What BIS AI specializes in:**\n\n"
                "• **Indian Standards (IS Codes):** Specifications, dimensions, chemical limits, and tolerances for goods sold in India.\n"
                "• **Mandatory Quality Control Orders (QCO):** Products requiring compulsory ISI mark or CRS registration before manufacture/import.\n"
                "• **Laboratory Testing Norms:** Dielectric strength, tensile stress, leaching limits, fire resistance, and microbial tests.\n"
                "• **Certification Pathways:** Step-by-step guidance for Scheme I (ISI Mark), Scheme II (CRS), and NABL audits.\n\n"
                "💡 **Try asking:**\n"
                "• *'Electric kettle manufacturing testing requirements'* \n"
                "• *'Permissible limits for lead and arsenic in drinking water'* \n"
                "• *'Seismic design criteria for multi-storey concrete structures'* \n"
                "• *'Safety requirements for toys or solar photovoltaic modules'*"
            ),
            "has_direct_match": False
        }

    # Case 3: Offline fallback with standards found
    if standards:
        top = standards[0]
        count = len(standards)
        codes = ", ".join(s["is_code"] for s in standards[:3])

        clauses_text = ""
        if top.get("key_clauses"):
            clauses_text = f" Key mandatory clauses include {top['key_clauses'][0]}"
            if len(top["key_clauses"]) > 1:
                clauses_text += f" and {top['key_clauses'][1]}"
            clauses_text += "."

        cert_text = ""
        if top.get("certification_process"):
            cert_text = f" Certification pathway: {top['certification_process']}."

        summary = (
            f"Found {count} applicable Indian Standard{'s' if count > 1 else ''} for your query. "
            f"The primary standard is {top['is_code']} — \"{top['title']}\". "
            f"It governs {top.get('scope', 'the necessary compliance specifications')[:160]}... "
            f"{clauses_text}{cert_text}"
        )

        walkalong = (
            f"📌 **Compliance Advisory for {top['is_code']}:**\n\n"
            f"• **Division:** {top.get('division', 'Technical Division')}\n"
            f"• **Testing:** {top.get('test_requirements', 'Standard laboratory tests required.')}\n"
            f"• **Regulatory Status:** {'Mandatory under Quality Control Order (QCO)' if top.get('mandatory') else 'Voluntary / Industry standard'}\n"
            f"• **Action:** Verify latest amendments on [Official BIS Portal]({top.get('url', 'https://www.services.bis.gov.in')})."
        )

        return {
            "summary": summary,
            "ai_walkalong": walkalong,
            "has_direct_match": True
        }

    # Case 4: BIS-related, but no specific standard card in offline database
    summary = (
        f"Your query regarding \"{query}\" is within the scope of Indian regulatory standards. "
        "However, a specific Indian Standard card was not matched in the local offline database."
    )
    walkalong = (
        "🔍 **How to proceed under BIS guidelines:**\n\n"
        "1. **Search BIS Manakonline:** Access `www.services.bis.gov.in` under 'Standards Review' to view the full 25,000+ catalog.\n"
        "2. **Check DPIIT Quality Control Orders (QCO):** Verify whether your product category has a mandatory ISI marking order notified in the official Gazette of India.\n"
        "3. **Identify Test Scheme:** Most consumer and industrial products fall under **Scheme I (Product Certification / ISI Mark)**, while electronics fall under **Scheme II (Compulsory Registration Scheme - CRS)**.\n"
        "4. **NABL Testing:** Ensure sample evaluation is conducted at a BIS-recognized or NABL-accredited test facility."
    )

    return {
        "summary": summary,
        "ai_walkalong": walkalong,
        "has_direct_match": False
    }


def calculate_confidence(bm25_score: float, max_score: float) -> int:
    """Convert a BM25 score to a 0-100 confidence percentage."""
    if max_score <= 0:
        return 50
    normalized = bm25_score / max_score
    confidence = int(60 + 38 * normalized)
    return min(98, max(30, confidence))


def get_confidence_tier(confidence: int) -> str:
    """Map confidence score to tier label."""
    if confidence >= 80:
        return "high"
    elif confidence >= 60:
        return "moderate"
    return "low"


def _fallback_magnify(query: str) -> dict:
    """Keyword expansion when no LLM is available."""
    q_lower = query.lower()
    keywords = [w for w in re.findall(r'[a-z0-9]+', q_lower) if len(w) > 2]

    expansions = []
    domain_map = {
        "kettle": ["IS 302-2-15", "electrical safety", "heating appliance", "thermostat", "leakage current"],
        "water": ["IS 10500", "IS 14543", "drinking water", "potable", "water quality", "turbidity"],
        "earthquake": ["IS 1893-1", "IS 13920", "seismic design", "ductile detailing", "response spectrum"],
        "fire": ["IS 1641", "IS 2190", "fire safety", "fire resistance", "sprinkler", "NBC Part 4"],
        "steel": ["IS 2062", "IS 800", "structural steel", "weldability", "tensile strength"],
        "food": ["IS 10146", "IS 9845", "food packaging", "migration limit", "food grade"],
        "cement": ["IS 269", "IS 456", "portland cement", "compressive strength"],
        "solar": ["IS 14286", "IS/IEC 61730-1", "photovoltaic", "solar panel", "inverter"],
        "building": ["IS 456", "IS 1893-1", "NBC 2016", "structural design"],
        "electric": ["electrical appliance", "IS 302-1", "safety requirements"],
        "vehicle": ["automotive", "IS 4151", "IS 11852", "crash test", "vehicle safety"],
        "helmet": ["IS 4151", "protective helmet", "impact absorption", "retention system"],
        "textile": ["IS 15748", "IS 1390", "fabric testing", "colorfastness", "protective clothing"],
        "medical": ["IS/ISO 13485", "IS 13422", "medical device", "biocompatibility"],
        "pipe": ["IS 4985", "IS 1239-1", "plumbing", "water supply pipe", "upvc"],
        "chemical": ["IS 14489", "IS 4209", "hazardous substance", "chemical safety"],
        "agriculture": ["IS 540", "IS 6092-1", "fertilizer", "pesticide", "soil testing"],
        "toy": ["IS 9873", "safety of toys", "mechanical physical properties", "flammability"],
        "pressure cooker": ["IS 2347", "domestic pressure cookers", "burst pressure test", "safety valve"],
        "cylinder": ["IS 3196", "welded low carbon steel gas cylinders", "lpg cylinder safety"],
    }

    for key, vals in domain_map.items():
        if key in q_lower:
            expansions.extend(vals)

    all_keywords = list(dict.fromkeys(keywords + expansions))[:10]

    magnified = query
    if expansions:
        magnified = f"{query} — {', '.join(expansions[:4])}"

    return {
        "is_bis_related": True,
        "original": query,
        "magnified": magnified,
        "keywords": all_keywords,
        "out_of_scope_message": ""
    }
