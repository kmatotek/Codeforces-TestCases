# Problem Description

We call a set of integers $$$Q$$$ aset of complementary sumsif it can be obtained through the following actions:
Note that $$$Q$$$ is not a multiset, meaning each number in it is unique. For example, if the array $$$a = [1, 3, 3, 7]$$$ was chosen, then $$$s = 14$$$ and $$$Q = \{7, 11, 13\}$$$.
Your task is to count the number of distinctsets of complementary sumsfor which the following holds:
Two sets are considered different if there exists an element in the first set that is not included in the second set.
Since the answer can be huge, output it modulo $$$998\,244\,353$$$.

## Input
Each test consists of several test cases. The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^{4}$$$) — the number of test cases. The description of the test cases follows.
The only line of each test case contains two integers $$$n$$$ and $$$x$$$ ($$$1 \le n, x \le 2 \cdot 10^{5}$$$).
Additional constraints on the input data:

## Output
For each test case, output a single integer — the answer to the problem modulo $$$998\,244\,353$$$.