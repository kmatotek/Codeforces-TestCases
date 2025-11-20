#!/usr/bin/env python3

import json
import os
import sys
from rich.console import Console

# Import the modules we need
import CF_TC
import contest_fetch as cf_fetch
from contest_fetch import parse_problem_statement_and_io

console = Console()
console._log_render.omit_repeated_times = False

JSON_PATH = "codeforces_problems_2025.json"
PROBLEM_ROOT = "problems"


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
    Return True if directory like: problems/2172L exists and has content.
    """
    dirname = f"{contest_id}{problem_index}"
    full_path = os.path.join(PROBLEM_ROOT, dirname)
    
    # Check if directory exists
    if not os.path.exists(full_path):
        return False
    
    # Check if it has statement.md (basic indicator of complete download)
    statement_path = os.path.join(full_path, "statement.md")
    return os.path.exists(statement_path)


def save_tc(cid, pid, tc):
    """Save test cases to files."""
    base_dir = PROBLEM_ROOT
    os.makedirs(base_dir, exist_ok=True)

    pth = os.path.join(base_dir, f"{cid}{pid}")
    if not os.path.exists(pth):
        os.mkdir(pth)

    n = len(tc)
    for i in range(n):
        tc_path = os.path.join(pth, f"tc{i+1}")
        os.makedirs(tc_path, exist_ok=True)

        with open(os.path.join(tc_path, "input.txt"), "w") as input_f:
            input_f.write(tc[i][0])
        
        with open(os.path.join(tc_path, "output.txt"), "w") as output_f:
            output_f.write(tc[i][1])

        console.log(f"Saved test case: {tc_path}/")


def fetch_problem(pvcodes, contest_id: str, problem_index: str) -> bool:
    """
    Fetch a single problem: test cases, statement, and limits.
    Returns True if successful, False otherwise.
    """
    try:
        console.log(f"Fetching test cases for {contest_id}{problem_index}...")
        
        # Fetch test cases
        with console.status("[Working on fetching test cases]", spinner="aesthetic"):
            res = pvcodes.get_testcases(contest_id, problem_index)
        
        if res[0] is None:
            console.log(f"[yellow]{res[1]}[/]")
            return False
        
        tc_list = res[1]
        n = len(tc_list)
        
        if n > 0:
            # Save test cases
            save_tc(contest_id, problem_index, tc_list)
            console.log(f"[green]Saved {n} test cases[/]")
            
            # Fetch and save problem statement + limits
            try:
                console.log(f"Fetching problem statement for {contest_id}{problem_index}...")
                page_html = pvcodes.fetch_problem_html_selenium(contest_id, problem_index)
                
                if page_html:
                    # Save statement as markdown
                    md = parse_problem_statement_and_io(page_html)
                    cf_fetch.save_description(contest_id, problem_index, md)
                    console.log(f"[green]Saved problem statement[/]")
                    
                    # Extract and save limits as JSON
                    limits = cf_fetch.parse_problem_limits(page_html)
                    cf_fetch.save_limits(contest_id, problem_index, limits)
                    console.log(f"[green]Saved limits: {limits}[/]")
                else:
                    console.log(f"[yellow]Failed to fetch statement for {contest_id}{problem_index}[/]")
                    return False
                    
            except Exception as e:
                console.log(f"[red]Error fetching statement: {e}[/]")
                return False
        else:
            console.log("[red]Not enough test cases found![/]")
            return False
        
        return True
        
    except Exception as e:
        console.log(f"[red]Error processing {contest_id}{problem_index}: {e}[/]")
        return False


def main():
    if not os.path.exists(JSON_PATH):
        console.log(f"[red]Could not find {JSON_PATH}![/]")
        return

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        problems = json.load(f)

    console.log(f"Loaded {len(problems)} problems from JSON.")
    
    # Initialize the scraper once for all problems
    console.log("Initializing Codeforces scraper...")
    pvcodes = CF_TC.CF_TC()
    
    try:
        success_count = 0
        skip_count = 0
        fail_count = 0
        
        for idx, (key, entry) in enumerate(problems.items(), 1):
            try:
                contest_id, problem_index = parse_key(key)
            except ValueError as e:
                console.log(f"[yellow]Skipping invalid key {key}: {e}[/]")
                fail_count += 1
                continue

            # Skip if directory already exists with statement
            if already_downloaded(contest_id, problem_index):
                console.log(f"[dim]({idx}/{len(problems)}) Skipping {contest_id}{problem_index} (already exists)[/]")
                skip_count += 1
                continue

            console.rule(f"[bold blue]({idx}/{len(problems)}) Fetching {contest_id}{problem_index}[/]")

            if fetch_problem(pvcodes, contest_id, problem_index):
                console.log(f"[green]✓ Successfully fetched {contest_id}{problem_index}[/]")
                success_count += 1
            else:
                console.log(f"[red]✗ Failed to fetch {contest_id}{problem_index}[/]")
                fail_count += 1
        
        # Summary
        console.rule("[bold green]Summary[/]")
        console.log(f"[green]Successful: {success_count}[/]")
        console.log(f"[yellow]Skipped: {skip_count}[/]")
        console.log(f"[red]Failed: {fail_count}[/]")
        console.log(f"Total: {len(problems)}")
        
    finally:
        # Close the browser
        console.log("Closing browser...")
        pvcodes.close()


if __name__ == "__main__":
    main()