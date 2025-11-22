# Problem Description


You are given four positive integers $$$n, l, r, k$$$. You need to find the lexicographically smallest$$$^{\text{∗}}$$$ array $$$a$$$ of length $$$n$$$, consisting of integers, such that:
If no such array exists, output $$$-1$$$. Otherwise, since the entire array might be too large to output, output $$$a_k$$$ only.
$$$^{\text{∗}}$$$An array $$$a$$$ is lexicographically smaller than an array $$$b$$$ if and only if one of the following holds:

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
Each test case contains four positive integers $$$n,l,r,k$$$ ($$$1 \le k \le n \le 10^{18}$$$, $$$1 \le l \le r \le 10^{18}$$$).

## Output
For each test case, output $$$a_k$$$ or $$$-1$$$ if no array meets the conditions.