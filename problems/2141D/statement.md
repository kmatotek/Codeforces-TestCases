# Problem Description

You are given an integer array $$$a_1, a_2, a_3, \dots, a_n$$$. Your task is to make all elements of $$$a$$$ equal. In order to do it, you can perform the following operation at most $$$k$$$ times:
What is the maximum number of coins you can earn among all possible ways to make the array equal?

## Input
The first line contains one integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases. Next, $$$t$$$ cases follow (all cases are independent).
The first line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$2 \le n \le 3 \cdot 10^5$$$; $$$1 \le k \le 10^{12}$$$) — the size of array $$$a$$$ and the maximum number of operations you can perform.
The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^9$$$) — the array itself.
It's guaranteed that the total sum of $$$n$$$ over all test cases doesn't exceed $$$3 \cdot 10^5$$$.

## Output
For each test case, if it's impossible to make all elements equal, print $$$-1$$$. Otherwise, print the maximum number of coins you can earn while making all elements equal.