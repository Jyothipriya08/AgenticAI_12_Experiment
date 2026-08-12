"""Main entry point for Multi-Agent SDR System."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sdr_system import MultiAgentSDRSystem

def main():
    print("=" * 60)
    print("       MULTI-AGENT SDR SYSTEM - PROJECT 05")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    leads_file = os.path.join(base_dir, "data", "leads.json")

    sdr = MultiAgentSDRSystem(leads_file)
    target_leads = ["L101", "L102", "L103"]

    for idx, lead_id in enumerate(target_leads, 1):
        print(f"\n[{idx}] Processing Lead ID: {lead_id}")
        res = sdr.process_lead(lead_id, auto_approve=True)
        if res.get("status") == "DISQUALIFIED":
            print(f"    Status: {res['status']}")
            print(f"    Score: {res['qualification']['score']}")
            print(f"    Reason: {res['message']}")
        else:
            print(f"    Qualification Score: {res['qualification']['score']}/100")
            print(f"    Personalized Hook: {res['personalization']['personalized_hook']}")
            print(f"    Subject Line: {res['email_draft']['subject']}")
            print(f"    Human Approval Status: {res['approval_gate']['status']}")
            print(f"    Gate Action: {res['approval_gate']['action']}")
        print("-" * 60)

    print("\n[OK] Project 05 Multi-Agent SDR System execution finished successfully.")

if __name__ == "__main__":
    main()
