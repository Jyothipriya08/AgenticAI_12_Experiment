"""Main entry point for Model Optimization Experiment."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from optimizer import ModelOptimizer

def main():
    print("=" * 60)
    print("      MODEL OPTIMIZATION EXPERIMENT - PROJECT 11")
    print("=" * 60)

    optimizer = ModelOptimizer("Llama-3-8B-Instruct")
    print(f"[*] Running Precision & Quantization Benchmark on '{optimizer.model_name}'...\n")

    results = optimizer.run_optimization_experiment()

    header = f"{'Precision':<20} | {'VRAM (GB)':<10} | {'TTFT (ms)':<10} | {'Tok/sec':<10} | {'Perplexity':<10}"
    print(header)
    print("-" * len(header))
    for res in results:
        print(f"{res['precision']:<20} | {res['vram_gb']:<10.1f} | {res['latency_ttft_ms']:<10.1f} | {res['throughput_tok_per_sec']:<10.1f} | {res['perplexity']:<10.2f}")

    print("\n" + "=" * 60)
    report = optimizer.generate_tradeoff_report(results)
    print(report)

    print("\n[OK] Project 11 Model Optimization Experiment finished successfully.")

if __name__ == "__main__":
    main()
