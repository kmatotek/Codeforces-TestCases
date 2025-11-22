# Problem Description

You are given two arrays $$$a$$$ and $$$b$$$ of length $$$n$$$. You can perform the following operation an unlimited number of times:
Let $$$f(c)$$$ be the number of distinct numbers in array $$$c$$$. Find the maximum value of $$$f(a) + f(b)$$$. Also, output the arrays $$$a$$$ and $$$b$$$ after performing all operations.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 10^5$$$) — the length of the arrays.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \le a_i \le 2n$$$) — the elements of array $$$a$$$.
The third line of each test case contains $$$n$$$ integers $$$b_1, b_2, \ldots, b_n$$$ ($$$1 \le b_i \le 2n$$$) — the elements of array $$$b$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^5$$$.

## Output
For each test case, print a single integer in the first line — the maximum value of $$$f(a) + f(b)$$$.
In the second line, print $$$n$$$ integers — the elements of array $$$a$$$ after performing the operations.
In the third line, print $$$n$$$ integers — the elements of array $$$b$$$ after performing the operations.