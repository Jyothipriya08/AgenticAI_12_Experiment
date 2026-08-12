import json
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from visual_qa_engine import VisualQAEngine

@pytest.fixture
def catalog_file(tmp_path):
    p = tmp_path / "test_cat.json"
    data = [
        {
            "image_id": "T1",
            "filename": "chart.png",
            "tags": ["sales", "chart"],
            "description": "Sales chart description",
            "extracted_text": "Revenue: $100k"
        }
    ]
    p.write_text(json.dumps(data), encoding="utf-8")
    return str(p)

def test_visual_qa_retrieval(catalog_file):
    engine = VisualQAEngine(catalog_file)
    res = engine.answer_visual_question("What is the sales revenue?")
    assert len(res["retrieved_images"]) > 0
    assert "$100k" in res["answer"]
