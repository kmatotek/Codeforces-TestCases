# Problem Description


You are given $$$n$$$ non-negative integers $$$a_1,a_2,\ldots,a_n$$$ arranged on a ring. For each $$$1\le i< n$$$, $$$a_i$$$ and $$$a_{i+1}$$$ are adjacent; $$$a_1$$$ and $$$a_n$$$ are adjacent.
You need to perform the following operationexactly$$$n-1$$$ times:
Note that this operation will decrease the size of the ring by $$$1$$$ and update the adjacent relationships accordingly.
Please calculate the minimum total cost to merge the ring into one element.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains an integer $$$n$$$ ($$$2\le n\le 2\cdot 10^5$$$).
The following line contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$0\le a_i \le 10^9$$$).
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2\cdot 10^5$$$.

## Output
For each test case, please print a single integer — the minimum total cost.