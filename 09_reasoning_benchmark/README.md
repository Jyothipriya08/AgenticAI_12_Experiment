# Project 09 — Reasoning Model Benchmarking Suite

> **Empirical Evaluation of LLM Prompt Strategies Powered by Google Gemini 2.5 Flash**

---

## 🎯 Overview

The **Reasoning Model Benchmarking Suite** systematically evaluates model performance across four distinct prompting paradigms: **Zero-shot**, **Few-shot**, **Chain-of-Thought (CoT)**, and **ReAct**. It computes empirical accuracy, average TTFT latency, total token consumption, and cost trade-offs.

---

## 🏗️ Benchmark Framework

```
[Benchmark Problem Dataset (`problems.json`)]
          │
          ▼
[Prompt Strategy Evaluator Loop]
   ├── 1. Zero-shot Evaluation
   ├── 2. Few-shot In-Context Learning Evaluation
   ├── 3. Chain-of-Thought (CoT) Step-by-Step Reasoning
   └── 4. ReAct Tool-Augmented Reasoning
          │
          ▼
[Metrics Aggregator (Accuracy %, Latency ms, Token Usage)]
          │
          ▼
[Comparative Benchmark Dashboard (Port 8009)]
```

---

## ⚡ Key Features

- **Multi-Strategy Comparative Analysis**: Evaluates 4 prompting paradigms side-by-side.
- **Empirical Metrics**: Measures pass rate, average execution latency (ms), and token efficiency.
- **Visual Analytics**: Interactive strategy cards, metric comparison bars, and benchmark summaries.
- **Standardized Datasets**: Benchmark problems cover math, logic, coding, and multi-step reasoning.

---

## 🔌 API Endpoints Specification

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves the Reasoning Benchmark UI. |
| `GET` | `/api/benchmark` | Runs benchmark suite across all strategies and returns aggregated metrics. |

---

## 🚀 Running Standalone Server

To run Project 09 standalone on port `8009`:

```bash
cd 09_reasoning_benchmark/src
python -m uvicorn server:app --host 127.0.0.1 --port 8009
```

Access the UI at: **http://127.0.0.1:8009**

---

## 🧪 Automated Testing

Run unit tests for Project 09:

```bash
python -m pytest 09_reasoning_benchmark/tests/
```
