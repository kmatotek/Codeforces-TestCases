# Problem Description

You are given two arrays of integers $$$a_1, a_2, \ldots, a_n$$$ and $$$b_1, b_2, \ldots, b_n$$$. It is guaranteed that each integer from $$$1$$$ to $$$2 \cdot n$$$ appears in exactly one of the arrays.
You need to perform a certain number of operations (possibly zero) so thatbothof the following conditions are satisfied:
During each operation, you can perform exactly one of the following three actions:
You do not need to minimize the number of operations, but the total number must not exceed $$$1709$$$. Find any sequence of operations that satisfiesbothconditions.

## Input
Each test consists of multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \leq t \leq 100$$$) — the number of test cases. The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \leq n \leq 40$$$) — the length of the arrays $$$a$$$ and $$$b$$$.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \leq a_i \leq 2 \cdot n$$$).
The third line of each test case contains $$$n$$$ integers $$$b_1, b_2, \ldots, b_n$$$ ($$$1 \leq b_i \leq 2 \cdot n$$$).
It is guaranteed that each integer from $$$1$$$ to $$$2 \cdot n$$$ appears either in array $$$a$$$ or in array $$$b$$$.

## Output
For each test case, output the sequence of operations.
In the first line for each test case, output the number of operations $$$k$$$. Note that $$$0 \leq k \leq 1709$$$.
In the following $$$k$$$ lines for each test case, output the operations themselves:
It can be shown that under the given constraints, a solution always exists.