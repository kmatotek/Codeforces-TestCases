# Problem Description

Given two strings $$$s$$$ and $$$t$$$ of length $$$n$$$, you aim to transform $$$s$$$ into $$$t$$$ through a series of the following operations:
Your task is to achieve this transformation usingthe minimum number of operations. You also need to output the solution by printing the constructed string $$$s'$$$ after each operation. If the transformation cannot be achieved in less than or equal to $$$k_{\mathrm{max}}$$$ operations, output-1.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$, $$$k_{\mathrm{max}}$$$ ($$$1 \le n \cdot k_{\mathrm{max}} \le 10^6$$$) — the length of two strings and the maximum number of operations that can be used.
The second line of each test case contains one string $$$s$$$ of length $$$n$$$.
The third line of each test case contains one string $$$t$$$ of length $$$n$$$.
It is guaranteed that the sum of $$$nk_{\mathrm{max}}$$$ over all test cases does not exceed $$$10^6$$$.
It is guaranteed that both $$$s$$$ and $$$t$$$ consist of lowercase Latin letters.

## Output
For each test case:
If there are multiple solutions, output any.