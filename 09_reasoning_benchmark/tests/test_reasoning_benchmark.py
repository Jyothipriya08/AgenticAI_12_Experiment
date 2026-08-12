import json
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from benchmark_suite import ReasoningBenchmarkSuite

@pytest.fixture
def prob_file(tmp_path):
    p = tmp_path / "test_p.json"
    data = [{"id": "1", "category": "Math", "question": "1+1?", "expected_answer": "2"}]
    p.write_text(json.dumps(data), encoding="utf-8")
    return str(p)

def test_benchmark_suite(prob_file):
    suite = ReasoningBenchmarkSuite(prob_file)
    results = suite.run_benchmark()
    assert len(results) == 4
    for r in results:
        assert r["accuracy"] == 100.0
        assert r["avg_latency_ms"] > 0
