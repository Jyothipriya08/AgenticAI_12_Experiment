import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from chain import PromptChainingSummarizer

def test_prompt_chaining_pipeline():
    summarizer = PromptChainingSummarizer()
    text = "Artificial intelligence models require careful prompt engineering. Multi-stage prompt chains significantly boost accuracy and reduce hallucinations."
    results = summarizer.run_chain(text)

    assert "cleaned_text" in results
    assert len(results["facts"]) > 0
    assert len(results["draft_summary"]) > 0
    assert results["critique"]["score"] > 0
    assert len(results["final_summary"]) > 0
