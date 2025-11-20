import json
import os
import sys
import time
from typing import List, Tuple, Optional

import cloudscraper
import requests
from bs4 import BeautifulSoup
from rich.console import Console

import CF_TC


console = Console()
console._log_render.omit_repeated_times = False

def parse_problem_limits(html: str):
    """
    Extracts time limit and memory limit from Codeforces problem HTML.
    
    Returns dict with:
    - time_limit: string (e.g., "2 seconds")
    - memory_limit: string (e.g., "256 megabytes")
    """
    soup = BeautifulSoup(html, "html.parser")
    
    limits = {
        "time_limit": None,
        "memory_limit": None
    }
    
    # Find the problem-statement div
    root = soup.find("div", class_="problem-statement")
    if not root:
        return limits
    
    # Look for the header div which contains time/memory limits
    header = root.find("div", class_="header")
    if not header:
        return limits
    
    # Find all divs with class "time-limit" and "memory-limit"
    time_limit_div = header.find("div", class_="time-limit")
    if time_limit_div:
        # Extract text, usually in format "time limit per test2 seconds"
        text = time_limit_div.get_text(strip=True)
        # Remove the label part
        if "time limit per test" in text.lower():
            limits["time_limit"] = text.split("time limit per test", 1)[-1].strip()
        else:
            limits["time_limit"] = text
    
    memory_limit_div = header.find("div", class_="memory-limit")
    if memory_limit_div:
        text = memory_limit_div.get_text(strip=True)
        if "memory limit per test" in text.lower():
            limits["memory_limit"] = text.split("memory limit per test", 1)[-1].strip()
        else:
            limits["memory_limit"] = text
    
    return limits


def save_limits(contest_id: str, problem_index: str, limits: dict) -> None:
    """
    Saves time and memory limits as JSON file in the problem directory.
    """
    base_dir = "problems"
    dir_name = os.path.join(base_dir, f"{contest_id}{problem_index}")
    ensure_dir(dir_name)
    
    limits_path = os.path.join(dir_name, "limits.json")
    with open(limits_path, "w", encoding="utf-8") as f:
        json.dump(limits, f, indent=2, ensure_ascii=False)
    
    console.log(f"Saved limits: {limits_path}")


# Update the process_problem function to include limits extraction
def process_problem(pvcodes: CF_TC.CF_TC, contest_id: str, problem_index: str) -> None:
    console.log(f"Processing problem {contest_id}{problem_index}")
    
    # Fetch testcases via existing scraper
    tc_res = pvcodes.get_testcases(contest_id, problem_index)
    if tc_res[0] and tc_res[1]:
        save_testcases(contest_id, problem_index, tc_res[1])
    else:
        console.log(f"Could not fetch system tests for {contest_id}{problem_index}: {tc_res[1]}")

    # Fetch statement via cloudscraper
    html = fetch_problem_html(contest_id, problem_index)
    if html:
        # Parse and save statement
        md = parse_problem_statement_and_io(html)
        save_description(contest_id, problem_index, md)
        
        # Parse and save limits
        limits = parse_problem_limits(html)
        save_limits(contest_id, problem_index, limits)
    else:
        console.log(f"Failed to fetch statement for {contest_id}{problem_index}")

def get_contest_problems(contest_id: str) -> List[str]:
    url = f"https://codeforces.com/api/contest.standings?contestId={contest_id}&from=1&count=1"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    if data.get("status") != "OK":
        raise RuntimeError("Codeforces API returned non-OK status")
    indices = [p.get("index") for p in data.get("result", {}).get("problems", [])]
    return indices


def create_scraper():
    return cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "windows", "mobile": False}
    )


def fetch_problem_html(contest_id: str, problem_index: str) -> Optional[str]:
    scraper = create_scraper()
    bases = [
        "https://codeforces.com/",
        "https://codeforces.net/",
        "https://m1.codeforces.com/",
    ]
    paths = [
        f"contest/{contest_id}/problem/{problem_index}",
        f"problemset/problem/{contest_id}/{problem_index}",
    ]
    variants = ["", "?locale=en", "?mobile=true", "?mobile=true&locale=en"]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Referer": "https://codeforces.com/",
    }
    for base in bases:
        for path in paths:
            for v in variants:
                url = f"{base}{path}{v}"
                try:
                    r = scraper.get(url, headers=headers, timeout=25)
                    r.raise_for_status()
                    if "Verify you are human" in r.text or "Just a moment" in r.text:
                        continue
                    return r.text
                except Exception:
                    continue
    return None


def parse_problem_statement_and_io(html: str):
    """
    Extracts only:
    - Problem description
    - Input specification
    - Output specification

    Returns Markdown string.
    """
    soup = BeautifulSoup(html, "html.parser")

    root = soup.find("div", class_="problem-statement")
    if not root:
        return "# Error: problem-statement block not found"

    # --- DESCRIPTION ---
    desc_block = []
    all_divs = root.find_all(recursive=False)

    # Description is the second div (after the header)
    if len(all_divs) >= 2:
        desc_div = all_divs[1]
        for p in desc_div.find_all("p"):
            desc_block.append(p.get_text(strip=True))

    # --- INPUT SPEC ---
    input_div = root.find("div", class_="input-specification")
    input_block = []
    if input_div:
        input_block.append("## Input")
        for p in input_div.find_all("p"):
            input_block.append(p.get_text(strip=True))

    # --- OUTPUT SPEC ---
    output_div = root.find("div", class_="output-specification")
    output_block = []
    if output_div:
        output_block.append("## Output")
        for p in output_div.find_all("p"):
            output_block.append(p.get_text(strip=True))

    # --- Assemble Markdown ---
    md = ["# Problem Description", ""]
    md.extend(desc_block)
    md.append("")
    md.extend(input_block)
    md.append("")
    md.extend(output_block)

    return "\n".join(md)




def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def save_description(contest_id: str, problem_index: str, markdown: str) -> None:
    base_dir = "problems"
    dir_name = os.path.join(base_dir, f"{contest_id}{problem_index}")
    ensure_dir(dir_name)
    statement_path = os.path.join(dir_name, "statement.md")
    with open(statement_path, "w", encoding="utf-8") as f:
        f.write(markdown)
    console.log(f"Saved statement: {statement_path}")


def save_testcases(contest_id: str, problem_index: str, tc):
    base_dir = "problems"
    dir_name = os.path.join(base_dir, f"{contest_id}{problem_index}")
    ensure_dir(dir_name)
    for i, (inp, out) in enumerate(tc, 1):
        tc_dir = os.path.join(dir_name, f"tc{i}")
        ensure_dir(tc_dir)
        with open(os.path.join(tc_dir, "input.txt"), "w", encoding="utf-8") as fi:
            fi.write(inp)
        with open(os.path.join(tc_dir, "output.txt"), "w", encoding="utf-8") as fo:
            fo.write(out)
    console.log(f"Saved {len(tc)} testcases under {dir_name}/")

def main():
    if len(sys.argv) < 2:
        console.print("Usage: python contest_fetch.py <contest_id> [--only A,B,C]")
        sys.exit(1)

    contest_id = str(sys.argv[1])
    only = None
    if len(sys.argv) >= 4 and sys.argv[2] == "--only":
        only = [x.strip() for x in sys.argv[3].split(",") if x.strip()]

    pvcodes = CF_TC.CF_TC()

    try:
        indices = get_contest_problems(contest_id)
    except Exception as e:
        console.log(f"[red]Failed to read problems from API:[/] {e}")
        sys.exit(1)

    if only:
        indices = [i for i in indices if i in only]

    console.log(f"Found {len(indices)} problems: {', '.join(indices)}")

    for idx in indices:
        try:
            process_problem(pvcodes, contest_id, idx)
        except Exception as e:
            console.log(f"[yellow]Problem {contest_id}{idx} failed:[/] {e}")
            continue

    console.log("Done.")


if __name__ == "__main__":
    main()


