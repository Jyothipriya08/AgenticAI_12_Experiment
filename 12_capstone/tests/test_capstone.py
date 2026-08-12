import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from capstone_agent import CapstoneAgenticSystem

def test_capstone_agent():
    system = CapstoneAgenticSystem()
    res = system.run_master_workflow("Show top products")
    assert res["safety_gate"] == "PASSED"
    assert len(res["trace"]) >= 4
    assert res["total_latency_ms"] >= 0.0
