# Project 07 — Deep Research Intelligence Platform

> **Autonomous Multi-Step AI Research Agent Powered by Google Gemini 2.5 Flash**

---

## 🎯 Overview

The **Deep Research Intelligence Platform** executes autonomous research workflows. It decomposes user research topics into targeted sub-questions, gathers evidence from an indexed corpus, synthesizes structured technical reports with inline citations, reflects on missing knowledge gaps, and revises final outputs.

---

## 🏗️ 5-Step Deep Research Pipeline

```
[Research Topic Input]
          │
          ▼
[Step 1: Decompose Topic into Sub-Questions]
          │
          ▼
[Step 2: Gather Evidence from Indexed Web Corpus]
          │
          ▼
[Step 3: Synthesize Grounded Report Draft with Citations]
          │
          ▼
[Step 4: Self-Reflection & Gap Detection Scoring]
          │
          ▼
[Step 5: Revise & Finalize Comprehensive Report]
```

---

## ⚡ Key Features

- **Autonomous Topic Decomposition**: Breaks broad prompts into structured technical sub-inquiries.
- **Evidence Gathering & Citations**: Matches corpus items and attaches `[Source: URL]` references.
- **Self-Reflection Agent**: Evaluates report completeness and identifies missing domain perspectives.
- **Report Export**: Download finalized research reports directly from the web interface.

---

## 🔌 API Endpoints Specification

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves the Deep Research Platform UI. |
| `POST` | `/api/research` | Executes 5-step research pipeline and returns report, evidence, and gap analysis. |

---

## 🚀 Running Standalone Server

To run Project 07 standalone on port `8007`:

```bash
cd 07_deep_research/src
python -m uvicorn server:app --host 127.0.0.1 --port 8007
```

Access the UI at: **http://127.0.0.1:8007**

---

## 🧪 Automated Testing

Run unit tests for Project 07:

```bash
python -m pytest 07_deep_research/tests/
```
