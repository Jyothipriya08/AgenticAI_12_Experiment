import json
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from research_agent import DeepResearchAgent

@pytest.fixture
def corpus_file(tmp_path):
    p = tmp_path / "test_corpus.json"
    data = [
        {"url": "https://test.com", "title": "Test Title", "snippet": "Test snippet with scaling and agentic info."}
    ]
    p.write_text(json.dumps(data), encoding="utf-8")
    return str(p)

def test_deep_research_flow(corpus_file):
    agent = DeepResearchAgent(corpus_file)
    res = agent.execute_deep_research("AI Agents")
    assert len(res["plan"]) == 3
    assert res["evidence_count"] > 0
    assert res["reflection"]["completeness_score"] > 0
    assert "# Deep Research Report" in res["final_report"]
