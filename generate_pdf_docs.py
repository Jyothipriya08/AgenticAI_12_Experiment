"""Script to generate enterprise-grade PDF documentation for all 12 Agentic AI projects using ReportLab."""
import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

PROJECTS_PDF_DATA = [
    {
        "folder": "01_text_to_sql",
        "pdf_name": "01_text_to_sql_documentation.pdf",
        "title": "Project 01: Real-Time Text-to-SQL AI Studio",
        "tagline": "Natural Language Database Analytics Powered by Google Gemini 2.5 Flash",
        "overview": "The Text-to-SQL AI Studio translates natural language questions into safe, executable SQLite queries. It features a continuous real-time e-commerce transaction stream, interactive Schema Explorer, read-only SQL safety validator, CSV data exporter, and SSE streaming AI query explanations.",
        "architecture": [
            "User Question Input -> SchemaRetriever & Few-Shot Examples",
            "Google Gemini 2.5 Flash Generator (Fallback: Schema Rule Engine)",
            "SQLValidator (Regex & Read-Only Safety Verification)",
            "SQLite Execution Engine (timeout=30.0s) -> Tabular Results & Chart UI"
        ],
        "endpoints": [
            ["GET", "/", "Serves single-page glassmorphism web application"],
            ["GET", "/api/schema", "Returns database schema summary"],
            ["GET", "/api/realtime-stats", "Returns live revenue, total order count, and latest transaction"],
            ["POST", "/api/query", "Translates natural language to SQL and executes query"],
            ["POST", "/api/simulate-live-order", "Triggers a real-time order transaction"],
            ["GET", "/api/stream-explain", "Streams token-by-token AI query explanations via SSE"]
        ],
        "port": 8001,
        "test_cmd": "python -m pytest 01_text_to_sql/tests/"
    },
    {
        "folder": "02_rag_qa",
        "pdf_name": "02_rag_qa_documentation.pdf",
        "title": "Project 02: RAG-Based Question Answering AI Studio",
        "tagline": "Enterprise Retrieval-Augmented Generation Grounded in Corpus Context",
        "overview": "The RAG QA Engine provides grounded document intelligence. It ingests custom knowledge bases, performs automated text chunking with overlap (250 chars, 30 overlap), indexes chunks via TF-IDF cosine similarity, and synthesizes answers with source citations.",
        "architecture": [
            "Document Ingestion -> DocumentChunker (250 chars, 30 overlap)",
            "SimpleVectorStore TF-IDF Cosine Similarity Indexing",
            "User Question -> Top-K Chunk Retrieval & Grounded Context Assembly",
            "Google Gemini 2.5 Flash Grounded Synthesis -> Answer with [Source | Chunk ID] Citations"
        ],
        "endpoints": [
            ["GET", "/", "Serves RAG AI Studio web UI"],
            ["GET", "/api/status", "Returns vector store status, chunk counts, and indexed sources"],
            ["GET", "/api/documents", "Lists indexed documents and chunk previews"],
            ["POST", "/api/ingest", "Ingests new text content into vector store"],
            ["POST", "/api/query", "Executes RAG query and returns grounded answer with citations"]
        ],
        "port": 8002,
        "test_cmd": "python -m pytest 02_rag_qa/tests/"
    },
    {
        "folder": "03_prompt_chaining",
        "pdf_name": "03_prompt_chaining_documentation.pdf",
        "title": "Project 03: Prompt Chaining Studio for Summarization",
        "tagline": "Multi-Stage Sequential Prompt Transformation Pipeline",
        "overview": "The Prompt Chaining Studio implements a 6-stage sequential LLM processing pipeline. Each stage performs a specific transformation step (Text Cleaning -> Fact Extraction -> Outline Generation -> Draft Summarization -> Self-Critique -> Polished Output), tracking latency and token telemetry per stage.",
        "architecture": [
            "Stage 1: Clean & Normalize Input Raw Text",
            "Stage 2: Extract 3-5 Core Factual Bullet Points",
            "Stage 3: Generate Structured 3-Part Outline",
            "Stage 4: Draft Concise Summary",
            "Stage 5: Self-Critique & Completeness Scoring (0-100)",
            "Stage 6: Final Polished Executive Summary Output"
        ],
        "endpoints": [
            ["GET", "/", "Serves Prompt Chaining Studio web UI"],
            ["POST", "/api/chain", "Executes 6-stage prompt chain and returns stage outputs & telemetry"]
        ],
        "port": 8003,
        "test_cmd": "python -m pytest 03_prompt_chaining/tests/"
    },
    {
        "folder": "04_sql_agent",
        "pdf_name": "04_sql_agent_documentation.pdf",
        "title": "Project 04: Autonomous SQL ReAct Agent",
        "tagline": "Tool-Augmented Reasoning & Acting Agent Loop",
        "overview": "The ReAct SQL Agent implements the Reasoning + Acting paradigm. The agent dynamically decides which database tools to invoke (inspect_schema, validate_sql, run_sql_query), observes output results, self-corrects invalid queries, and synthesizes final answers.",
        "architecture": [
            "Thought 1: Inspect database schema -> Action: inspect_schema()",
            "Observation 1: Retrieve tables & column data types",
            "Thought 2: Formulate SQLite SELECT query -> Action: run_sql_query(sql)",
            "Observation 2: Execute query safely & capture tabular rows",
            "Synthesis: Generate final answer with full trajectory log"
        ],
        "endpoints": [
            ["GET", "/", "Serves ReAct SQL Agent web UI"],
            ["GET", "/api/schema", "Returns database schema specification"],
            ["POST", "/api/run-agent", "Executes ReAct agent workflow and returns trajectory logs"]
        ],
        "port": 8004,
        "test_cmd": "python -m pytest 04_sql_agent/tests/"
    },
    {
        "folder": "05_multi_agent_sdr",
        "pdf_name": "05_multi_agent_sdr_documentation.pdf",
        "title": "Project 05: Multi-Agent SDR Platform",
        "tagline": "Autonomous Sales Development Representative Assembly Line",
        "overview": "The Multi-Agent SDR Platform orchestrates a 4-agent collaborative pipeline for B2B sales engineering. It enriches raw leads, evaluates ICP fit scores, synthesizes persona-specific outreach hooks, drafts personalized cold emails, and enforces a mandatory Human Approval Gate before dispatch.",
        "architecture": [
            "Agent 1: Lead Discovery & Profile Enrichment",
            "Agent 2: ICP Qualification Scoring (0-100 Scale)",
            "Agent 3: Industry Pain Point & Persona Hook Synthesis",
            "Agent 4: Personalized Cold Email Copywriter",
            "Human Approval Safety Gate -> Outbound Sales Dispatch"
        ],
        "endpoints": [
            ["GET", "/", "Serves Multi-Agent SDR Platform web UI"],
            ["GET", "/api/leads", "Returns available B2B lead records"],
            ["POST", "/api/process-lead", "Executes 4-agent SDR workflow for selected lead"],
            ["POST", "/api/approve-email", "Human approval gate endpoint to finalize outreach email"]
        ],
        "port": 8005,
        "test_cmd": "python -m pytest 05_multi_agent_sdr/tests/"
    },
    {
        "folder": "06_policy_compliance",
        "pdf_name": "06_policy_compliance_documentation.pdf",
        "title": "Project 06: AI Policy & Compliance Governance Engine",
        "tagline": "Hybrid Rule & LLM Corporate Expense Governance",
        "overview": "The AI Policy & Compliance Engine evaluates corporate expense claims against financial policy rules. It uses a deterministic rule engine to flag maximum transaction limits ($1,000), restricted merchants, and missing receipts ($50 threshold), combined with Gemini 2.5 Flash to generate formal executive compliance reports.",
        "architecture": [
            "Deterministic Rule Engine Checks (Transaction Limits, Merchant Restrictions, Receipts)",
            "Status Classification: COMPLIANT / WARNING / NON_COMPLIANT",
            "Google Gemini 2.5 Flash Auditor -> Formal Executive Audit Summary",
            "Human Oversight Flagging for NON_COMPLIANT and WARNING claims"
        ],
        "endpoints": [
            ["GET", "/", "Serves Policy Compliance web UI"],
            ["GET", "/api/policies", "Returns corporate policy rules and threshold definitions"],
            ["POST", "/api/audit-claim", "Audits expense claim and returns status, violations, and summary"]
        ],
        "port": 8006,
        "test_cmd": "python -m pytest 06_policy_compliance/tests/"
    },
    {
        "folder": "07_deep_research",
        "pdf_name": "07_deep_research_documentation.pdf",
        "title": "Project 07: Deep Research Intelligence Platform",
        "tagline": "Autonomous Multi-Step AI Research Agent",
        "overview": "The Deep Research Intelligence Platform executes multi-step research workflows. It decomposes user research topics into targeted sub-questions, gathers evidence from an indexed corpus, synthesizes structured technical reports with inline citations, reflects on missing knowledge gaps, and revises final outputs.",
        "architecture": [
            "Step 1: Decompose Topic into Sub-Questions",
            "Step 2: Gather Evidence from Indexed Web Corpus",
            "Step 3: Synthesize Grounded Report Draft with Citations",
            "Step 4: Self-Reflection & Gap Detection Scoring",
            "Step 5: Revise & Finalize Comprehensive Report"
        ],
        "endpoints": [
            ["GET", "/", "Serves Deep Research Platform web UI"],
            ["POST", "/api/research", "Executes 5-step research pipeline and returns report & evidence"]
        ],
        "port": 8007,
        "test_cmd": "python -m pytest 07_deep_research/tests/"
    },
    {
        "folder": "08_visual_qa",
        "pdf_name": "08_visual_qa_documentation.pdf",
        "title": "Project 08: Visual QA & Image Retrieval Studio",
        "tagline": "Multimodal Vision-Language Inspection Engine",
        "overview": "The Visual QA Studio combines image metadata retrieval with multimodal question answering. It indexes visual assets by tag, description, and OCR text, retrieves matching catalog images, and synthesizes answers based on visual content.",
        "architecture": [
            "Catalog Image Keyword Indexer (Tags, Descriptions, OCR Text)",
            "Top-K Asset Retrieval & Metadata Extraction",
            "Google Gemini 2.5 Flash Multimodal VLM Grounded Synthesis",
            "Interactive Dashboard displaying image previews, tags, and OCR overlays"
        ],
        "endpoints": [
            ["GET", "/", "Serves Visual QA Studio web UI"],
            ["POST", "/api/visual-qa", "Executes visual retrieval and returns multimodal answer"]
        ],
        "port": 8008,
        "test_cmd": "python -m pytest 08_visual_qa/tests/"
    },
    {
        "folder": "09_reasoning_benchmark",
        "pdf_name": "09_reasoning_benchmark_documentation.pdf",
        "title": "Project 09: Reasoning Model Benchmarking Suite",
        "tagline": "Empirical Evaluation of LLM Prompt Strategies",
        "overview": "The Reasoning Model Benchmarking Suite systematically evaluates model performance across four distinct prompting paradigms: Zero-shot, Few-shot, Chain-of-Thought (CoT), and ReAct. It computes empirical accuracy, average TTFT latency, total token consumption, and cost trade-offs.",
        "architecture": [
            "Benchmark Dataset: Math, Logic, Coding & Reasoning Problems",
            "Evaluator Engine: Executes Zero-shot, Few-shot, CoT, and ReAct paradigms",
            "Metrics Aggregator: Pass Rate %, TTFT Latency (ms), Token Usage",
            "Comparative Analytics Dashboard on Port 8009"
        ],
        "endpoints": [
            ["GET", "/", "Serves Reasoning Benchmark web UI"],
            ["GET", "/api/benchmark", "Runs benchmark suite across all strategies and returns aggregated metrics"]
        ],
        "port": 8009,
        "test_cmd": "python -m pytest 09_reasoning_benchmark/tests/"
    },
    {
        "folder": "10_fine_tuning",
        "pdf_name": "10_fine_tuning_documentation.pdf",
        "title": "Project 10: Fine-Tuning Studio for Domain Adaptation",
        "tagline": "Instruction Data Validation & Parameter-Efficient LoRA Tuning",
        "overview": "The Fine-Tuning Studio manages parameter-efficient fine-tuning (PEFT) workflows using Low-Rank Adaptation (LoRA). It validates domain instruction JSONL data, configures rank (r=8) and scaling factor (alpha=16), tracks epoch training loss, and evaluates base vs. fine-tuned model performance gains (+44.9% accuracy gain).",
        "architecture": [
            "Dataset Validator & Tokenizer Inspector (domain_data.jsonl)",
            "LoRA Configurer (r=8, alpha=16, target_modules=[q_proj, v_proj])",
            "LoRA Adapter Trainer (Multi-Epoch Loss Tracking: 2.45 -> 0.54)",
            "Base vs. Adapted Model Evaluator (+44.9% Domain Accuracy Gain)"
        ],
        "endpoints": [
            ["GET", "/", "Serves Fine-Tuning Studio web UI"],
            ["GET/POST", "/api/run-fine-tune", "Executes LoRA adapter training and returns history & evaluation metrics"]
        ],
        "port": 8010,
        "test_cmd": "python -m pytest 10_fine_tuning/tests/"
    },
    {
        "folder": "11_model_optimization",
        "pdf_name": "11_model_optimization_documentation.pdf",
        "title": "Project 11: Model Optimization Experiment Lab",
        "tagline": "Inference Quantization & Hardware Acceleration Benchmarking",
        "overview": "The Model Optimization Lab benchmarks post-training quantization (PTQ) techniques. It evaluates FP16 (Baseline), INT8 (8-bit Quantization), and INT4 (4-bit AWQ) precisions, comparing VRAM footprint (-71.9% memory savings), TTFT latency, throughput (88.2 tok/s), perplexity shift, and quality retention scores.",
        "architecture": [
            "Precision Evaluator: FP16 Baseline vs INT8 vs INT4 AWQ",
            "Hardware Metrics: VRAM Footprint, TTFT Latency, Throughput (tok/s)",
            "Quality Retention Analyzer: Perplexity shift & Quality Score %",
            "Gemini 2.5 Flash Trade-Off Engineering Recommendation Engine"
        ],
        "endpoints": [
            ["GET", "/", "Serves Model Optimization Lab web UI"],
            ["GET/POST", "/api/run-optimization", "Runs precision benchmark suite and returns trade-off report"]
        ],
        "port": 8011,
        "test_cmd": "python -m pytest 11_model_optimization/tests/"
    },
    {
        "folder": "12_capstone",
        "pdf_name": "12_capstone_documentation.pdf",
        "title": "Project 12: Flagship Capstone End-to-End Agentic Platform",
        "tagline": "Integrated Enterprise AI Workspace Powered by Google Gemini 2.5 Flash",
        "overview": "The Flagship Capstone Platform integrates Master Orchestrator Intent Planning, Specialist SQL Query Execution, Policy Safety Guardrails, and Synthesis Engines into a single unified workspace with complete observability trace logging.",
        "architecture": [
            "MasterPlannerAgent (Gemini 2.5 Intent Planning)",
            "SQLSpecialistAgent (Query Translation & Database Execution)",
            "PolicyGuardrailAgent (Safety Rules & Read-Only Checks)",
            "SynthesisEngine (Master Response Generation)",
            "Execution Trace Logger (Node Latency & Step Metadata)"
        ],
        "endpoints": [
            ["GET", "/", "Serves Capstone Studio web UI"],
            ["POST", "/api/run-capstone", "Executes master agentic workflow and returns trace log & synthesis"]
        ],
        "port": 8012,
        "test_cmd": "python -m pytest 12_capstone/tests/"
    }
]

def build_pdf(project_data: dict, base_dir: str):
    pdf_path = os.path.join(base_dir, project_data["folder"], project_data["pdf_name"])
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0B1220'),
        spaceAfter=4
    )

    tagline_style = ParagraphStyle(
        'DocTagline',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#6366F1'),
        spaceAfter=12
    )

    h2_style = ParagraphStyle(
        'DocH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#0B1220'),
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1E293B'),
        spaceAfter=8
    )

    list_style = ParagraphStyle(
        'DocList',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        'DocCode',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#06B6D4')
    )

    story = []

    # Title & Subtitle
    story.append(Paragraph(project_data["title"], title_style))
    story.append(Paragraph(project_data["tagline"], tagline_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#6366F1'), spaceAfter=10))

    # Executive Overview
    story.append(Paragraph("1. Executive Overview", h2_style))
    story.append(Paragraph(project_data["overview"], body_style))

    # System Architecture
    story.append(Paragraph("2. System Architecture & Workflow Pipeline", h2_style))
    for step in project_data["architecture"]:
        story.append(Paragraph(f"• {step}", list_style))
    story.append(Spacer(1, 8))

    # API Endpoints Table
    story.append(Paragraph("3. API Endpoints Specification", h2_style))
    table_data = [["Method", "Endpoint", "Description"]]
    for ep in project_data["endpoints"]:
        table_data.append([
            Paragraph(f"<b>{ep[0]}</b>", body_style),
            Paragraph(f"<font color='#06B6D4'>{ep[1]}</font>", code_style),
            Paragraph(ep[2], body_style)
        ])

    t = Table(table_data, colWidths=[60, 140, 340])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#0B1220')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    # Deployment & Testing Reference
    story.append(Paragraph("4. Deployment & Automated Verification", h2_style))
    deploy_text = f"<b>Standalone Uvicorn Launch:</b><br/><code>cd {project_data['folder']}/src && python -m uvicorn server:app --host 127.0.0.1 --port {project_data['port']}</code><br/><br/><b>Automated Test Suite Execution:</b><br/><code>{project_data['test_cmd']}</code>"
    story.append(Paragraph(deploy_text, body_style))

    doc.build(story)
    print(f"[+] Successfully generated PDF: {pdf_path}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for proj in PROJECTS_PDF_DATA:
        build_pdf(proj, base_dir)

if __name__ == "__main__":
    main()
