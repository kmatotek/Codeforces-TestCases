# Problem Description

Alice has a grid of size $$$n \times n$$$. Initially, all cells are colored white. Alice wants to color some cells black satisfying certain properties.
Let $$$(x_1, y_1), (x_2, y_2), \ldots, (x_m, y_m)$$$ be the cells colored black. You are given an array $$$a$$$ of size $$$n$$$. The following conditions must be satisfied:
For example, when $$$a = [2, 2, 1, 0, 0]$$$, a possible set of black cells is $$$\{(1, 1), (2, 2), (3, 3), (2, 4), (1, 5)\}$$$. This corresponds to the following grid:
Count the number of possible grids. $$$2$$$ grids are said to be different if there is some cell which is colored black in one of the grids, and white in the other. Since the answer may be large, output it modulo $$$998\,244\,353$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$).
The second line of each test case contains $$$n$$$ integers — $$$a_1, a_2, \ldots, a_n$$$ ($$$0 \le a_i \le n$$$)
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output a single line containing an integer: the number of valid grids modulo $$$998\,244\,353$$$.