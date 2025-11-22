# Problem Description

You are given an array $$$a$$$ of $$$n$$$ integers. We define the $$$\text{beauty}$$$ of a number $$$x$$$ to be the number of $$$1$$$ bits in its binary representation. We define the beauty of an array to be the sum of beauties of the numbers it contains.
In one operation, you can select an index $$$i$$$ $$$(1 \le i \le n)$$$ and increase $$$a_i$$$ by $$$1$$$.
Find the maximum beauty of the array after doingat most$$$k$$$ operations.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 5000$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le n \le 5000$$$, $$$0 \le k \le 10^{18}$$$) — the length of the array and the maximal number of operations.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots a_n$$$ ($$$0 \le a_i \le 10^9$$$) —denoting the array $$$a$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$5000$$$.

## Output
For each test case, output a single integer, the maximum beauty after at most $$$k$$$ operations.