# Problem Description


This is an interactive problem.
You are given $$$n$$$ boxes, indexed from $$$1$$$ to $$$n$$$. The boxes look identical, but each one has a hidden power value $$$a_i$$$, which is either $$$1$$$ or $$$2$$$.
You want to determine the power value of each box. To do so, you conduct the following experiment. Initially, the $$$i$$$-th box is placed at coordinate $$$i$$$ on a number line ($$$1 \le i \le n$$$).
You are allowed to perform the following two types of queries:
Your task is to determine the power value of each box using no more than $$$\left\lceil \frac{3n}{2} \right\rceil$$$ queries in total, counting bothswapandthrowqueries.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 500$$$). The description of the test cases follows.
The first and the only line of each test case contains a single integer $$$n$$$ ($$$2 \le n \le 1000$$$) — the number of boxes.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$1000$$$.
