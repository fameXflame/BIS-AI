from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="BIS AI API",
    version="1.0.0",
    description="AI-powered Bureau of Indian Standards search engine",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.getenv("FRONTEND_URL", "http://localhost:3000"),
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SearchRequest(BaseModel):
    query: str
    filters: dict | None = None


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "BIS AI", "version": "1.0.0"}


@app.post("/api/search")
async def search_standards(request: SearchRequest):
    return {
        "summary": f"Search endpoint received query: {request.query}",
        "query_magnified": "",
        "standards": [],
    }


@app.post("/api/upload-file")
async def upload_file(file: UploadFile = File(...)):
    return {
        "message": f"File received: {file.filename}",
        "extracted_text": "",
    }


@app.post("/api/transcribe-audio")
async def transcribe_audio(file: UploadFile = File(...)):
    return {
        "message": "Audio transcription endpoint",
        "transcription": "",
    }


@app.get("/api/standard/{is_code}")
async def get_standard(is_code: str):
    return {
        "message": f"Standard detail for {is_code}",
        "data": None,
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("BACKEND_PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
