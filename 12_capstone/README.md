# Project 12 — Flagship Capstone End-to-End Agentic Platform

> **Integrated Enterprise AI Workspace Powered by Google Gemini 2.5 Flash**

---

## 🎯 Overview

The **Flagship Capstone End-to-End Agentic Platform** represents the culmination of all 12 projects. It integrates Master Orchestrator Intent Planning, Specialist SQL Query Execution, Policy Safety Guardrails, and Synthesis Engines into a single unified workspace with complete observability trace logging.

---

## 🏗️ Master Orchestrator Architecture

```
[User Request Input]
          │
          ▼
[MasterPlannerAgent (Gemini 2.5 Intent Planning)]
          │
          ▼
[SQLSpecialistAgent (Query Translation & Execution)]
          │
          ▼
[PolicyGuardrailAgent (Safety Rules & Read-Only Checks)]
          │
          ▼
[SynthesisEngine (Master Response Generation)]
          │
          ▼
[Execution Trace Logger (Node Latency & Step Metadata)] ──► [Capstone Studio Dashboard]
```

---

## ⚡ Key Features

- **Integrated Multi-Agent Workflow**: Combines planning, SQL database execution, and policy guardrails.
- **Full Observability Trace**: Logs step timestamps, agent actions, payload details, and per-node latency (ms).
- **Master Synthesis Engine**: Generates comprehensive structured responses with execution metrics.
- **Enterprise Dashboard**: Dark Navy glassmorphism UI with interactive trace tree, execution controls, and status telemetry.

---

## 🔌 API Endpoints Specification

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves the Flagship Capstone Studio UI. |
| `POST` | `/api/run-capstone` | Executes master agentic workflow and returns trace log & synthesis. |

---

## 🚀 Running Standalone Server

To run Project 12 standalone on port `8012`:

```bash
cd 12_capstone/src
python -m uvicorn server:app --host 127.0.0.1 --port 8012
```

Access the UI at: **http://127.0.0.1:8012**

---

## 🧪 Automated Testing

Run unit tests for Project 12:

```bash
python -m pytest 12_capstone/tests/
```
