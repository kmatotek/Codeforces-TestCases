# Problem Description

There is a sheet of paper divided into $$$n$$$ rows and $$$m$$$ columns. Initially, no cell of this sheet is colored.
In one operation, you can choose any column or row and color it (if some cells were previously colored, their color changes to the new one). During the first operation, cells are colored with color $$$1$$$; during operation $$$i > 1$$$, you can choose either color $$$c_{i-1}$$$ or $$$c_{i-1} + 1$$$, where $$$c_{i-1}$$$ is the color chosen during operation $$$(i-1)$$$.
We call the final coloring beautiful if the following conditions are met:
For a beautiful final coloring, we define its value as the minimum number of operations required to achieve it.
For each $$$i$$$ from $$$\min(n, m)$$$ to $$$n + m - 1$$$, calculate the number of beautiful colorings with value $$$i$$$. Two colorings are considered different if the color of at least one cell differs in these colorings.

## Input
The input consists of a single line containing three integers $$$n, m, k$$$ ($$$2 \le n, m \le 2000$$$; $$$1 \le k \le n + m - 1$$$).

## Output
For each $$$i$$$ from $$$\min(n, m)$$$ to $$$n + m - 1$$$, output a single integer — the number of beautiful colorings with value $$$i$$$, taken modulo $$$998244353$$$.