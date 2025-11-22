# Problem Description


Consider an undirected graph $$$G$$$ with $$$n$$$ vertices and positive integer capacities on its edges. We denote by $$$\textsf{maxflow}(u, v)$$$ the value of themaximum flowin the graph from source $$$u$$$ to sink $$$v$$$. We say that such a graph $$$G$$$ isgoodif there exists a positive integer $$$d \geq 2$$$ such that $$$d$$$ divides each of the $$$n \cdot (n-1)$$$ values of $$$\textsf{maxflow}(u, v)$$$ for all pairs $$$(u, v)$$$ of distinct vertices of $$$G$$$. Note that, in particular, any graph without edges is good.
You are given a graph, and you have to color its vertices so that, for each color, the subgraph induced$$$^{\text{∗}}$$$ by the vertices of that color is good. Find such a coloring with theminimumpossible number of colors.
$$$^{\text{∗}}$$$Subgraph induced by a set of vertices $$$S$$$ is another graph, whose vertices are $$$S$$$ and whose edges areallof the edges, from the original graph, connecting pairs of vertices in $$$S$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 1000$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$1 \leq n \leq 50$$$, $$$0 \leq m \leq \frac{n(n-1)}{2}$$$), the number of vertices and the number of edges of the graph.
The next $$$m$$$ lines each contain three integers $$$u$$$, $$$v$$$, $$$w$$$ ($$$1 \leq u, v \leq n$$$, $$$1 \leq w \leq 10^6$$$), denoting that there is an edge connecting vertices $$$u$$$ and $$$v$$$ with capacity $$$w$$$. It is guaranteed that there are no self-loops or multiple edges between the same vertices.
It is guaranteed that the sum of $$$n^4$$$ over all test cases does not exceed $$$50^4$$$.
It can be shown that other limitations imply that the sum of $$$m$$$ over all test cases does not exceed $$$50\,000$$$, so you don't need to worry about the size of the input.

## Output
For each test case, output one integer $$$c$$$, the minimum possible number of colors. Then, output $$$2c$$$ lines, describing the coloring. For each $$$1 \leq i \leq c$$$, you must output two lines: one line with the number of vertices $$$k_i$$$ colored with the $$$i$$$-th color, followed by one line with $$$k_i$$$ integers, the vertices colored with the $$$i$$$-th color.
If there are multiple solutions, print any of them.