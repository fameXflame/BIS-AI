"""
BIS AI — FastAPI Backend
========================
Production API server for the Bureau of Indian Standards AI search engine.

Endpoints:
  GET  /api/health          — Health check
  POST /api/search          — Full hybrid search pipeline
  POST /api/upload-file     — Extract text from uploaded docs and search
  GET  /api/standard/{code} — Lookup a single standard by IS code
  GET  /api/stats           — Database statistics
"""

from __future__ import annotations

import os
import sys
import time

from typing import Optional, List, Dict, Any

from fastapi import FastAPI, UploadFile, File, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Add backend dir to path for imports
sys.path.insert(0, os.path.dirname(__file__))

load_dotenv()

from data_engine import get_all_standards, get_standard_by_code
from search_engine.hybrid_search import HybridSearchEngine
from services.file_processor import extract_text_from_file
from services.audio_service import transcribe_audio_file
from services.pdf_generator import generate_dossier_pdf
from services.comparison_service import compare_standards, answer_clause_question

# ─── App Setup ───────────────────────────────────────────────────────

app = FastAPI(
    title="BIS AI API",
    version="2.0.0",
    description="AI-powered Bureau of Indian Standards search engine with hybrid BM25 + LLM pipeline",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.getenv("FRONTEND_URL", "http://localhost:3000"),
        "http://127.0.0.1:3000",
        "http://localhost:3000",
        "*",  # Allow all origins for demo
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Initialize Search Engine ────────────────────────────────────────

_standards = get_all_standards()
_search_engine = HybridSearchEngine(_standards)
print(f"[BIS AI] Loaded {len(_standards)} standards into search engine.")
print(f"[BIS AI] Gemini API key: {'configured [OK]' if os.getenv('GEMINI_API_KEY') else 'not set (using fallback mode)'}")


# ─── Request / Response Models ───────────────────────────────────────

class SearchRequest(BaseModel):
    query: str
    top_k: int = 8
    division: Optional[str] = None


class SearchResponse(BaseModel):
    query_original: str
    query_magnified: str
    summary: str
    ai_walkalong: str = ""
    is_bis_related: bool = True
    standards: list[dict]
    total_results: int
    latency_ms: int


class ExportDossierRequest(BaseModel):
    query: str
    search_results: Dict[str, Any]


class CompareRequest(BaseModel):
    standard_a: str
    standard_b: str


class ClauseQARequest(BaseModel):
    is_code: str
    question: str


# ─── Endpoints ───────────────────────────────────────────────────────

@app.get("/api/health")
async def health_check():
    """Health check with system info."""
    return {
        "status": "ok",
        "service": "BIS AI",
        "version": "2.0.0",
        "standards_loaded": len(_standards),
        "gemini_configured": bool(os.getenv("GEMINI_API_KEY")),
    }


@app.get("/api/divisions")
async def get_divisions():
    """Returns list of distinct BIS departments and standards count."""
    counts: dict[str, int] = {}
    for s in _standards:
        d = s.get("division", "Other")
        counts[d] = counts.get(d, 0) + 1
    return [{"division": d, "count": count} for d, count in sorted(counts.items())]


@app.post("/api/search", response_model=SearchResponse)
async def search_standards(request: SearchRequest):
    """
    Full hybrid search pipeline:
    1. Query classification (detects if related to BIS or out-of-scope)
    2. Query magnification (expand with BIS technical vocabulary)
    3. BM25 lexical search across all standards (with optional department filter)
    4. Reciprocal Rank Fusion scoring
    5. LLM synthesis with clause-level grounding and walk-along guidance
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    start = time.time()
    results = await _search_engine.search(request.query, top_k=request.top_k, division=request.division)
    latency = int((time.time() - start) * 1000)

    return SearchResponse(
        query_original=results["query_original"],
        query_magnified=results["query_magnified"],
        summary=results["summary"],
        ai_walkalong=results.get("ai_walkalong", ""),
        is_bis_related=results.get("is_bis_related", True),
        standards=results["standards"],
        total_results=results["total_results"],
        latency_ms=latency,
    )


@app.post("/api/upload-file")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a document (PDF, DOCX, TXT) — extract text and search for
    applicable BIS standards.
    """
    content = await file.read()
    if len(content) == 0:
        raise HTTPException(status_code=400, detail="Empty file")

    if len(content) > 10 * 1024 * 1024:  # 10 MB limit
        raise HTTPException(status_code=413, detail="File too large (max 10 MB)")

    # Extract text
    extracted = await extract_text_from_file(content, file.filename or "unknown.txt")

    if not extracted or len(extracted) < 10:
        return {
            "filename": file.filename,
            "extracted_text": extracted,
            "search_results": None,
            "message": "Could not extract meaningful text from file.",
        }

    # Use extracted text as a search query (take first 500 chars)
    search_query = extracted[:500].strip()
    start = time.time()
    results = await _search_engine.search(search_query, top_k=6)
    latency = int((time.time() - start) * 1000)

    return {
        "filename": file.filename,
        "extracted_text": extracted[:1000],  # Return first 1000 chars
        "search_results": {
            "query_original": f"Document analysis: {file.filename}",
            "query_magnified": results["query_magnified"],
            "summary": results["summary"],
            "standards": results["standards"],
            "total_results": results["total_results"],
            "latency_ms": latency,
        },
    }


@app.post("/api/transcribe-audio")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Transcribe uploaded audio (WebM, WAV, MP3) and return both transcript
    and search results.
    """
    content = await file.read()
    if len(content) == 0:
        raise HTTPException(status_code=400, detail="Empty audio recording")

    transcription = await transcribe_audio_file(content, file.filename or "recording.webm")
    start = time.time()
    results = await _search_engine.search(transcription, top_k=6)
    latency = int((time.time() - start) * 1000)

    return {
        "transcription": transcription,
        "search_results": {
            "query_original": transcription,
            "query_magnified": results["query_magnified"],
            "summary": results["summary"],
            "standards": results["standards"],
            "total_results": results["total_results"],
            "latency_ms": latency,
        },
    }


@app.get("/api/standard/{is_code}")
async def get_standard(is_code: str):
    """Look up a single standard by its IS code."""
    std = get_standard_by_code(is_code)
    if not std:
        raise HTTPException(status_code=404, detail=f"Standard '{is_code}' not found")
    return {"data": std}


@app.post("/api/export-pdf")
async def export_pdf(payload: ExportDossierRequest):
    """
    Generates a publication-grade BIS Standards Compliance Dossier PDF.
    """
    try:
        pdf_bytes = generate_dossier_pdf(payload.query, payload.search_results)
        filename = f"BIS_Compliance_Dossier_{int(time.time())}.pdf"
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        print(f"[PDF Export Error] {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate PDF dossier: {str(e)}")


@app.post("/api/compare")
async def compare_two_standards(payload: CompareRequest):
    """
    RAG Comparative Analysis between two Indian Standards.
    Returns technical parameter breakdown, scope differences, and legal requirements.
    """
    result = compare_standards(payload.standard_a, payload.standard_b)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.post("/api/clause-qa")
async def ask_clause_qa(payload: ClauseQARequest):
    """
    Interactive Clause Q&A Assistant:
    Answers specific technical limits (water absorption, tolerances, test clauses)
    grounded directly on the official standard specification.
    """
    result = answer_clause_question(payload.is_code, payload.question)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.get("/api/stats")
async def get_stats():
    """Database statistics."""
    divisions: dict[str, int] = {}
    mandatory_count = 0
    for s in _standards:
        div = s.get("division", "Unknown")
        divisions[div] = divisions.get(div, 0) + 1
        if s.get("mandatory"):
            mandatory_count += 1

    return {
        "total_standards": len(_standards),
        "mandatory_standards": mandatory_count,
        "divisions": divisions,
        "search_engine": "BM25 + RRF Hybrid",
        "llm": "Gemini 1.5 Flash" if os.getenv("GEMINI_API_KEY") else "Fallback (template-based)",
    }


# ─── Entry Point ─────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("BACKEND_PORT", "8000"))
    print(f"[BIS AI] Starting server on port {port}...")
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
