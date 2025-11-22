# Problem Description

Consider a binary string of length $$$n$$$ and an odd number $$$k$$$. We will call the binary stringgoodif for each substring of length $$$k$$$, the leftmost character of the substring occurs more than the other.
For example, if $$$k = 3$$$,000101is a good string, because for all substrings of length 3 (000,001,010, and101) the first character of the substring occurs more than the other character. On the other hand,1011is not good, because the property is false for011.
Given a pattern of length $$$n$$$ consisting of characters0,1and?, find the number of ways to replace question marks with0or1, such that the resulting binary string is good. Since the answer may be large, find it modulo $$$998\,244\,353$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^3$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$3 \le k \le n \le 10^5$$$, $$$k$$$ is odd). The second line contains $$$n$$$ characters0,1or?— the pattern.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^5$$$.

## Output
For each test case, print the number of ways to replace?with0or1such that the resulting string is good, modulo $$$998\,244\,353$$$.