# Problem Description

Two arrays $$$p$$$ and $$$s$$$ of length $$$n$$$ are given, where $$$p$$$ is the prefix GCD$$$^{\text{∗}}$$$ of some array $$$a$$$, and $$$s$$$ is the suffix GCD of the same array $$$a$$$. In other words, if the array $$$a$$$ existed, then for each $$$1 \le i \le n$$$, the following equalities would hold both:
$$$^{\text{∗}}$$$$$$\gcd(x, y)$$$ denotes thegreatest common divisor (GCD)of integers $$$x$$$ and $$$y$$$.

## Input
The first line contains an integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
Each test case consists of three lines:
The first line of each test case contains a single integer $$$n$$$ ($$$1 \leq n \leq 10^5$$$) — the length of the array.
The second line of each test case contains $$$n$$$ integers $$$p_1, p_2, \dots, p_n$$$ ($$$1 \leq p_i \le 10^9$$$) — the elements of the array.
The third line of each test case contains $$$n$$$ integers $$$s_1, s_2, \dots, s_n$$$ ($$$1 \leq s_i \le 10^9$$$) — the elements of the array.
It is guaranteed that the sum of all $$$n$$$ across all test cases does not exceed $$$10^5$$$.

## Output
For each test case, output "Yes" (without quotes) if there exists an array $$$a$$$ for which the given arrays $$$p$$$ and $$$s$$$ can be obtained, and "No" (without quotes) otherwise.
You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.