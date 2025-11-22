# Problem Description

You are given a binary$$$^{\text{∗}}$$$ string $$$s$$$ of length $$$n$$$.
Your task is to find any subsequence$$$^{\text{†}}$$$ $$$p$$$ of $$$s$$$ such that:
You only need to output any valid subsequence $$$p$$$ that satisfies both conditions. If no such subsequence exists, output $$$-1$$$.
Note that an empty string is both non-decreasing and a palindrome.
$$$^{\text{∗}}$$$A binary string is a string consisting of characters '0' and '1'.
$$$^{\text{†}}$$$Asubsequenceof a string $$$s = s_1s_2\ldots s_n$$$ is a sequence $$$p = s_{i_1}s_{i_2}\ldots s_{i_k}$$$ such that $$$1 \leq i_1 < i_2 < \ldots < i_k \leq n$$$. The characters are selected in order, but not necessarily contiguously. Note that an empty string is a subsequence of any string.
$$$^{\text{‡}}$$$A string $$$t = t_1t_2\ldots t_m$$$ is apalindromeif $$$t_i = t_{m - i + 1}$$$ for all $$$1 \leq i \leq m$$$. In other words, the string reads the same forward and backward.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 3000$$$) — the number of test cases.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 10$$$) — the length of the string.
The second line contains a binary string $$$s$$$ of length $$$n$$$.

## Output
If a solution exists:
Otherwise, print a single line containing $$$-1$$$.