# Problem Description

You are given an $$$n \times n$$$ grid where some cells are colored black, and the rest are white. You may paint some of the white cells black to achieve the following conditions:
You can't paint black cells white.
Determine whether it is possible to paint some white cells black in order to satisfy all the conditions.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 1000$$$). The description of the test cases follows.
The first line contains an integer $$$n$$$ ($$$1 \leq n \leq 100$$$) — the size of the grid.
The following $$$n$$$ lines contain $$$n$$$ characters each — the grid description, where each character represents a cell:
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2000$$$.

## Output
For each test case, print "YES" if it is possible to paint some white cells black to satisfy all the conditions, and "NO" otherwise.
You may print each letter in any case (uppercase or lowercase). For example, the strings "yEs", "yes", "Yes", and "YES" will all be recognized as a positive answer.