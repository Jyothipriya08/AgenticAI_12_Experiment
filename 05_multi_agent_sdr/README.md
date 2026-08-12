# Project 05 — Multi-Agent SDR Platform

> **Autonomous Sales Development Representative Assembly Line with Human Approval Safety Gate**

---

## 🎯 Overview

The **Multi-Agent SDR Platform** orchestrates a 4-agent collaborative pipeline for outbound sales engineering. It enriches raw B2B leads, evaluates ICP fit scores, synthesizes persona-specific outreach hooks, drafts personalized cold emails, and enforces a mandatory Human Approval Gate before dispatch.

---

## 🏗️ 4-Agent Collaborative Architecture

```
[Raw B2B Lead Data]
        │
        ▼
[Agent 1: Lead Discovery & Enrichment]
        │
        ▼
[Agent 2: ICP Qualification Scoring (0-100)]
        │
        ▼
[Agent 3: Persona & Industry Hook Synthesis]
        │
        ▼
[Agent 4: Personalized Email Copywriter]
        │
        ▼
[🛡️ Human Approval Safety Gate] ──► [Outbound Dispatch]
```

---

## ⚡ Key Features

- **4-Agent Pipeline**: Specialized division of labor across discovery, scoring, research, and copywriting.
- **Dynamic Pain Point Engine**: Synthesizes industry-tailored pain points for FinTech, Logistics, Cloud, and Enterprise leads.
- **Human Approval Safety Gate**: Requires human verification before outbound emails can be sent.
- **Interactive CRM Dashboard**: Visual lead status badges, qualification scores, and email drafts.

---

## 🔌 API Endpoints Specification

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves the Multi-Agent SDR Platform UI. |
| `GET` | `/api/leads` | Returns available B2B lead records. |
| `POST` | `/api/process-lead` | Executes the 4-agent SDR workflow for a selected lead. |
| `POST` | `/api/approve-email` | Human approval gate endpoint to finalize outreach email. |

---

## 🚀 Running Standalone Server

To run Project 05 standalone on port `8005`:

```bash
cd 05_multi_agent_sdr/src
python -m uvicorn server:app --host 127.0.0.1 --port 8005
```

Access the UI at: **http://127.0.0.1:8005**

---

## 🧪 Automated Testing

Run unit tests for Project 05:

```bash
python -m pytest 05_multi_agent_sdr/tests/
```
