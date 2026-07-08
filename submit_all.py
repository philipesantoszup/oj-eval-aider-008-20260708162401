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

    # Normalize PROBLEMS into a list of strings
    problem_list = []
    if isinstance(PROBLEMS, str):
        problem_list = [p.strip() for p in PROBLEMS.split(",") if p.strip()]
    elif isinstance(PROBLEMS, list):
        for item in PROBLEMS:
            if isinstance(item, str) and ',' in item:
                problem_list.extend([p.strip() for p in item.split(",") if p.strip()])
            else:
                problem_list.append(str(item))

    for pid in problem_list:
        submit_single_problem(pid)

def submit_single_problem(pid):
    if not pid:
        return
    
    file_path = f"code/{pid}.mv"
    if not os.path.exists(file_path):
        print(f"Skipping {pid}: {file_path} not found.")
        return
    
    print(f"Submitting problem {pid}...")
    cmd = [
        "python3", CLIENT_PATH,
        "--token", TOKEN,
        "submit",
        "--problem-id", str(pid),
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
