# Problem Description

You are given an undirected connected weighted graph. Define the cost of a path of length $$$k$$$ to be as follows:
Across all paths from vertex $$$1$$$ to $$$n$$$, report the cost of the path with minimum cost. Note that the path is not necessarily simple.

## Input
The first line contains an integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$2 \le n \le 2 \cdot 10^5, n - 1 \le m \le \min(2 \cdot 10^5, \frac{n(n - 1)}{2})$$$).
The next $$$m$$$ lines each contain integers $$$u, v$$$ and $$$w$$$ ($$$1 \le u, v \le n, 1 \le w \le 10^9$$$) representing an edge from vertex $$$u$$$ to $$$v$$$ with weight $$$w$$$. It is guaranteed that the graph does not contain self-loops or multiple edges and the resulting graph is connected.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$ and that the sum of $$$m$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output a single integer, the minimum cost path from vertex $$$1$$$ to $$$n$$$.