"""Master multi-server launcher to run all 12 separate UI project backends on ports 8001..8012 simultaneously."""
import subprocess
import os
import sys
import time

PROJECTS = [
    ("01_text_to_sql", 8001),
    ("02_rag_qa", 8002),
    ("03_prompt_chaining", 8003),
    ("04_sql_agent", 8004),
    ("05_multi_agent_sdr", 8005),
    ("06_policy_compliance", 8006),
    ("07_deep_research", 8007),
    ("08_visual_qa", 8008),
    ("09_reasoning_benchmark", 8009),
    ("10_fine_tuning", 8010),
    ("11_model_optimization", 8011),
    ("12_capstone", 8012)
]

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    processes = []
    
    print("=" * 70)
    print("  LAUNCHING ALL 12 SEPARATE PROJECT UIs (PORTS 8001 - 8012)")
    print("  POWERED BY GOOGLE GEMINI 2.5 FLASH")
    print("=" * 70)

    for project, port in PROJECTS:
        src_dir = os.path.join(base_dir, project, "src")
        server_script = os.path.join(src_dir, "server.py")
        if os.path.exists(server_script):
            cmd = [sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", str(port)]
            p = subprocess.Popen(cmd, cwd=src_dir)
            processes.append((project, port, p))
            print(f"  [+] Launched {project} UI -> http://127.0.0.1:{port}")
        else:
            print(f"  [-] Missing server script for {project}")

    print("\nAll 12 project UI servers are live!")
    print("Press Ctrl+C to stop all servers.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping all servers...")
        for name, port, p in processes:
            p.terminate()

if __name__ == "__main__":
    main()
