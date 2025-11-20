import json
import os
import traceback
from rich.console import Console
import CF_TC

console = Console()
console._log_render.omit_repeated_times = False

INPUT_JSON = "problems.json"      # <-- your JSON file
OUTPUT_JSON = "problems_with_tc.json"  # <-- output file


def normalize_pid(pid: str):
    """Ensure problem id is uppercase (e.g., 'a' -> 'A')."""
    if pid.isalpha():
        return pid.upper()
    return pid


def save_tc(cid, pid, tc):
    """Save testcases exactly like main.py (no logging)."""
    directory = f"{cid}{pid}"

    if not os.path.exists(directory):
        os.mkdir(directory)

    for i, (inp, outp) in enumerate(tc, start=1):
        tc_dir = f"{directory}/tc{i}"
        if not os.path.exists(tc_dir):
            os.mkdir(tc_dir)

        with open(f"{tc_dir}/input.txt", "w") as f_in:
            f_in.write(inp)

        with open(f"{tc_dir}/output.txt", "w") as f_out:
            f_out.write(outp)


def main():
    pvcodes = CF_TC.CF_TC()

    with open(INPUT_JSON, "r") as f:
        problems = json.load(f)

    enriched = {}

    for pid_key, pdata in problems.items():
        contest, problem_letter = pid_key.split("-")
        problem_letter = normalize_pid(problem_letter)

        try:
            status, result = pvcodes.get_testcases(contest, problem_letter)

            if status is None:
                console.log(f"[yellow on red]Failed fetching {pid_key}: {result}")
                pdata["testcases"] = None
                enriched[pid_key] = pdata
                continue

            testcases = result
            pdata["testcases"] = [{"input": tc[0], "output": tc[1]} for tc in testcases]

            # Save locally with no logging
            if len(testcases) > 0:
                save_tc(contest, problem_letter, testcases)
            else:
                console.log(f"[yellow on red]No testcases found for {pid_key}")

            enriched[pid_key] = pdata

        except Exception as e:
            console.log(f"[yellow on red]Unexpected error for {pid_key}: {e}")
            console.print_exception()
            pdata["testcases"] = None
            enriched[pid_key] = pdata

    with open(OUTPUT_JSON, "w") as f:
        json.dump(enriched, f, indent=2)


if __name__ == "__main__":
    main()
