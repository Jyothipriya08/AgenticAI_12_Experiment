# Project 11 — Model Optimization Experiment Lab

> **Inference Quantization & Hardware Acceleration Benchmarking Powered by Google Gemini 2.5 Flash**

---

## 🎯 Overview

The **Model Optimization Experiment Lab** benchmarks post-training quantization (PTQ) techniques. It evaluates model performance across **FP16 (Baseline)**, **INT8 (8-bit Quantization)**, and **INT4 (4-bit AWQ)** precisions, comparing VRAM footprint, TTFT latency, throughput (tok/s), perplexity shift, and quality retention scores.

---

## 🏗️ Optimization Benchmark Matrix

```
                      ┌─────────────────────────────────────────┐
                      │    Precision Optimization Matrix       │
                      ├──────────┬──────────┬──────────┬────────┤
                      │ Precision│ VRAM GB  │ Tok/sec  │ Quality│
                      ├──────────┼──────────┼──────────┼────────┤
                      │   FP16   │  16.0GB  │  38.5    │ 100.0% │
                      │   INT8   │   8.2GB  │  64.0    │  98.6% │
                      │   INT4   │   4.5GB  │  88.2    │  94.2% │
                      └──────────┴──────────┴──────────┴────────┘
                                      │
                                      ▼
             [Trade-off Report Generator (71.9% VRAM Savings, 2.29x Speedup)]
```

---

## ⚡ Key Features

- **Quantization Comparison Lab**: Side-by-side comparison of FP16, INT8, and INT4 precisions.
- **VRAM & Throughput Metrics**: Measures memory reduction, time-to-first-token (TTFT), and token generation speed.
- **Engineering Recommendation Engine**: Synthesizes 3-bullet deployment trade-off reports using Gemini 2.5 Flash.
- **Interactive UI Cards**: Visual charts displaying throughput gains and quality retention scores.

---

## 🔌 API Endpoints Specification

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves the Model Optimization Lab UI. |
| `POST` | `/api/run-optimization` | Runs precision benchmark suite and returns trade-off report. |

---

## 🚀 Running Standalone Server

To run Project 11 standalone on port `8011`:

```bash
cd 11_model_optimization/src
python -m uvicorn server:app --host 127.0.0.1 --port 8011
```

Access the UI at: **http://127.0.0.1:8011**

---

## 🧪 Automated Testing

Run unit tests for Project 11:

```bash
python -m pytest 11_model_optimization/tests/
```
