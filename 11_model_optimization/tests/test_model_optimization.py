import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from optimizer import ModelOptimizer

def test_model_optimizer():
    opt = ModelOptimizer()
    results = opt.run_optimization_experiment()
    assert len(results) == 3
    assert results[0]["vram_gb"] > results[2]["vram_gb"]
    report = opt.generate_tradeoff_report(results)
    assert "Engineering Trade-Off Report" in report
