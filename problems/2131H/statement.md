# Problem Description


Umi is given an array $$$a$$$ of length $$$n$$$, whose elements are integers between $$$1$$$ and $$$m$$$. She loves coprime integers and wants to find fourdistinctindices $$$p, q, r, s$$$ ($$$1 \le p, q, r, s \le n$$$), such that $$$\gcd(a_p, a_q) = 1$$$ and $$$\gcd(a_r, a_s) = 1$$$$$$^{\text{∗}}$$$.
If there are multiple solutions, you may output any one of them.
$$$^{\text{∗}}$$$$$$\gcd(x, y)$$$ denotes thegreatest common divisor (GCD)of integers $$$x$$$ and $$$y$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$4 \le n \le 2 \cdot 10^5, 1 \le m \le 10^6$$$).
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le m$$$).
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$, and that the sum of $$$m$$$ over all test cases does not exceed $$$10^6$$$.

## Output
For each test case: