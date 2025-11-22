# Problem Description

You are given an undirected connected graph with $$$n$$$ nodes and $$$m$$$ edges. The weight $$$w_i$$$ of the $$$i$$$-th edge is not yet decided and must be a real number between $$$l_i$$$ and $$$r_i$$$.
You are given a node $$$k$$$. Determine if there exists a valid assignment of weights $$$(w_1, \ldots, w_m)$$$ such that:
$$$^{\text{∗}}$$$Given an assignment of weights $$$w$$$, $$$\mathrm{dist}_w(u, v)$$$ is the minimum value of $$$w_{e_1} + w_{e_2} + \ldots + w_{e_p}$$$ over all sequences of $$$p$$$ edges $$$(e_1, e_2, \ldots, e_p)$$$ that form a path from $$$u$$$ to $$$v$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10\,000$$$). The description of the test cases follows.
The first line of each test case contains three integers $$$n$$$, $$$m$$$, and $$$k$$$ ($$$4 \le n \le 200\,000$$$, $$$n-1 \le m \le 200\,000$$$, $$$2 \le k \le n - 1$$$) — the number of nodes, the number of edges, and the node $$$k$$$.
The $$$i$$$-th of the following $$$m$$$ lines contains four integers $$$u_i$$$, $$$v_i$$$, $$$l_i$$$, and $$$r_i$$$ ($$$1 \le u_i, v_i \le n$$$, $$$u_i \ne v_i$$$, $$$1 \le l_i \le r_i \le 10^9$$$), representing an edge between $$$u_i$$$ and $$$v_i$$$ whose weight must be between $$$l_i$$$ and $$$r_i$$$ inclusive. No edge appears in the input more than once.
It is guaranteed that:

## Output
PrintYESif there exists a valid assignment of weights andNOotherwise.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.