"""Main entry point for Capstone End-to-End Agentic System."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from capstone_agent import CapstoneAgenticSystem

def main():
    print("=" * 60)
    print("   CAPSTONE: END-TO-END AGENTIC SYSTEM - PROJECT 12")
    print("=" * 60)

    system = CapstoneAgenticSystem()
    query = "Show all customers located in USA"

    print(f"[*] Executing Capstone Agentic System for query:\n    '{query}'...\n")
    res = system.run_master_workflow(query)

    print(res["final_answer"])

    print("\n" + "-" * 60)
    print("Observability Execution Trace:")
    for step in res["trace"]:
        print(f"  [{step['node']}] Action: {step['action']} | Latency: {step['latency_ms']}ms")

    print("\n[OK] Project 12 Capstone System execution finished successfully.")

if __name__ == "__main__":
    main()
