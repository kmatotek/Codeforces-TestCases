# Problem Description


Juan has a beautiful tree with $$$n$$$ nodes numbered from $$$1$$$ to $$$n$$$. There are also $$$k$$$ distinct colors numbered from $$$1$$$ to $$$k$$$. Each node $$$u$$$ in the tree has its own set $$$C_u$$$ which contains colors. Let's denote with $$$s$$$ the quantity $$$\sum_{i=1}^n \left| C_i \right|$$$.
There are $$$q$$$ queries where you will be given nodes $$$u$$$ and $$$v$$$. Let $$$P$$$ denote the set of all nodes in the simple path between $$$u$$$ and $$$v$$$, inclusive. You are asked to calculate for each query the following quantity: $$$$$$\left| \bigcap_{w \in P} C_w \right|$$$$$$
That is, the cardinality of the intersection of the sets of all the nodes in the path from $$$u$$$ to $$$v$$$. In other words, calculate how many colors appear in every set on the path from $$$u$$$ to $$$v$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains four integers $$$n$$$, $$$k$$$, $$$s$$$, and $$$q$$$ ($$$1 \le n, k, q \le 3 \cdot 10^5, 1 \le s \le \min (nk, 3 \cdot 10^5)$$$) — the number of nodes in the tree, the number of distinct colors, the sum of the cardinalities of all sets of colors, and the number of queries, respectively.
The next $$$n-1$$$ lines each contain two integers $$$u$$$, $$$v$$$ ($$$1 \le u, v \le n$$$), indicating that there's an edge between nodes $$$u$$$ and $$$v$$$.
The next $$$s$$$ lines each contain two integers $$$v$$$ and $$$x$$$ ($$$1 \le v \le n, 1 \le x \le k$$$) indicating that color $$$x$$$ is in $$$C_v$$$. All $$$s$$$ lines are pairwise distinct.
The next $$$q$$$ lines each contain two integers $$$u$$$ and $$$v$$$ ($$$1 \le u, v \le n$$$), indicating a query between nodes $$$u$$$ and $$$v$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$3 \cdot 10^5$$$.
It is guaranteed that the sum of $$$k$$$ over all test cases does not exceed $$$3 \cdot 10^5$$$.
It is guaranteed that the sum of $$$s$$$ over all test cases does not exceed $$$3 \cdot 10^5$$$.
It is guaranteed that the sum of $$$q$$$ over all test cases does not exceed $$$3 \cdot 10^5$$$.

## Output
For each test case, output a line: the answer to all queries in the order they appear in the input, separated by spaces.