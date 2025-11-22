# Problem Description

You are given two integer arrays $$$a_0, \ldots, a_{n - 1}$$$ and $$$b_0, \ldots, b_{m - 1}$$$. Each integer among $$$1, \ldots, n + m$$$ is present exactly once among $$$a_0, \ldots, a_{n - 1}, b_0, \ldots, b_{m - 1}$$$.
We perform $$$k$$$ operations on the arrays. Namely, for each integer $$$i$$$ from $$$0$$$ to $$$k - 1$$$ in this order
Determine the final state of both arrays after all $$$k$$$ operations are completed.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains three integers $$$n, m, k$$$ ($$$1 \leq n, m \leq 2 \cdot 10^5$$$, $$$0 \leq k \leq 10^{18}$$$).
The second line contains $$$n$$$ integers $$$a_0, \ldots, a_{n - 1}$$$.
The third line contains $$$m$$$ integers $$$b_0, \ldots, b_{m - 1}$$$.
It is guaranteed that the joint sequence $$$a_0, \ldots, a_{n - 1}, b_0, \ldots, b_{m - 1}$$$ is a permutation of integers from $$$1$$$ to $$$n + m$$$.
The sum of $$$n + m$$$ over all testcases doesn't exceed $$$2 \cdot 10^5$$$.

## Output
For each testcase, print two lines — the states of the arrays $$$a_0, \ldots, a_{n - 1}$$$ and $$$b_0, \ldots, b_{m - 1}$$$ after the $$$k$$$ operations are performed as described above.