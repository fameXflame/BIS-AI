# BIS AI

> AI-powered Bureau of Indian Standards search engine with semantic understanding

![Next.js](https://img.shields.io/badge/Next.js-14-black?logo=next.js)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi)
![TypeScript](https://img.shields.io/badge/TypeScript-5.7-3178C6?logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-38B2AC?logo=tailwindcss)

---

## 🚀 What is BIS AI?

BIS AI is an intelligent search platform that helps manufacturers, engineers, and compliance officers quickly find relevant **Bureau of Indian Standards (BIS)** standards for their products. Instead of manually browsing through 25,000+ standards, users can ask natural-language questions and receive ranked, confidence-scored results.

### Example Query
> *"I want to manufacture an electric kettle in India. Which BIS standards apply to it, what tests are required, and how do I get certification?"*

**BIS AI responds with:**
- A concise AI summary explaining the compliance roadmap
- Ranked standard cards (IS 302, IS 4250, IS 13252, etc.) with confidence scores
- Clickable detail panels showing key clauses, scope, and official references

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌌 **Wormhole Starfield** | Canvas-based animated background with 500 stars streaming through a hyperspace vortex |
| 🪟 **Liquid Glass UI** | Apple visionOS-style glassmorphism panels with `backdrop-blur`, subtle borders, and glow effects |
| 💬 **ChatGPT-style Input** | Multi-line textarea with Enter-to-submit, file attachment (PDF/DOCX), and voice recording |
| 🎤 **Voice Input** | Browser MediaRecorder API for voice-to-query transcription |
| 📎 **File Upload** | Drag-and-drop or click to attach engineering spec documents |
| 🔍 **3-Step Search Animation** | Visual pipeline: Magnifying → Scanning → Ranking |
| 📊 **Confidence-Scored Cards** | Color-coded bars — 🟢 High (>80%) · 🟡 Moderate (55-79%) · 🔵 Low (<55%) |
| 📋 **Standard Detail Drawer** | Slide-in panel with key clauses, scope, division, and BIS portal links |
| 🕐 **Search History** | Sidebar with previous queries and one-click replay |
| ⚡ **Suggestion Pills** | Quick-action chips for common queries |

---

## 🏗️ Architecture

```
BIS-AI/
├── backend/                    # FastAPI Python backend
│   ├── main.py                 # API server (health, search, upload, transcribe)
│   ├── requirements.txt        # Python dependencies
│   ├── data_engine/            # BIS data ingestion (Phase 2)
│   ├── search_engine/          # Hybrid BM25 + semantic search (Phase 3)
│   └── services/               # AI synthesis layer (Phase 4)
│
├── frontend/                   # Next.js 14 + TypeScript + Tailwind CSS
│   └── src/
│       ├── app/
│       │   ├── page.tsx        # Main page (landing → loading → results)
│       │   ├── layout.tsx      # Root layout
│       │   └── globals.css     # Glass utilities, animations, scrollbar
│       ├── components/
│       │   ├── WormholeStars   # Canvas wormhole animation
│       │   ├── ChatInput       # Input box with file/audio/send
│       │   ├── StandardCard    # Result card with confidence bar
│       │   ├── AIResponse      # AI summary with keyword pills
│       │   ├── SearchProgress  # Multi-step loading animation
│       │   ├── StandardDetailModal  # Slide-in detail drawer
│       │   ├── Sidebar         # Search history panel
│       │   ├── Header          # Top navigation bar
│       │   └── SuggestionPills # Quick-action chips
│       ├── hooks/
│       │   └── useVoiceRecorder.ts
│       └── lib/
│           ├── types.ts        # TypeScript interfaces
│           └── api.ts          # Backend API client
│
├── data/                       # BIS dataset storage
├── netlify.toml                # Netlify deployment config
└── run_dev.bat                 # One-click dev server launcher
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Next.js 14 (App Router), TypeScript, Tailwind CSS, Framer Motion, Lucide Icons |
| **Backend** | FastAPI, Uvicorn, Pydantic v2 |
| **Search (Phase 3)** | BM25 (rank-bm25) + Sentence-Transformers + ChromaDB |
| **AI (Phase 4)** | Google Gemini / OpenAI GPT for query expansion & synthesis |
| **Deployment** | Netlify (frontend), Docker (full stack) |

---

## ⚡ Quick Start

### Prerequisites
- **Node.js** 18+ and npm
- **Python** 3.10+ (for backend)

### Frontend Only (Recommended for Demo)

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Full Stack (Frontend + Backend)

**Windows:**
```bash
run_dev.bat
```

**Manual:**
```bash
# Terminal 1 — Backend
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000

# Terminal 2 — Frontend
cd frontend
npm install
npm run dev
```

---

## 🌐 Deployment

### Netlify (Static Frontend)

1. Connect this repo to Netlify
2. The `netlify.toml` auto-configures:
   - **Base directory:** `frontend`
   - **Build command:** `npm run build`
   - **Publish directory:** `out`
3. Deploy — done!

---

## 📋 Roadmap

| Phase | Description | Status |
|---|---|---|
| 1 | Project Architecture + Full Frontend | ✅ Complete |
| 2 | BIS Dataset Ingestion & Indexing | ⬜ Planned |
| 3 | Hybrid RAG Search Engine (BM25 + Semantic) | ⬜ Planned |
| 4 | Backend API + AI Synthesis | ⬜ Planned |
| 5 | End-to-End Integration | ⬜ Planned |
| 6 | Polish & Production Deployment | ⬜ Planned |

---

## 📄 License

This project is built for the **Smart India Hackathon (SIH)** initiative.

---

<p align="center">
  Built with ⚡ by Team BIS AI
</p>
