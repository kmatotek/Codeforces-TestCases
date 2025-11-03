import json
import os
import signal
import sys
import time
from typing import Dict, List, Tuple, Optional

import requests
from rich.console import Console

import CF_TC
from contest_fetch import fetch_problem_html, parse_problem_markdown


console = Console()
console._log_render.omit_repeated_times = False


def get_all_finished_contests() -> List[int]:
    url = "https://codeforces.com/api/contest.list?gym=false"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    data = r.json()
    if data.get("status") != "OK":
        raise RuntimeError("contest.list returned non-OK status")
    contests = [c for c in data.get("result", []) if c.get("phase") == "FINISHED"]
    # Oldest first for stability
    contests.sort(key=lambda c: c.get("id"))
    return [c.get("id") for c in contests]


def get_contest_problems(contest_id: int) -> List[str]:
    url = f"https://codeforces.com/api/contest.standings?contestId={contest_id}&from=1&count=1"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    data = r.json()
    if data.get("status") != "OK":
        return []
    return [p.get("index") for p in data.get("result", {}).get("problems", [])]


def load_progress(path: str) -> Dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"version": 1, "contests": {}}


def save_progress(path: str, prog: Dict) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(prog, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def problem_dir(base_dir: str, contest_id: int, problem_index: str) -> str:
    return os.path.join(base_dir, "contests", str(contest_id), problem_index)


def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def save_statement(path_dir: str, markdown: str) -> None:
    ensure_dir(path_dir)
    with open(os.path.join(path_dir, "statement.md"), "w", encoding="utf-8") as f:
        f.write(markdown)


def save_tests(path_dir: str, testcases: List[Tuple[str, str]]) -> None:
    tests_root = os.path.join(path_dir, "tests", "system")
    ensure_dir(tests_root)
    for i, (inp, out) in enumerate(testcases, 1):
        tc_dir = os.path.join(tests_root, f"tc{i}")
        ensure_dir(tc_dir)
        with open(os.path.join(tc_dir, "input.txt"), "w", encoding="utf-8") as fi:
            fi.write(inp)
        with open(os.path.join(tc_dir, "output.txt"), "w", encoding="utf-8") as fo:
            fo.write(out)


def already_done(path_dir: str) -> bool:
    # Consider a problem done if statement.md exists and at least one tc exists
    stm = os.path.join(path_dir, "statement.md")
    tests_root = os.path.join(path_dir, "tests", "system")
    if not os.path.exists(stm):
        return False
    if not os.path.exists(tests_root):
        return False
    # any tc subdir
    for name in os.listdir(tests_root):
        if name.startswith("tc"):
            return True
    return False


stop_requested = False


def _handle_sigint(signum, frame):
    global stop_requested
    stop_requested = True
    console.log("Stop requested. Will finish current item and persist progress…")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Download all Codeforces contests (statements + tests)")
    parser.add_argument("--out", default="data", help="Output directory root (default: data)")
    parser.add_argument("--from_id", type=int, default=None, help="Start from this contest id (inclusive)")
    parser.add_argument("--max", type=int, default=None, help="Max number of contests to process")
    parser.add_argument("--only", type=str, default=None, help="Comma-separated problem indices to include (e.g., A,B)")
    args = parser.parse_args()

    out_root = args.out
    progress_path = os.path.join(out_root, "progress.json")
    ensure_dir(out_root)

    prog = load_progress(progress_path)

    signal.signal(signal.SIGINT, _handle_sigint)

    contests = get_all_finished_contests()
    if args.from_id is not None:
        contests = [c for c in contests if c >= args.from_id]
    if args.max is not None:
        contests = contests[: args.max]

    only_set = None
    if args.only:
        only_set = {x.strip() for x in args.only.split(",") if x.strip()}

    pvcodes = CF_TC.CF_TC()

    for cid in contests:
        if stop_requested:
            break

        console.log(f"Contest {cid}")
        problems = get_contest_problems(cid)
        if only_set:
            problems = [p for p in problems if p in only_set]
        if not problems:
            continue

        prog.setdefault("contests", {}).setdefault(str(cid), {})

        for idx in problems:
            if stop_requested:
                break

            pdir = problem_dir(out_root, cid, idx)
            entry = prog["contests"][str(cid)].setdefault(idx, {"statement": False, "tests": False})

            if already_done(pdir):
                entry["statement"] = True
                entry["tests"] = True
                continue

            console.log(f"  Problem {cid}{idx}")

            # Tests first (reuses Selenium scraper)
            try:
                tc_res = pvcodes.get_testcases(cid, idx)
                if tc_res[0] and tc_res[1]:
                    save_tests(pdir, tc_res[1])
                    entry["tests"] = True
                else:
                    console.log(f"    Tests unavailable: {tc_res[1]}")
            except Exception as e:
                console.log(f"    Tests failed: {e}")

            # Statement via cloudscraper
            try:
                html = fetch_problem_html(str(cid), idx)
                if html:
                    md = parse_problem_markdown(html)
                    save_statement(pdir, md)
                    entry["statement"] = True
                else:
                    console.log("    Statement fetch failed (blocked or unavailable)")
            except Exception as e:
                console.log(f"    Statement failed: {e}")

            save_progress(progress_path, prog)
            time.sleep(0.5)

        save_progress(progress_path, prog)

    save_progress(progress_path, prog)
    console.log("Done.")


if __name__ == "__main__":
    main()


