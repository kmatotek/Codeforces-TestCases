# Problem Description


This is an interactive problem.
Madeline is playing with a pointless machine. The pointless machine has a hidden tree of size $$$n$$$, and Madeline has to find the edges of the tree by asking the machine.
In a query, Madeline will give the machine a permutation $$$p$$$ of $$$[1,2,\ldots,n]$$$, and the machine will return a sequence $$$q_1, q_2, \ldots, q_n$$$, where $$$q_i$$$ is the number of edges of the induced subgraph formed by the vertices $$$\{p_1,p_2,\ldots,p_i\}$$$.
Here, an induced subgraph of a graph $$$G(V,E)$$$ formed by a subset of vertices $$$V' \subseteq V$$$, is a graph consisting of vertices from this subset and all edges between vertices from subset that are present in original graph $$$G$$$.
However, the machine works slowly, so Madeline can only get the results at once after all queries are completed. The memory of this machine is not very large either, so Madeline can only ask $$$31$$$ times. She doesn't know how to solve it, so she invited you to help her.
Note that the interactor isnon-adaptive. That is, tree is fixed in advance and doesn't change with your queries.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The only line of each test case contains a single integer $$$n$$$ ($$$3\le n\le 5\cdot 10^4$$$) — the size of the tree.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$5\cdot 10^4$$$.
