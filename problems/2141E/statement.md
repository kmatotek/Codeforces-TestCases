# Problem Description

You are given a string $$$s$$$ consisting of characters0,1, and/or?.
Let's call a binary (consisting of0and/or1) stringperfectif you can cut the string into two non-empty parts: a prefix $$$a$$$ and the suffix $$$b$$$, such that $$$a_i \ge b_i$$$ for each $$$i$$$ from $$$1$$$ to $$$\min(|a|, |b|)$$$.
Your task is to calculate the number of ways to replace all the question marks (independently) with zeros and ones so that the resulting string is perfect mod. Two ways are considered different if there exists at least one position that has different characters in these two ways. Since the answer can be large, print it modulo $$$998244353$$$.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The only line of each test case contains a string $$$s$$$ ($$$2 \le |s| \le 2 \cdot 10^5$$$), consisting of characters0,1, and/or?.
Additional constraint on the input: the sum of the lengths of the strings $$$s$$$ over all test cases doesn't exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, print a single integer — the number of ways to replace all the question marks (independently) with zeros and ones so that the resulting string is perfect, taken modulo $$$998244353$$$.