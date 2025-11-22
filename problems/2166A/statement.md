# Problem Description


You are given a string $$$s$$$ of length $$$n$$$, consisting of lowercase letters.
In one operation, you can select an integer $$$i$$$ such that $$$1\leq i < n$$$ and change $$$s_i$$$ into $$$s_{i+1}$$$.
What is the minimum number of operations needed to make every character the same? It can be proved that this is always possible.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 20$$$). The description of the test cases follows.
The first line of each test case contains an integer $$$n$$$ ($$$2\le n\le 100$$$) — the length of the string.
The following line contains a string $$$s$$$ of length $$$n$$$, consisting of lowercase letters.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$100$$$.

## Output
For each test case, output a single integer — the minimum number of operations needed to make every character the same.