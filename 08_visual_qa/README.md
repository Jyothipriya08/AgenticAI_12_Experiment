# Project 08 — Visual QA & Image Retrieval Studio

> **Multimodal Vision-Language Inspection Engine Powered by Google Gemini 2.5 Flash**

---

## 🎯 Overview

The **Visual QA & Image Retrieval Studio** combines image metadata retrieval with multimodal question answering. It indexes visual assets by tag, description, and OCR extracted text, retrieves matching catalog images, and synthesizes answers based on visual content.

---

## 🏗️ Visual QA Architecture

```
[Visual Question Input]
          │
          ▼
[Catalog Image Retriever (Tag, Description & OCR Keyword Matching)]
          │
          ▼
[Top-K Image Retrieval & Metadata Extraction]
          │
          ▼
[Google Gemini 2.5 Flash Multimodal VLM] ──(Fallback)──► [Local Visual Engine]
          │
          ▼
[FastAPI REST API (Port 8008)] ──► [Visual QA Dashboard]
```

---

## ⚡ Key Features

- **Multi-Modal Keyword Search**: Ranks catalog assets by tags, descriptions, and extracted OCR text.
- **Visual Metadata Grounding**: Answers questions referencing specific bounding details and OCR strings.
- **Catalog Management**: Displays image previews, detected tags, and extracted text overlays.
- **Graceful Fallbacks**: Local visual engine ensures robust responses even without an active LLM key.

---

## 🔌 API Endpoints Specification

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves the Visual QA Studio UI. |
| `POST` | `/api/visual-qa` | Executes visual retrieval and returns multimodal answer with asset details. |

---

## 🚀 Running Standalone Server

To run Project 08 standalone on port `8008`:

```bash
cd 08_visual_qa/src
python -m uvicorn server:app --host 127.0.0.1 --port 8008
```

Access the UI at: **http://127.0.0.1:8008**

---

## 🧪 Automated Testing

Run unit tests for Project 08:

```bash
python -m pytest 08_visual_qa/tests/
```
