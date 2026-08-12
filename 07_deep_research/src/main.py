"""Main entry point for Deep Research Agent Workflow."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from research_agent import DeepResearchAgent

def main():
    print("=" * 60)
    print("      DEEP RESEARCH AGENT WORKFLOW - PROJECT 07")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    corpus_file = os.path.join(base_dir, "data", "web_corpus.json")

    agent = DeepResearchAgent(corpus_file)
    topic = "Next-Generation LLM Architectures and Scaling Dynamics"

    print(f"[*] Starting Deep Research on topic: '{topic}'...\n")
    res = agent.execute_deep_research(topic)

    print("Research Sub-Questions Plan:")
    for idx, q in enumerate(res["plan"], 1):
        print(f"  {idx}. {q}")

    print(f"\nCollected {res['evidence_count']} evidence snippets.")
    print(f"Reflection Completeness Score: {res['reflection']['completeness_score']}/100")

    print("\n" + "=" * 60)
    print("FINAL SYNTHESIZED REPORT:")
    print("=" * 60)
    print(res["final_report"])

    print("\n[OK] Project 07 Deep Research Workflow execution finished successfully.")

if __name__ == "__main__":
    main()
