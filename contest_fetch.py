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


def parse_problem_markdown(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    root = soup.select_one("div.problem-statement")
    if not root:
        # Fallback: return whole page text if structure not found
        return soup.get_text("\n", strip=False)

    def text_of(sel: str) -> Optional[str]:
        el = root.select_one(sel)
        return el.get_text("\n", strip=False) if el else None

    title = text_of("div.header .title") or ""
    time_limit = text_of("div.header .time-limit") or ""
    memory_limit = text_of("div.header .memory-limit") or ""
    statement_parts = []
    # The statement paragraphs are usually direct children except sections; capture generously
    for p in root.select(
        ".header ~ p, .header ~ div:not(.input-specification):not(.output-specification):not(.sample-test):not(.note) p"
    ):
        statement_parts.append(p.get_text("\n", strip=False))
    statement = "\n\n".join([s for s in statement_parts if s.strip()])

    input_spec = text_of("div.input-specification") or ""
    output_spec = text_of("div.output-specification") or ""

    # Examples
    examples = []
    sample = root.select_one("div.sample-test") or root.select_one("div.sample-tests")
    if sample:
        ins = sample.select("div.input pre, .input pre")
        outs = sample.select("div.output pre, .output pre")
        for i_pre, o_pre in zip(ins, outs):
            examples.append((i_pre.get_text("\n", strip=False), o_pre.get_text("\n", strip=False)))

    notes = text_of("div.note") or ""

    # Build Markdown
    md = []
    if title:
        md.append(f"# {title}")
    if time_limit or memory_limit:
        md.append(f"- Time limit: {time_limit}\n- Memory limit: {memory_limit}")
    if statement:
        md.append("\n## Statement\n" + statement)
    if input_spec:
        md.append("\n## Input\n" + input_spec)
    if output_spec:
        md.append("\n## Output\n" + output_spec)
    if examples:
        md.append("\n## Examples")
        for idx, (inp, out) in enumerate(examples, 1):
            md.append(f"\n### Example {idx}\nInput:\n\n```\n{inp}\n```\n\nOutput:\n\n```\n{out}\n```")
    if notes:
        md.append("\n## Notes\n" + notes)

    return "\n\n".join(md).strip() + "\n"


def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def save_description(contest_id: str, problem_index: str, markdown: str) -> None:
    dir_name = f"{contest_id}{problem_index}"
    ensure_dir(dir_name)
    statement_path = os.path.join(dir_name, "statement.md")
    with open(statement_path, "w", encoding="utf-8") as f:
        f.write(markdown)
    console.log(f"Saved statement: {statement_path}")


def save_testcases(contest_id: str, problem_index: str, tc: List[Tuple[str, str]]) -> None:
    dir_name = f"{contest_id}{problem_index}"
    ensure_dir(dir_name)
    for i, (inp, out) in enumerate(tc, 1):
        tc_dir = os.path.join(dir_name, f"tc{i}")
        ensure_dir(tc_dir)
        with open(os.path.join(tc_dir, "input.txt"), "w", encoding="utf-8") as fi:
            fi.write(inp)
        with open(os.path.join(tc_dir, "output.txt"), "w", encoding="utf-8") as fo:
            fo.write(out)
    console.log(f"Saved {len(tc)} testcases under {dir_name}/")


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
        md = parse_problem_markdown(html)
        save_description(contest_id, problem_index, md)
    else:
        console.log(f"Failed to fetch statement for {contest_id}{problem_index}")


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


