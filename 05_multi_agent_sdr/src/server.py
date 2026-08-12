"""FastAPI web server for Multi-Agent SDR System powered by Google Gemini 2.5 Flash."""
import os
import sys
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sdr_system import MultiAgentSDRSystem

app = FastAPI(title="Multi-Agent SDR System AI Studio", version="1.0.0")

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
leads_file = os.path.join(base_dir, "data", "leads.json")

sdr = MultiAgentSDRSystem(leads_file)

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

class LeadProcessRequest(BaseModel):
    lead_id: str
    auto_approve: bool = True

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_file = os.path.join(static_dir, "index.html")
    if os.path.exists(html_file):
        return FileResponse(html_file)
    return HTMLResponse("<h2>Multi-Agent SDR Web App</h2>")

@app.get("/api/leads")
def get_leads():
    return {"leads": sdr.leads}

@app.post("/api/process-lead")
def process_lead(req: LeadProcessRequest):
    res = sdr.process_lead(req.lead_id, auto_approve=req.auto_approve)
    return res

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8005)
