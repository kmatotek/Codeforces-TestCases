# Problem Description

You are given three positive integers $$$n$$$, $$$a$$$, and $$$b$$$ ($$$1\leq a,b \leq n$$$).
Consider a row of $$$n$$$ cells, initially all white and indexed from $$$1$$$ to $$$n$$$. You will perform the following two stepsin order:
If a cell is painted both red and blue, its final color is blue.
A coloring of the grid is consideredsymmetricif, for every integer $$$i$$$ from $$$1$$$ to $$$n$$$ (inclusive), the color of cell $$$i$$$ is the same as the color of cell $$$(n+1-i)$$$. Your task is to determine whether there exist integers $$$x$$$ and $$$y$$$ such that the final coloring of the grid is symmetric.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 500$$$). The description of the test cases follows.
The first and the only line of each test case contains three integers $$$n$$$, $$$a$$$, and $$$b$$$ ($$$1 \le n \le 10^9$$$, $$$1 \le a,b \le n$$$) — the number of cells of the grid and the number of cells to be painted in each step.

## Output
For each testcase, output "YES" if it is possible that the final coloring of the grid is symmetric; otherwise, output "NO".
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.