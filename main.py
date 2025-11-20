#main.py
import CF_TC
import contest_fetch as cf_fetch
import os, time, sys, json

from rich.console import Console
from contest_fetch import parse_problem_statement_and_io

console = Console()
console._log_render.omit_repeated_times = False


# Helper Function
def check_pid(pid):
    if pid.isalpha():
        pid = pid.upper()
    elif pid.isnumeric():
        pid = "A" + pid - 1
    # print(pid)
    return pid


def save_tc(cid, pid, tc):
    base_dir = "problems"
    os.makedirs(base_dir, exist_ok=True)

    pth = os.path.join(base_dir, f"{cid}{pid}")

    # make a dir for that problem
    if not os.path.exists(pth):
        os.mkdir(pth)

    # save all TCs in sep files
    n = len(tc)
    for i in range(n):
        tc_path = os.path.join(pth, f"tc{i+1}")
        os.makedirs(tc_path, exist_ok=True)

        input_f = open(os.path.join(tc_path, "input.txt"), "w")
        output_f = open(os.path.join(tc_path, "output.txt"), "w")

        console.log(f"Successfully created file: {tc_path}/input.txt and output.txt")

        input_f.write(tc[i][0])
        output_f.write(tc[i][1])



pvcodes = CF_TC.CF_TC()

# Support CLI args or ENV for non-interactive runs
cid = None
pid = None
if len(sys.argv) >= 3:
    cid = str(sys.argv[1])
    pid = str(sys.argv[2])
else:
    cid = os.getenv("CF_CID")
    pid = os.getenv("CF_PID")

if not cid:
    cid = console.input("Enter the [bold green]Contest ID[/]: ")
if not pid:
    pid = console.input("Enter the [bold green]problem index[/] [A-G]: ")

# res return a tuple of (status, TCs) if status is True, else (None, error_msg)
pid = check_pid(pid)

with console.status(" : [Working on fetching of TCs]\n", spinner="aesthetic"):
    res = pvcodes.get_testcases(cid, pid)
# print(res)

if res[0] is None:
    console.log(f"[yellow on red]{res[1]}")
    exit()

res = res[1]

n = len(res)
# print(n)

if n > 0:
    save_tc(cid, pid, res)
    # Also fetch and save the problem statement (Markdown + original HTML + limits)
    try:
        page_html = pvcodes.fetch_problem_html_selenium(cid, pid)
        if page_html:
            # Save statement as markdown
            md = cf_fetch.parse_problem_statement_and_io(page_html)
            cf_fetch.save_description(cid, pid, md)
            
            # Save original HTML if you have that function
            # cf_fetch.save_description_html(cid, pid, page_html)
            
            # Extract and save limits as JSON
            limits = cf_fetch.parse_problem_limits(page_html)
            cf_fetch.save_limits(cid, pid, limits)
        else:
            console.log(f"Failed to fetch statement for {cid}{pid}")
    except Exception as e:
        console.log(f"Error while fetching/saving statement for {cid}{pid}: {e}")
else:
    console.log("Not enough TCs found! Please try later!", style="red on white")