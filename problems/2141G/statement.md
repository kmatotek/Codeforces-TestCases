# Problem Description

On a Cartesian plane, there are $$$n$$$ distinct points painted black, while all other points are painted white. Each black point has integer coordinates.
There is also a robot that can move one unit in any of the directions 'U' (up), 'D' (down), 'L' (left), or 'R' (right) with a single command.
A path of the robot from point $$$p_{1}$$$ to point $$$p_{2}$$$ is a sequence of commands such that if the robot, starting at point $$$p_{1}$$$, executes this sequence, it will arrive at point $$$p_{2}$$$.
The shortest path of the robot from point $$$p_{1}$$$ to point $$$p_{2}$$$ is a path whose sequence consists of the minimum possible number of commands.
You need to count the number of pairs of points $$$p_i$$$, $$$p_j$$$ ($$$i \neq j$$$) such that for this pair of points the following condition holds:
Allpoints with integer coordinates onanyshortest path of the robot from point $$$p_{i}$$$ to point $$$p_{j}$$$ are painted black.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 5 \cdot 10^{5}$$$) — the number of points painted black.
The next $$$n$$$ lines of each test case contain two integers $$$x_{i}, y_{i}$$$ ($$$-10^{9} \le x_{i}, y_{i} \le 10^{9}$$$) — the coordinates of point $$$p_{i}$$$. All points are pairwise distinct.
It is guaranteed that the sum of $$$n$$$ across all test cases does not exceed $$$5 \cdot 10^{5}$$$.

## Output
For each test case, output a single integer — the answer to the problem.