# Problem Description

For two integers $$$a$$$ and $$$b$$$, we define $$$f(a, b)$$$ as the number of positions in the decimal representation of the numbers $$$a$$$ and $$$b$$$ where their digits are the same. For example, $$$f(12, 21) = 0$$$, $$$f(31, 37) = 1$$$, $$$f(19891, 18981) = 2$$$, $$$f(54321, 24361) = 3$$$.
You are given two integers $$$l$$$ and $$$r$$$ of thesamelength in decimal representation. Consider all integers $$$l \leq x \leq r$$$. Your task is to find the minimum value of $$$f(l, x) + f(x, r)$$$.

## Input
Each test consists of multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \leq t \leq 10^4$$$) — the number of test cases. The description of the test cases follows.
Each test case consists of a single line containing two integers $$$l$$$ and $$$r$$$ ($$$1 \leq l \leq r < 10^9$$$).
It is guaranteed that the numbers $$$l$$$ and $$$r$$$ have the same length in decimal representation and do not have leading zeros.

## Output
For each test case, output the minimum value of $$$f(l, x) + f(x, r)$$$ among all integer values $$$l \leq x \leq r$$$.