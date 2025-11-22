# Problem Description

You are given a binary string $$$s_1s_2 \ldots s_n$$$ of length $$$n$$$. A string $$$s$$$ is called binary if it consists only of zeros and ones.
For a string $$$p$$$, we define the function $$$f(p)$$$ as the maximum number of occurrences of any character in the string $$$p$$$. For example, $$$f(00110) = 3$$$, $$$f(01) = 1$$$.
You need to find the sum $$$f(s_ls_{l+1} \ldots s_r)$$$ for all pairs $$$1 \leq l \leq r \leq n$$$.

## Input
Each test consists of multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases. Then follows their descriptions.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 2 \cdot 10^5$$$) — the length of the binary string.
The second line of each test case contains a string of length $$$n$$$, consisting of $$$0$$$s and $$$1$$$s — the binary string $$$s$$$.
It is guaranteed that the sum of $$$n$$$ across all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output the sum $$$f(s_ls_{l+1} \ldots s_r)$$$ for all pairs $$$1 \leq l \leq r \leq n$$$.