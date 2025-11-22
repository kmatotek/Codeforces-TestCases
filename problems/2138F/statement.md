# Problem Description


You are given a 2D plane. Initially, two points $$$P_1$$$ and $$$P_2$$$ are located at $$$(0,0)$$$ and $$$(1,0)$$$, respectively, with a line segment connecting them. You can draw triangles using the following operation:
Note that each operation draws one new point and two new line segments.
Your task is to draw a point at coordinates $$$(p, q)$$$ using at most $$$m = \left\lceil 2\sqrt{p^2 + q^2}\right\rceil$$$ operations, where $$$\lceil x\rceil$$$ is the smallest integer greater than or equal to $$$x$$$. It is guaranteed that $$$p$$$ and $$$q$$$ are positive integers.
Due to potential rounding errors:
Note that the target point may be created before the last operation (see the second test case).

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 1000$$$). The description of the test cases follows.
The first line of each test case contains three integers $$$p$$$, $$$q$$$, and $$$m$$$ ($$$1\le p, q\le 10^4$$$, $$$m = \left\lceil 2\sqrt{p^2 + q^2}\right\rceil$$$) — the $$$x$$$ and $$$y$$$ coordinates of the target, and the maximum number of operations you are allowed to perform, respectively.
It is guaranteed that the sum of $$$m$$$ over all test cases does not exceed $$$10^5$$$.

## Output
For each test case, output a single integer $$$n$$$ ($$$0\le n\le m$$$) representing the number of operations used.
Then, output $$$n$$$ lines describing the operations. The $$$i$$$-th of the next $$$n$$$ lines should contain four values: two integers $$$u$$$ and $$$v$$$ ($$$1\le u,v\le i+1,u\neq v$$$), the identifiers of the two chosen points, followed by two real numbers $$$x$$$ and $$$y$$$ ($$$-2\cdot 10^4\le x,y\le 2\cdot 10^4$$$), the coordinates of the new point.
The identifiers are assigned as follows:
If there are multiple valid solutions that use at most $$$m$$$ operations, you may output any of them.