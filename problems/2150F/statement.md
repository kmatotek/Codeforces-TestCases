# Problem Description

You are given an undirected, connected graph $$$G$$$ with $$$n$$$ nodes and $$$m$$$ edges. The graph does not contain self loops nor multiple edges.
In one operation, you do the following, in order:
Note that an edge added by some operation can only be used by future operations, because the edges are added at the end of printing all simple paths.
Make $$$G$$$ complete in at most $$$2$$$ operations. Specifically, $$$G$$$ must contain every edge $$$(u, v)$$$ with $$$u < v$$$ exactly once.
Note:You are provided with the input files for the first $$$10$$$ tests of this problem, along with $$$2$$$ checkers (one in C++, one in Python) to verify your output. The checkers assume you follow the input and output formats of the problem. You can download the zip file from the Contest Materials section.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^3$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$3 \leq n \leq 200$$$, $$$n - 1\leq m \leq n(n-1)/2$$$) — the number of nodes and edges in $$$G$$$, respectively.
Each of the next $$$m$$$ lines contains two integers $$$u_i$$$, $$$v_i$$$ ($$$1 \leq u_i, v_i \leq n$$$, $$$u_i \neq v_i$$$), representing the edge $$$(u_i, v_i)$$$. The graph is connected and does not contain self loops nor multiple edges.
It is guaranteed that the sum of $$$n^2$$$ does not exceed $$$4 \cdot 10^4$$$ over all testcases.

## Output
For each test case, print the following.
In the first line, print the number of operations $$$op$$$ ($$$0 \le op \le 2$$$) you want to perform. For each operation: