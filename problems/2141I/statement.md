# Problem Description

You are given a tree consisting of $$$n$$$ vertices. Initially, none of the vertices of the tree are colored.
You can perform the following operation: choose any two vertices $$$u$$$ and $$$v$$$ (you are allowed to choose $$$u=v$$$) and color all the vertices on the path between them (including the endpoints) with color $$$i$$$, where $$$i$$$ is the index of the operation you are performing (that is, the first operation uses color $$$1$$$, the second uses color $$$2$$$, and so on). If any vertex on the path has already been colored before, its color changes to the new one.
We call the coloring of the treecompleteif for each vertex, at least one operation has colored it.
Your task is to calculate two values:

## Input
The first line contains a single integer $$$n$$$ ($$$3 \le n \le 32$$$) — the number of vertices in the tree.
The next $$$(n-1)$$$ lines contain two integers $$$x_i$$$ and $$$y_i$$$ ($$$1 \le x_i, y_i \le n$$$; $$$x_i \ne y_i$$$) — the endpoints of the next edge of the tree.
Additional constraint on the input: the edges define a valid tree with $$$n$$$ vertices.

## Output
Print two integers — the minimum number of operations and the number of distinct complete colorings that can be obtained with the minimum number of operations. Since the second number can be very large, output it modulo $$$998244353$$$.