# Problem Description

Given a tree$$$^{\text{∗}}$$$ with $$$n$$$ vertices numbered from $$$1$$$ to $$$n$$$. Each vertex has an initial color $$$a_i$$$.
Each edge of the tree is defined by three numbers: $$$u_i$$$, $$$v_i$$$, and $$$c_i$$$, where $$$u_i$$$ and $$$v_i$$$ are the endpoints of the edge, and $$$c_i$$$ is the edge parameter. The cost of the edge is defined as follows: if the colors of vertices $$$u_i$$$ and $$$v_i$$$ are the same, the cost is $$$0$$$; otherwise, the cost is $$$c_i$$$.
You are also given $$$q$$$ queries. Each query has the form: repaint vertex $$$v$$$ to color $$$x$$$. The queries depend on each other (after each query, the color change is preserved). After each query, you need to output the sum of the costs of all edges in the tree.
$$$^{\text{∗}}$$$A tree is a connected graph without cycles.

## Input
The first line contains an integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first line of each test case contains two integers $$$n$$$ and $$$q$$$ ($$$1 \le n, q \le 2\cdot10^5$$$) — the number of vertices and the number of queries, respectively.
The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le n$$$), where the $$$i$$$-th number specifies the initial color of vertex $$$i$$$.
The next $$$n-1$$$ lines describe the edges of the tree. Each line contains three integers $$$u$$$, $$$v$$$, and $$$c$$$, denoting an edge between vertices $$$u$$$ and $$$v$$$ with parameter $$$c$$$ ($$$1 \le u, v \le n$$$, $$$1 \le c \le 10^9$$$).
The following $$$q$$$ lines contain the queries. Each query contains two integers $$$v$$$ and $$$x$$$ — repaint vertex $$$v$$$ to color $$$x$$$ ($$$1 \le v,x \le n$$$).
It is guaranteed that the sum of $$$n$$$ and the sum of $$$q$$$ across all test cases do not exceed $$$2\cdot10^5$$$.

## Output
For each query, output a single integer on a separate line — the sum of the costs of all edges in the tree after applying the corresponding query.