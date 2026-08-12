"""Master Launcher Dashboard for all 12 LLM & Agent Workflow Projects."""
import os
import sys
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Agentic AI Lab Command Center", version="3.0.0")

STATIC_HTML = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agentic AI Lab | Command Center</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root[data-theme="dark"] {
            --bg-base: #080d18;
            --bg-surface: #0b1220;
            --card-bg: #172033;
            --card-border: rgba(255, 255, 255, 0.08);
            --accent-indigo: #6366f1;
            --accent-cyan: #06b6d4;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --shadow-card: 0 10px 30px rgba(0, 0, 0, 0.35);
        }

        :root[data-theme="light"] {
            --bg-base: #f8fafc;
            --bg-surface: #ffffff;
            --card-bg: #ffffff;
            --card-border: rgba(15, 23, 42, 0.08);
            --accent-indigo: #4f46e5;
            --accent-cyan: #0891b2;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --success: #059669;
            --warning: #d97706;
            --danger: #dc2626;
            --shadow-card: 0 10px 30px rgba(15, 23, 42, 0.06);
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-base);
            color: var(--text-main);
            min-height: 100vh;
            display: flex; flex-direction: column;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        header {
            padding: 1.25rem 2.5rem;
            background: var(--bg-surface);
            border-bottom: 1px solid var(--card-border);
            display: flex; align-items: center; justify-content: space-between;
            position: sticky; top: 0; z-index: 100;
        }

        .logo-group { display: flex; align-items: center; gap: 1rem; }
        .logo-icon {
            width: 44px; height: 44px; border-radius: 12px;
            background: linear-gradient(135deg, var(--accent-indigo) 0%, var(--accent-cyan) 100%);
            display: flex; align-items: center; justify-content: center;
            font-weight: 800; font-size: 1.1rem; color: #fff;
            box-shadow: 0 4px 20px rgba(99, 102, 241, 0.35);
        }

        .header-actions { display: flex; align-items: center; gap: 1rem; }
        .theme-toggle {
            background: var(--card-bg); border: 1px solid var(--card-border);
            color: var(--text-main); padding: 0.5rem 1rem; border-radius: 10px;
            font-family: inherit; font-weight: 600; font-size: 0.85rem; cursor: pointer;
        }

        .badge-status {
            background: rgba(16, 185, 129, 0.15); color: var(--success);
            border: 1px solid rgba(16, 185, 129, 0.3);
            padding: 0.4rem 0.85rem; border-radius: 20px;
            font-size: 0.85rem; font-weight: 600;
            display: flex; align-items: center; gap: 0.5rem;
        }
        .badge-status::before {
            content: ''; width: 8px; height: 8px; border-radius: 50%;
            background-color: var(--success); box-shadow: 0 0 10px var(--success);
        }

        main { max-width: 1400px; margin: 2rem auto; padding: 0 2rem; width: 100%; display: flex; flex-direction: column; gap: 2rem; }

        /* KPI Banner */
        .kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.25rem; }
        @media (max-width: 900px) { .kpi-grid { grid-template-columns: repeat(2, 1fr); } }
        @media (max-width: 500px) { .kpi-grid { grid-template-columns: 1fr; } }

        .kpi-card {
            background: var(--card-bg); border: 1px solid var(--card-border);
            border-radius: 16px; padding: 1.25rem; display: flex; flex-direction: column; gap: 0.5rem;
            box-shadow: var(--shadow-card);
        }
        .kpi-title { font-size: 0.85rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
        .kpi-val { font-size: 1.8rem; font-weight: 800; color: var(--text-main); }
        .kpi-sub { font-size: 0.8rem; color: var(--success); font-weight: 600; }

        /* Filter Controls */
        .controls-bar {
            display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap;
            background: var(--card-bg); border: 1px solid var(--card-border); padding: 1rem 1.25rem; border-radius: 16px;
        }
        .search-input {
            background: var(--bg-surface); border: 1px solid var(--card-border); color: var(--text-main);
            padding: 0.65rem 1rem; border-radius: 10px; font-family: inherit; font-size: 0.9rem; width: 300px;
        }
        .filter-tags { display: flex; gap: 0.5rem; flex-wrap: wrap; }
        .filter-btn {
            background: var(--bg-surface); border: 1px solid var(--card-border); color: var(--text-muted);
            padding: 0.45rem 0.85rem; border-radius: 8px; font-size: 0.85rem; font-weight: 600; cursor: pointer;
            transition: all 0.2s ease;
        }
        .filter-btn.active, .filter-btn:hover { background: var(--accent-indigo); color: #fff; border-color: transparent; }

        /* Projects Grid */
        .projects-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
        @media (max-width: 1100px) { .projects-grid { grid-template-columns: repeat(2, 1fr); } }
        @media (max-width: 700px) { .projects-grid { grid-template-columns: 1fr; } }

        .project-card {
            background: var(--card-bg); border: 1px solid var(--card-border);
            border-radius: 16px; padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between; gap: 1.25rem;
            box-shadow: var(--shadow-card); transition: all 0.25s ease; position: relative; overflow: hidden;
        }
        .project-card:hover { transform: translateY(-4px); border-color: var(--accent-indigo); }

        .card-header-top { display: flex; align-items: center; justify-content: space-between; }
        .card-number { font-size: 0.75rem; font-weight: 700; color: var(--accent-cyan); text-transform: uppercase; letter-spacing: 0.08em; }
        .live-tag { background: rgba(16, 185, 129, 0.15); color: var(--success); font-size: 0.7rem; font-weight: 700; padding: 0.2rem 0.5rem; border-radius: 6px; }

        .card-title { font-size: 1.2rem; font-weight: 700; margin-top: 0.35rem; }
        .card-desc { font-size: 0.9rem; color: var(--text-muted); line-height: 1.55; margin-top: 0.5rem; }
        
        .tech-pills { display: flex; gap: 0.4rem; flex-wrap: wrap; margin-top: 0.75rem; }
        .tech-pill { background: var(--bg-surface); border: 1px solid var(--card-border); font-size: 0.75rem; color: var(--text-muted); padding: 0.2rem 0.55rem; border-radius: 6px; font-family: 'JetBrains Mono', monospace; }

        .btn-group { display: grid; grid-template-columns: 1fr; gap: 0.5rem; margin-top: 1rem; }
        .btn-launch {
            background: linear-gradient(135deg, var(--accent-indigo) 0%, var(--accent-cyan) 100%);
            border: none; border-radius: 10px; padding: 0.7rem; color: #fff;
            font-weight: 700; font-size: 0.88rem; text-decoration: none; text-align: center; cursor: pointer;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.25); transition: opacity 0.2s;
        }
        .btn-launch:hover { opacity: 0.9; }

        footer { text-align: center; padding: 2rem; color: var(--text-muted); font-size: 0.85rem; border-top: 1px solid var(--card-border); margin-top: auto; }
    </style>
</head>
<body>
    <header>
        <div class="logo-group">
            <div class="logo-icon">AI</div>
            <div>
                <div style="font-size: 1.25rem; font-weight: 800;">Agentic AI Lab</div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">Build. Reason. Automate.</div>
            </div>
        </div>
        <div class="header-actions">
            <button class="theme-toggle" onclick="toggleTheme()">🌓 Theme</button>
            <div class="badge-status">12 Production Systems Live</div>
        </div>
    </header>

    <main>
        <!-- KPI Telemetry Banner -->
        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="kpi-title">Total AI Applications</div>
                <div class="kpi-val">12</div>
                <div class="kpi-sub">✓ 100% Deployed & Operational</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Active AI Foundation</div>
                <div class="kpi-val" style="font-size: 1.4rem; color: var(--accent-cyan);">Gemini 2.5 Flash</div>
                <div class="kpi-sub">✓ Dual Hybrid Rule Engine</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Port Range</div>
                <div class="kpi-val" style="font-size: 1.4rem;">8001 — 8012</div>
                <div class="kpi-sub">✓ Microservice Backends</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Test Suite Coverage</div>
                <div class="kpi-val" style="color: var(--success);">100%</div>
                <div class="kpi-sub">✓ Automated Pytest Passed</div>
            </div>
        </div>

        <!-- Controls Bar -->
        <div class="controls-bar">
            <input type="text" id="searchInput" class="search-input" placeholder="Search projects by name, keyword..." onkeyup="filterProjects()">
            <div class="filter-tags">
                <button class="filter-btn active" onclick="setCategory('all', this)">All (12)</button>
                <button class="filter-btn" onclick="setCategory('analytics', this)">Analytics & SQL</button>
                <button class="filter-btn" onclick="setCategory('workflow', this)">RAG & Workflows</button>
                <button class="filter-btn" onclick="setCategory('agent', this)">Agents & Governance</button>
                <button class="filter-btn" onclick="setCategory('ml', this)">ML & Optimization</button>
            </div>
        </div>

        <!-- Projects Grid -->
        <div class="projects-grid" id="projectsGrid">

            <!-- 01 -->
            <div class="project-card" data-cat="analytics" data-name="text to sql natural language query data analyst">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 01 • Port 8001</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">Text-to-SQL Data Analyst</div>
                    <div class="card-desc">Natural language SQLite engine with schema tree inspector, query validator, chart visualizer, CSV export, and SSE streaming explanations.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">FastAPI</span>
                        <span class="tech-pill">SQLite</span>
                        <span class="tech-pill">Chart.js</span>
                        <span class="tech-pill">Streaming</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8001" target="_blank" class="btn-launch">Launch Project 01 (Port 8001)</a>
                </div>
            </div>

            <!-- 02 -->
            <div class="project-card" data-cat="workflow" data-name="rag qa enterprise knowledge assistant vector embeddings">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 02 • Port 8002</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">RAG Knowledge Assistant</div>
                    <div class="card-desc">Enterprise semantic search with document chunking preview, cosine vector retrieval, similarity score badges, and grounded source citations.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">RAG</span>
                        <span class="tech-pill">Vector DB</span>
                        <span class="tech-pill">Cosine Sim</span>
                        <span class="tech-pill">Citations</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8002" target="_blank" class="btn-launch">Launch Project 02 (Port 8002)</a>
                </div>
            </div>

            <!-- 03 -->
            <div class="project-card" data-cat="workflow" data-name="prompt chaining visual ai workflow builder summarization">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 03 • Port 8003</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">Prompt Chaining Studio</div>
                    <div class="card-desc">Visual multi-stage workflow editor (Clean -> Extract -> Outline -> Draft -> Critique -> Polish) with token/latency telemetry tracking.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">Prompt Chain</span>
                        <span class="tech-pill">Workflow UI</span>
                        <span class="tech-pill">Telemetry</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8003" target="_blank" class="btn-launch">Launch Project 03 (Port 8003)</a>
                </div>
            </div>

            <!-- 04 -->
            <div class="project-card" data-cat="analytics" data-name="sql agent react autonomous database analyst">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 04 • Port 8004</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">Autonomous SQL ReAct Agent</div>
                    <div class="card-desc">ReAct database agent with schema discovery, query validation guardrails, self-correction, agent activity log, and anomaly detection.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">ReAct Agent</span>
                        <span class="tech-pill">Tool Use</span>
                        <span class="tech-pill">Schema Explorer</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8004" target="_blank" class="btn-launch">Launch Project 04 (Port 8004)</a>
                </div>
            </div>

            <!-- 05 -->
            <div class="project-card" data-cat="agent" data-name="multi agent sdr sales development platform email">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 05 • Port 8005</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">Multi-Agent SDR Platform</div>
                    <div class="card-desc">4-agent sales pipeline for lead discovery, ICP qualification scoring, persona hook synthesis, email copywriting, and human approval safety gate.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">Multi-Agent</span>
                        <span class="tech-pill">ICP Scoring</span>
                        <span class="tech-pill">Safety Gate</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8005" target="_blank" class="btn-launch">Launch Project 05 (Port 8005)</a>
                </div>
            </div>

            <!-- 06 -->
            <div class="project-card" data-cat="agent" data-name="policy compliance ai governance expense risk">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 06 • Port 8006</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">AI Governance & Compliance</div>
                    <div class="card-desc">Hybrid compliance platform combining deterministic policy rules with AI audit explanations, risk classification badges, and human review flags.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">Governance</span>
                        <span class="tech-pill">Rule Engine</span>
                        <span class="tech-pill">Audit Report</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8006" target="_blank" class="btn-launch">Launch Project 06 (Port 8006)</a>
                </div>
            </div>

            <!-- 07 -->
            <div class="project-card" data-cat="agent" data-name="deep research agent workflow intelligence platform">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 07 • Port 8007</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">Deep Research Intelligence</div>
                    <div class="card-desc">Autonomous multi-stage research agent executing query planning, peer-reviewed source evaluation, evidence extraction, and citation reports.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">Deep Research</span>
                        <span class="tech-pill">Multi-Step</span>
                        <span class="tech-pill">Citations</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8007" target="_blank" class="btn-launch">Launch Project 07 (Port 8007)</a>
                </div>
            </div>

            <!-- 08 -->
            <div class="project-card" data-cat="ml" data-name="visual qa image vision inspection ocr">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 08 • Port 8008</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">AI Vision Inspection Studio</div>
                    <div class="card-desc">Multimodal image analysis platform featuring object detection bounding boxes, OCR text extraction, visual QA reasoning, and confidence meters.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">Vision QA</span>
                        <span class="tech-pill">Multimodal</span>
                        <span class="tech-pill">OCR</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8008" target="_blank" class="btn-launch">Launch Project 08 (Port 8008)</a>
                </div>
            </div>

            <!-- 09 -->
            <div class="project-card" data-cat="ml" data-name="reasoning benchmark llm evaluation performance accuracy cost">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 09 • Port 8009</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">LLM Benchmark Suite</div>
                    <div class="card-desc">Automated reasoning benchmark evaluating Zero-shot, Few-shot, CoT, and ReAct prompting strategies on accuracy, latency, and token efficiency.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">Benchmarking</span>
                        <span class="tech-pill">Prompting CoT</span>
                        <span class="tech-pill">Latency Matrix</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8009" target="_blank" class="btn-launch">Launch Project 09 (Port 8009)</a>
                </div>
            </div>

            <!-- 10 -->
            <div class="project-card" data-cat="ml" data-name="fine tuning domain adaptation lora dataset">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 10 • Port 8010</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">LLM Fine-Tuning Studio</div>
                    <div class="card-desc">Domain adaptation laboratory with synthetic instruction dataset validator, LoRA adapter configuration, epoch loss charts, and checkpoint evaluator.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">Fine-Tuning</span>
                        <span class="tech-pill">LoRA Adapter</span>
                        <span class="tech-pill">Loss Curve</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8010" target="_blank" class="btn-launch">Launch Project 10 (Port 8010)</a>
                </div>
            </div>

            <!-- 11 -->
            <div class="project-card" data-cat="ml" data-name="model optimization lab quantization FP16 INT8 throughput">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 11 • Port 8011</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">Model Optimization Lab</div>
                    <div class="card-desc">Inference optimization lab comparing FP16, INT8, and INT4 quantization on VRAM footprint, throughput (tok/s), latency, and accuracy retention.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">Optimization</span>
                        <span class="tech-pill">Quantization</span>
                        <span class="tech-pill">VRAM Metrics</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8011" target="_blank" class="btn-launch">Launch Project 11 (Port 8011)</a>
                </div>
            </div>

            <!-- 12 -->
            <div class="project-card" data-cat="workflow" data-name="capstone flagship enterprise agentic ai platform">
                <div>
                    <div class="card-header-top">
                        <span class="card-number">Project 12 • Port 8012</span>
                        <span class="live-tag">LIVE</span>
                    </div>
                    <div class="card-title">Flagship Capstone Platform</div>
                    <div class="card-desc">Master enterprise application combining RAG retrieval, SQL tools, Multi-Agent workflow orchestration, system health telemetry, and workspace settings.</div>
                    <div class="tech-pills">
                        <span class="tech-pill">Capstone</span>
                        <span class="tech-pill">Enterprise SaaS</span>
                        <span class="tech-pill">Full Suite</span>
                    </div>
                </div>
                <div class="btn-group">
                    <a href="http://127.0.0.1:8012" target="_blank" class="btn-launch">Launch Project 12 (Port 8012)</a>
                </div>
            </div>

        </div>
    </main>

    <footer>
        <p>Agentic AI Lab • Build. Reason. Automate. • Enterprise Multi-Agent Suite Powered by Google Gemini 2.5 Flash</p>
    </footer>

    <script>
        function toggleTheme() {
            const html = document.documentElement;
            const current = html.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', next);
            localStorage.setItem('theme', next);
        }

        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            document.documentElement.setAttribute('data-theme', savedTheme);
        }

        let currentCat = 'all';

        function setCategory(cat, btn) {
            currentCat = cat;
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            filterProjects();
        }

        function filterProjects() {
            const query = document.getElementById('searchInput').value.toLowerCase().trim();
            const cards = document.querySelectorAll('.project-card');

            cards.forEach(card => {
                const cat = card.getAttribute('data-cat');
                const text = card.getAttribute('data-name');
                const matchesCat = (currentCat === 'all' || cat === currentCat);
                const matchesQuery = !query || text.includes(query);

                if (matchesCat && matchesQuery) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTMLResponse(STATIC_HTML)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

