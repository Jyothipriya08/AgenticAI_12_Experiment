"""FastAPI web server for Capstone End-to-End Agentic System powered by Google Gemini 2.5 Flash."""
import os
import sys
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from capstone_agent import CapstoneAgenticSystem

app = FastAPI(title="Capstone End-to-End Agentic AI Studio", version="1.0.0")

system = CapstoneAgenticSystem()

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

class CapstoneQuery(BaseModel):
    query: str

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_file = os.path.join(static_dir, "index.html")
    if os.path.exists(html_file):
        return FileResponse(html_file)
    return HTMLResponse("<h2>Capstone End-to-End Agentic System</h2>")

@app.post("/api/run-capstone")
def run_capstone_workflow(req: CapstoneQuery):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    result = system.run_master_workflow(req.query.strip())
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8012)
