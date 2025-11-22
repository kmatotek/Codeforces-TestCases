# Problem Description

There is an undirected tree with root $$$1$$$ where each vertex has a weight $$$w_i\in\{1,-1\}$$$.
A volcano at the root erupts at time $$$0$$$. At time $$$t$$$, lava floods all vertices whose distance from the root is at most $$$t$$$, where the distance is the number of edges in the shortest path between the two vertices.
At time $$$0$$$, you are at vertex $$$st$$$ with life value $$$S$$$, initially $$$S=1$$$. Starting at time $$$0$$$ (including time $$$0$$$), the following events happen in order at each time stamp:
Find the maximum number of moves you can make before you die.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$T$$$ ($$$1 \le T \le 10^4$$$). The description of the test cases follows.
For each test case, the first line contains two integers $$$n,st$$$ ($$$2 \le st \le n \le 5\cdot 10^5$$$), denoting the number of vertices and the vertex you start at at time stamp $$$0$$$.
The second line contains $$$n$$$ integers $$$w_1, w_2, \ldots, w_n$$$ ($$$w_i\in\{1,-1\}$$$,$$$w_{st}=1$$$), where $$$w_i$$$ represents the weight of the vertex $$$i$$$.
The next $$$n-1$$$ lines each contain two integers $$$u,v$$$ ($$$1\le u,v \le n$$$), which describe a pair of vertices connected by an edge.
It is guaranteed that the given graph is a tree and the sum of $$$n$$$ over all test cases does not exceed $$$10^6$$$.

## Output
For each test case, output a line with an integer indicating the maximum number of moves you can make.