# Problem Description

Surely, you have seen problems which require you to output the answer modulo $$$10^9+7$$$, $$$10^9+9$$$, or $$$998244353$$$. But have you ever seen a problem where you have to print the answer modulo $$$3$$$?
You are given a functional graph consisting of $$$n$$$ vertices, numbered from $$$1$$$ to $$$n$$$. It is a directed graph, in which each vertex has exactly one outgoing arc. The graph is given as the array $$$g_1, g_2, \dots, g_n$$$, where $$$g_i$$$ means that there is an arc that goes from $$$i$$$ to $$$g_i$$$. For some vertices, the outgoing arcs might be self-loops.
Initially, all vertices of the graph are colored in color $$$1$$$. You can perform the following operation: select a vertex and a color from $$$1$$$ to $$$k$$$, and then color this vertex and all vertices that are reachable from it. You can perform this operation any number of times (even zero).
You should process $$$q$$$ queries. The query is described by three integers $$$x$$$, $$$y$$$ and $$$k$$$. For each query, you should:
Note that in every query, the initial coloring of the graph is reset (all vertices initially have color $$$1$$$ in each query).

## Input
The first line contains two integers $$$n$$$ and $$$q$$$ ($$$1 \le n, q \le 2 \cdot 10^5$$$).
The second line contains $$$n$$$ integers $$$g_1, g_2, \dots, g_n$$$ ($$$1 \le g_i \le n$$$).
The $$$q$$$ lines follow. The $$$i$$$-th line contains three integers $$$x_i$$$, $$$y_i$$$ and $$$k_i$$$ ($$$1 \le x_i, y_i \le n$$$; $$$1 \le k_i \le 10^9$$$).

## Output
For each query, print a single integer — the number of different graph colorings for the given value of $$$k$$$, taken modulo $$$3$$$.