# Problem Description

You are given an integer $$$n$$$ and an array $$$a$$$ of length $$$n$$$.
Find thesmallestinteger $$$x$$$ ($$$2 \le x \le 10^{18}$$$) such that there exists an index $$$i$$$ ($$$1 \le i \le n$$$) with$$$\gcd$$$$$$^{\text{∗}}$$$$$$(a_i, x) = 1$$$. If no such $$$x$$$ exists within the range $$$[2,10^{18}]$$$, output $$$-1$$$.
$$$^{\text{∗}}$$$$$$\gcd(x, y)$$$ denotes thegreatest common divisor (GCD)of integers $$$x$$$ and $$$y$$$.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
Each of the following $$$t$$$ test cases consists of two lines:
The first line contains a single integer $$$n$$$ ($$$1 \le n \le 10^{5}$$$) — the length of the array.
The second line contains $$$n$$$ space-separated integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^{18}$$$).
It is guaranteed that the total sum of $$$n$$$ across all test cases does not exceed $$$10^{5}$$$.

## Output
For each test case, output a single integer: the smallest $$$x$$$ ($$$2 \le x \le 10^{18}$$$) such that there exists an index $$$i$$$ with $$$\gcd(a_i, x) = 1$$$. If there is no such $$$x$$$ in the range $$$[2,10^{18}]$$$, print $$$-1$$$.