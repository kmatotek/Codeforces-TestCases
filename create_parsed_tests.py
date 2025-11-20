import os
import json

# path to your metadata json
METADATA = "codeforces_problems_2025.json"

# root directory where your scraped contests are stored
TEST_ROOT = "."        # adjust to your directory structure
OUTFILE = "parsed_test.json"


def load_metadata():
    with open(METADATA, "r", encoding="utf8") as f:
        return json.load(f)


def load_testcases(problem_dir):
    """
    Read all tc folders under something like:
       2172L/tc1/input.txt
       2172L/tc1/output.txt
    Returns list of dicts: [{"input": "...", "output": "..."}, ...]
    """
    tcs = []
    for name in sorted(os.listdir(problem_dir)):
        if not name.startswith("tc"):
            continue
        tc_path = os.path.join(problem_dir, name)

        inp = os.path.join(tc_path, "input.txt")
        out = os.path.join(tc_path, "output.txt")

        if not (os.path.exists(inp) and os.path.exists(out)):
            continue

        with open(inp, "r", encoding="utf8") as fi:
            input_text = fi.read().rstrip("\n")

        with open(out, "r", encoding="utf8") as fo:
            output_text = fo.read().rstrip("\n")

        tcs.append({"input": input_text, "output": output_text})

    return tcs


def main():
    metadata = load_metadata()
    parsed = {}

    for pid, info in metadata.items():
        # Example: "2172-L" -> directory "2172L"
        contest_problem_id = pid.replace("-", "")
        problem_dir = os.path.join(TEST_ROOT, contest_problem_id)

        if not os.path.exists(problem_dir):
            continue

        tcs = load_testcases(problem_dir)
        if len(tcs) == 0:
            continue

        # key should be a readable slug or id; you choose one.
        # example uses problem title lowercased without spaces.
        slug = info.get("title", pid).lower().replace(" ", "")

        parsed[slug] = tcs

    with open(OUTFILE, "w", encoding="utf8") as f:
        json.dump(parsed, f, indent=2, ensure_ascii=False)

    print(f"Saved parsed tests → {OUTFILE}")


if __name__ == "__main__":
    main()
