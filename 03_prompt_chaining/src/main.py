"""Main entry point for Prompt Chaining for Summarization."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chain import PromptChainingSummarizer

def main():
    print("=" * 60)
    print("   PROMPT CHAINING FOR SUMMARIZATION - PROJECT 03")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sample_file = os.path.join(base_dir, "data", "sample_article.txt")

    if os.path.exists(sample_file):
        with open(sample_file, "r", encoding="utf-8") as f:
            article_text = f.read()
    else:
        article_text = "Prompt chaining decomposes complex tasks into smaller sub-prompts, dramatically reducing error rates."

    summarizer = PromptChainingSummarizer()
    print("[*] Stepping through 6-Stage Prompt Chain...\n")
    results = summarizer.run_chain(article_text)

    print("Stage 1 (Cleaned Text Length):", len(results["cleaned_text"]))
    print("\nStage 2 (Extracted Facts):")
    for fact in results["facts"]:
        print(f"  - {fact}")

    print("\nStage 3 (Structured Outline):")
    print(results["outline"])

    print("\nStage 4 (Draft Summary):")
    print(results["draft_summary"])

    print("\nStage 5 (Critique Feedback):")
    print(f"  Score: {results['critique']['score']}/100")
    print(f"  Notes: {results['critique']['feedback']}")

    print("\nStage 6 (Final Summary):")
    print(results["final_summary"])

    print("\n" + "=" * 60)
    print("[OK] Project 03 Prompt Chaining execution finished successfully.")

if __name__ == "__main__":
    main()
