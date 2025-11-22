# Problem Description


To help improve her math, Kudryavka is given a set $$$S$$$ that consists of $$$n$$$ distinct positive integers.
Initially, herscoreis $$$1$$$. She can perform an arbitrary number of the following operations on the set if it is not empty:
She is addicted to performing operations, but after $$$k$$$ operations, she realizes she forgot herscore. Please help her determine herscore, modulo $$$10^9+7$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le n \le 2 \cdot 10^5$$$, $$$1 \le k \le 10^9$$$).
The second line of each test case contains $$$n$$$ integers $$$s_1, s_2, \dots, s_n$$$ ($$$1 \le s_i \le 10^9$$$, $$$s_i \neq s_j$$$) — the elements of the initial set $$$S$$$. It is guaranteed that the set $$$S$$$ is not empty before each of the $$$k$$$ operations is performed.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output an integer indicating the answer modulo $$$10^9+7$$$.