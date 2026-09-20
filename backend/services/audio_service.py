"""
Audio transcription service for voice queries.
Supports Groq Whisper API (free, fast) or Gemini multimodal audio if API keys are set,
with a fallback response.
"""

from __future__ import annotations

import os
import io

async def transcribe_audio_file(content: bytes, filename: str = "audio.webm") -> str:
    """
    Transcribe audio bytes to text string.
    Tries:
      1. Groq Whisper (free API) if GROQ_API_KEY is present
      2. Gemini audio if GEMINI_API_KEY is present
      3. Fallback mock transcription for demo queries
    """
    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key:
        try:
            import httpx
            async with httpx.AsyncClient() as client:
                files = {"file": (filename, content, "audio/webm")}
                data = {"model": "whisper-large-v3"}
                resp = await client.post(
                    "https://api.groq.com/openai/v1/audio/transcriptions",
                    headers={"Authorization": f"Bearer {groq_key}"},
                    files=files,
                    data=data,
                    timeout=15.0
                )
                if resp.status_code == 200:
                    text = resp.json().get("text", "").strip()
                    if text:
                        return text
        except Exception as e:
            print(f"[Audio] Groq transcription failed: {e}")

    gemini_key = os.getenv("GEMINI_API_KEY")
    if gemini_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=gemini_key)
            model = genai.GenerativeModel("gemini-3.6-flash")
            audio_part = {
                "mime_type": "audio/webm",
                "data": content
            }
            resp = model.generate_content([
                "Transcribe this speech accurately into text. Output only the transcript, nothing else.",
                audio_part
            ])
            text = resp.text.strip()
            if text:
                return text
        except Exception as e:
            print(f"[Audio] Gemini transcription failed: {e}")

    # Fallback transcription for demo
    return "What are the mandatory testing and certification requirements for electric kettles under BIS?"
