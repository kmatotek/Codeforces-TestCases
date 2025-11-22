# Problem Description

An arbitrary array of integers $$$b$$$ of length $$$m$$$ is considered awesome if for all $$$i$$$ ($$$1 \le i < m$$$):
In other words, the following inequality is true: $$$b_1 < b_2 > b_3 < b_4 \ldots$$$
You are given an array of positive integers $$$a$$$ of length $$$n$$$. You may do either of the following operations any number of times, in any order:
Determine the minimum number of times you need to do operation $$$2$$$ to make $$$a$$$ awesome. Note that you donotneed to minimise the number of times you perform operation $$$1$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains an integer $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$) — the length of the array $$$a$$$.
The second line of each test case contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$1 \le a_i \le 10^9$$$).
The sum of $$$n$$$ across all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each testcase, output the minimum cost to make $$$a$$$ awesome.