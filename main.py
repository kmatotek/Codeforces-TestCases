import CF_TC
import os, time, sys

from rich.console import Console

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
else:
    console.log("Not enough TCs found! Please try later!", style="red on white")


# with open(f"[{cid}{pid}]input.txt", "w+") as f:
#     for a, b in res:
#         f.write(a)

# with open(f"[{cid}{pid}]output.txt", "w+") as f:
#     for a, b in res:
#         f.write(b)


# id = pvcodes.get_testcases(1882, "A")
# cid = id[1]
# n = None
# if len(id) <= 10:
#     n = len(id)
# else:
#     n = 10
# if id:
#     for i in range(n):
#         print(id[i][0], id[i][1], sep="\n")
#         print("\n----------------------\n")
#     # print(id)
# else:
#     print(id)

# pvcodes.close()

# pvcodes.get_testcases(1856, 1)
