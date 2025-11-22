# Problem Description

You are given an array of integers $$$a_1, a_2, \ldots, a_n$$$ and two integers $$$s$$$ and $$$x$$$. Count the number of subsegments of the array whose sum of elements equals $$$s$$$ and whose maximum value equals $$$x$$$.
More formally, count the number of pairs $$$1 \leq l \leq r \leq n$$$ such that:

## Input
Each test consists of multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \leq t \leq 10^4$$$) — the number of test cases. The description of the test cases follows.
The first line of each test case contains three integers $$$n$$$, $$$s$$$, and $$$x$$$ ($$$1 \leq n \leq 2 \cdot 10^5$$$, $$$-2 \cdot 10^{14} \leq s \leq 2 \cdot 10^{14}$$$, $$$-10^9 \leq x \leq 10^9$$$).
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$-10^9 \leq a_i \leq 10^9$$$).
It is guaranteed that the sum of $$$n$$$ across all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output the number of subsegments of the array whose sum of elements equals $$$s$$$ and whose maximum value equals $$$x$$$.