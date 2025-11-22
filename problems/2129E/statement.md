# Problem Description

You are given an unweighted, undirected graph $$$G$$$ with $$$n$$$ nodes and $$$m$$$ edges. The graph $$$G$$$ contains no self-loops or multiple edges.
We denote the node set of $$$G$$$ as $$$V$$$. For any node subset $$$V' \subseteq V$$$, the corresponding induced subgraph, denoted by $$$G[V']$$$, is defined as follows:
Your task is to answer $$$q$$$ queries. Each query provides three integers $$$l$$$, $$$r$$$, and $$$k$$$. Denoting $$$V'=\{l,l+1,\ldots,r\}$$$, you need to find the $$$k$$$-th smallest value among $$$f(l,G[V'])$$$, $$$f(l+1,G[V'])$$$, $$$\ldots$$$ , $$$f(r,G[V'])$$$ (i.e., the $$$k$$$-th value in increasing order; repeated values are counted multiple times).
Here, $$$f(u,G[V'])=\bigoplus_{(u,v)\in G[V']}v$$$. In other words, it is thebitwise XORvalue of the labels of all adjacent nodes of node $$$u$$$ in graph $$$G[V']$$$.
You might want to read the notes for a better understanding.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 1.5 \cdot 10^4$$$). The description of the test cases follows.
Each test case begins with two integers $$$n$$$ and $$$m$$$ ($$$2 \leq n \leq 1.5 \cdot 10^5$$$, $$$1 \leq m \leq 1.5 \cdot 10^5$$$) — the number of nodes and edges, respectively.
The next $$$m$$$ lines each contain two integers $$$u_i$$$ and $$$v_i$$$ ($$$1 \leq u_i, v_i \leq n$$$, $$$u_i \neq v_i$$$), representing an undirected edge between nodes $$$u_i$$$ and $$$v_i$$$.
The next line contains a single integer $$$q$$$ ($$$1 \leq q \leq 1.5 \cdot 10^5$$$) — the number of queries.
Each of the next $$$q$$$ lines contains three integers $$$l$$$, $$$r$$$, and $$$k$$$ ($$$1 \leq l \leq r \leq n$$$, $$$1 \le k \le r-l+1$$$), defining a query about the induced subgraph $$$G[\{l,\ldots,r\}]$$$.
It is guaranteed that the graph contains no self-loops or multiple edges.
It is guaranteed that the sum of $$$n$$$,$$$m$$$, and $$$q$$$ over all test cases does not exceed $$$1.5 \cdot 10^5$$$, respectively.

## Output
For each test case, output $$$q$$$ integers, representing the answer for each query.