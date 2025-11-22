# Problem Description

There is a robot located in the cell $$$(a,b)$$$ of an infinite grid. Misha wants to move it to the cell $$$(0,0)$$$. To do this, he has fixed some integer $$$k$$$.
Misha can perform the following operation: choose two integers $$$dx$$$ and $$$dy$$$ (both from $$$0$$$ to $$$k$$$ inclusive) and move the robot $$$dx$$$ cells to the left (in the direction of decreasing $$$x$$$ coordinate) and $$$dy$$$ cells down (in the direction of decreasing $$$y$$$ coordinate). In other words, move the robot from $$$(x,y)$$$ to $$$(x - dx, y - dy)$$$.
The cost of the operation is:
Note that if $$$dx \ne dy$$$, the pairs $$$(dx, dy)$$$ and $$$(dy, dx)$$$ are considered different.
Help Misha bring the robot to the cell $$$(0,0)$$$ with minimum total cost. Note that you don't have to minimize the number of operations.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The only line of each test case contains three integers $$$a, b$$$, and $$$k$$$ ($$$1 \le a, b, k \le 10^{18}$$$).

## Output
For each test case, output a single integer — the minimum total cost of operations required to move the robot to the cell $$$(0,0)$$$.