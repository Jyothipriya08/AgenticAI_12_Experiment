"""FastAPI web server for Reasoning Model Benchmarking powered by Google Gemini 2.5 Flash."""
import os
import sys
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from benchmark_suite import ReasoningBenchmarkSuite

app = FastAPI(title="Reasoning Benchmark AI Studio", version="1.0.0")

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
problems_file = os.path.join(base_dir, "data", "problems.json")

suite = ReasoningBenchmarkSuite(problems_file)

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_file = os.path.join(static_dir, "index.html")
    if os.path.exists(html_file):
        return FileResponse(html_file)
    return HTMLResponse("<h2>Reasoning Benchmark Web App</h2>")

@app.get("/api/benchmark")
def run_benchmark_api():
    return {"results": suite.run_benchmark()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8009)
