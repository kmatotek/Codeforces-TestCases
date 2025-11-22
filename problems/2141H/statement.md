# Problem Description

You are given an undirected graph, initially containing $$$n$$$ vertices and $$$m$$$ edges. You can perform the following operation on this graph:
This operation can be performed any number of times until there exists a vertex in the graph that is directly connected by edges to all other vertices. As soon as such a vertex appears, the process ends. Additionally, if such a vertex already exists in the graph initially, no operations can be performed.
Your task is to count the minimum and maximum number of operations that you can perform.

## Input
The first line contains two integers $$$n$$$ and $$$m$$$ ($$$1 \le n \le 2 \cdot 10^5$$$; $$$0 \le m \le \min(\frac{n(n - 1)}{2}, 2 \cdot 10^5)$$$).
The $$$i$$$-th of the following $$$m$$$ lines contains two integers $$$x_i, y_i$$$ ($$$1 \le x_i, y_i \le n$$$; $$$x_i \ne y_i$$$) — the endpoints of the $$$i$$$-th edge. There is at most one edge between each pair of vertices.

## Output
Output two integers — the minimum and the maximum number of operations.