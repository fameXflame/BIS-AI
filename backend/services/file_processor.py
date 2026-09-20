"""
File processing service — extracts text from uploaded PDFs, DOCX, and plain text files.
"""

from __future__ import annotations

import io
from typing import Optional


async def extract_text_from_file(content: bytes, filename: str) -> str:
    """
    Extract searchable text from an uploaded file.

    Supports:
      - .pdf  (via pypdf)
      - .txt / .csv  (direct decode)
      - .docx (basic XML extraction)

    Returns extracted text string.
    """
    ext = filename.lower().rsplit(".", 1)[-1] if "." in filename else ""

    if ext == "pdf":
        return _extract_pdf(content)
    elif ext in ("txt", "csv", "log"):
        return _extract_text(content)
    elif ext == "docx":
        return _extract_docx(content)
    else:
        return f"Unsupported file type: .{ext}. Supported: PDF, TXT, CSV, DOCX."


def _extract_pdf(content: bytes) -> str:
    """Extract text from PDF bytes using pypdf."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(content))
        pages = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages.append(text.strip())
        if pages:
            return "\n\n".join(pages)
        return "PDF contained no extractable text (possibly scanned/image-based)."
    except Exception as e:
        return f"PDF extraction failed: {str(e)}"


def _extract_text(content: bytes) -> str:
    """Decode plain text file."""
    for encoding in ("utf-8", "latin-1", "cp1252"):
        try:
            return content.decode(encoding)
        except (UnicodeDecodeError, ValueError):
            continue
    return "Could not decode text file."


def _extract_docx(content: bytes) -> str:
    """Basic DOCX text extraction via XML parsing (no python-docx dependency)."""
    try:
        import zipfile
        import xml.etree.ElementTree as ET

        with zipfile.ZipFile(io.BytesIO(content)) as zf:
            if "word/document.xml" not in zf.namelist():
                return "Invalid DOCX file."

            xml_content = zf.read("word/document.xml")
            tree = ET.fromstring(xml_content)

            # Extract all text nodes from the Word XML namespace
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            paragraphs = []
            for para in tree.findall(".//w:p", ns):
                texts = [t.text for t in para.findall(".//w:t", ns) if t.text]
                if texts:
                    paragraphs.append(" ".join(texts))

            if paragraphs:
                return "\n".join(paragraphs)
            return "DOCX contained no extractable text."
    except Exception as e:
        return f"DOCX extraction failed: {str(e)}"
