"""Main entry point for Reasoning Model Benchmarking."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from benchmark_suite import ReasoningBenchmarkSuite

def main():
    print("=" * 60)
    print("      REASONING MODEL BENCHMARKING - PROJECT 09")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    problems_file = os.path.join(base_dir, "data", "problems.json")

    suite = ReasoningBenchmarkSuite(problems_file)
    print(f"[*] Running benchmark suite over {len(suite.problems)} reasoning problems...\n")

    results = suite.run_benchmark()

    header = f"{'Strategy':<20} | {'Accuracy':<10} | {'Avg Latency (ms)':<18} | {'Tokens':<10}"
    print(header)
    print("-" * len(header))
    for res in results:
        print(f"{res['strategy']:<20} | {res['accuracy']:<9.1f}% | {res['avg_latency_ms']:<18.2f} | {res['total_tokens']:<10}")

    print("\n[OK] Project 09 Reasoning Model Benchmarking finished successfully.")

if __name__ == "__main__":
    main()
