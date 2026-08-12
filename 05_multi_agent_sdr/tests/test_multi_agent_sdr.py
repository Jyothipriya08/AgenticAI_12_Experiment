import json
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from sdr_system import MultiAgentSDRSystem

@pytest.fixture
def leads_file(tmp_path):
    p = tmp_path / "test_leads.json"
    data = [
        {
            "lead_id": "L99",
            "company": "Acme Test Corp",
            "contact_name": "John Doe",
            "title": "CTO",
            "industry": "Software",
            "company_size": 200,
            "tech_stack": ["Python", "AWS"],
            "recent_news": "Acquired new AI venture"
        }
    ]
    p.write_text(json.dumps(data), encoding="utf-8")
    return str(p)

def test_sdr_workflow(leads_file):
    sdr = MultiAgentSDRSystem(leads_file)
    res = sdr.process_lead("L99", auto_approve=True)
    assert res["lead_id"] == "L99"
    assert res["qualification"]["score"] >= 60
    assert res["approval_gate"]["status"] == "APPROVED"
    assert "John Doe" in res["email_draft"]["body"]

def test_sdr_approval_rejection(leads_file):
    sdr = MultiAgentSDRSystem(leads_file)
    res = sdr.process_lead("L99", auto_approve=False)
    assert res["approval_gate"]["status"] == "REJECTED"
