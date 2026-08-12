"""FastAPI web server for Visual QA System powered by Google Gemini 2.5 Flash."""
import os
import sys
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from visual_qa_engine import VisualQAEngine

app = FastAPI(title="Visual QA AI Studio", version="1.0.0")

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
catalog_file = os.path.join(base_dir, "data", "sample_catalog.json")

engine = VisualQAEngine(catalog_file)

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

class VisualQuery(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_file = os.path.join(static_dir, "index.html")
    if os.path.exists(html_file):
        return FileResponse(html_file)
    return HTMLResponse("<h2>Visual QA Web App</h2>")

@app.post("/api/visual-qa")
def execute_visual_qa(req: VisualQuery):
    if not req.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    res = engine.answer_visual_question(req.question.strip())
    return res

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8008)
