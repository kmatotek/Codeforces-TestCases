#!/usr/bin/env python3

import json
import subprocess
import os
from rich.console import Console

console = Console()

JSON_PATH = "codeforces_problems_2025.json"
MAIN_SCRIPT = "main.py"
PROBLEM_ROOT = "problems"   # adjust if yours is different


def parse_key(key: str):
    """
    Convert '2172-L' → ('2172', 'L')
    """
    if "-" not in key:
        raise ValueError(f"Invalid key format: {key}")
    contest, letter = key.split("-", 1)
    return contest, letter


def already_downloaded(contest_id: str, problem_index: str) -> bool:
    """
    Return True if directory like: problems/2172L exists.
    """
    dirname = f"{contest_id}{problem_index}"
    full_path = os.path.join(PROBLEM_ROOT, dirname)
    return os.path.exists(full_path)


def main():
    if not os.path.exists(JSON_PATH):
        console.log(f"[red]Could not find {JSON_PATH}![/]")
        return

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        problems = json.load(f)

    console.log(f"Loaded {len(problems)} problems from JSON.")

    for key, entry in problems.items():
        try:
            contest_id, problem_index = parse_key(key)
        except ValueError as e:
            console.log(f"[yellow]Skipping invalid key {key}: {e}[/]")
            continue

        # 🆕 SKIP if directory already exists
        if already_downloaded(contest_id, problem_index):
            console.log(f"[green]Skipping {contest_id}{problem_index} (already exists)[/]")
            continue

        console.rule(f"[bold blue]Fetching {contest_id}{problem_index}[/]")

        cmd = [
            "python3",
            MAIN_SCRIPT,
            contest_id,
            problem_index
        ]

        result = subprocess.run(cmd)
        if result.returncode != 0:
            console.log(f"[red]Failed to fetch {contest_id}{problem_index}[/]")
        else:
            console.log(f"[green]Done: {contest_id}{problem_index}[/]")


if __name__ == "__main__":
    main()
