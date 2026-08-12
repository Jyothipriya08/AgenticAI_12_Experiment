"""FastAPI web server for Model Optimization Experiment powered by Google Gemini 2.5 Flash."""
import os
import sys
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from optimizer import ModelOptimizer

app = FastAPI(title="Model Optimization AI Studio", version="1.0.0")

optimizer = ModelOptimizer("Gemini-2.5-Flash")

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_file = os.path.join(static_dir, "index.html")
    if os.path.exists(html_file):
        return FileResponse(html_file)
    return HTMLResponse("<h2>Model Optimization Web App</h2>")

@app.get("/api/run-optimization")
@app.post("/api/run-optimization")
def run_optimization_api():
    results = optimizer.run_optimization_experiment()
    report = optimizer.generate_tradeoff_report(results)
    return {"results": results, "report": report}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8011)
