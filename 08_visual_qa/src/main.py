"""Main entry point for Visual QA System."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from visual_qa_engine import VisualQAEngine

def main():
    print("=" * 60)
    print("      IMAGE RETRIEVAL / VISUAL QA SYSTEM - PROJECT 08")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    catalog_file = os.path.join(base_dir, "data", "sample_catalog.json")

    engine = VisualQAEngine(catalog_file)

    sample_questions = [
        "What was the total sales revenue reported in Q4 2023?",
        "What database is used in the AWS architecture diagram?",
        "What is the model number and serial number of the smart home hub product?"
    ]

    for idx, q in enumerate(sample_questions, 1):
        print(f"\n[{idx}] Question: '{q}'")
        res = engine.answer_visual_question(q)
        print(f"    Answer: {res['answer']}")
        if res["retrieved_images"]:
            print(f"    Retrieved Asset: {res['retrieved_images'][0]['filename']} ({res['retrieved_images'][0]['image_id']})")
        print("-" * 60)

    print("\n[OK] Project 08 Visual QA execution finished successfully.")

if __name__ == "__main__":
    main()
