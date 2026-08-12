# Project 03 — Prompt Chaining Studio for Summarization

> **Multi-Stage Sequential Prompt Pipeline Powered by Google Gemini 2.5 Flash**

---

## 🎯 Overview

The **Prompt Chaining Studio** implements a 6-stage sequential LLM processing pipeline. Each stage performs a specific transformation step (Text Cleaning $\rightarrow$ Fact Extraction $\rightarrow$ Outline Generation $\rightarrow$ Draft Summarization $\rightarrow$ Self-Critique $\rightarrow$ Polished Output), capturing latency and token telemetry at every node.

---

## 🏗️ 6-Stage Pipeline Workflow

```
[Raw Text Input]
      │
      ▼
[Stage 1: Clean & Normalize Input]
      │
      ▼
[Stage 2: Extract Key Facts (3-5 Bullet Points)]
      │
      ▼
[Stage 3: Generate 3-Part Outline]
      │
      ▼
[Stage 4: Draft Concise Summary]
      │
      ▼
[Stage 5: Self-Critique & Completeness Scoring]
      │
      ▼
[Stage 6: Final Polished Summary]
```

---

## ⚡ Key Features

- **Visual Pipeline Node Editor**: Inspect intermediate outputs at every step of the chain.
- **Dynamic Text Processing**: Generates outlines, summaries, and critiques dynamically based on input content.
- **Latency & Token Metrics**: Tracks execution time and estimated token consumption per stage.
- **Graceful API Fallbacks**: Fallback text transformation logic ensures pipeline execution even without an API key.

---

## 🔌 API Endpoints Specification

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves the Prompt Chaining Studio UI. |
| `POST` | `/api/chain` | Executes the complete 6-stage prompt chain and returns stage outputs & telemetry. |

---

## 🚀 Running Standalone Server

To run Project 03 standalone on port `8003`:

```bash
cd 03_prompt_chaining/src
python -m uvicorn server:app --host 127.0.0.1 --port 8003
```

Access the UI at: **http://127.0.0.1:8003**

---

## 🧪 Automated Testing

Run unit tests for Project 03:

```bash
python -m pytest 03_prompt_chaining/tests/
```
