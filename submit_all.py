import subprocess
import os

# List of problem IDs to submit
PROBLEMS = ["2276", "2277", "2278", "2279", "2280", "2281", "2282", "2283"]
TOKEN = os.environ.get("ACMOJ_TOKEN")
CLIENT_PATH = "submit_acmoj/acmoj_client.py"

def submit_problems():
    if not TOKEN:
        print("Error: ACMOJ_TOKEN environment variable not set.")
        return

    # Handle case where PROBLEMS might be a single comma-separated string
    if isinstance(PROBLEMS, str):
        problem_list = [p.strip() for p in PROBLEMS.split(",") if p.strip()]
    else:
        problem_list = PROBLEMS

    for pid in problem_list:
        # Ensure pid is a single problem ID string
        pid = pid.strip()
        if not pid:
            continue
            
        file_path = f"code/{pid}.mv"
        if not os.path.exists(file_path):
            print(f"Skipping {pid}: {file_path} not found.")
            continue
        
        print(f"Submitting problem {pid}...")
        cmd = [
            "python3", CLIENT_PATH,
            "--token", TOKEN,
            "submit",
            "--problem-id", pid,
            "--language", "mov",
            "--code-file", file_path
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Successfully submitted {pid}: {result.stdout}")
            else:
                print(f"Failed to submit {pid}: {result.stderr}")
        except Exception as e:
            print(f"An error occurred while submitting {pid}: {e}")

if __name__ == "__main__":
    submit_problems()
