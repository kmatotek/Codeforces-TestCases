# Problem Description

For an array $$$b$$$ of length $$$m$$$, define $$$f(b)$$$ as follows.
Consider a $$$1 \times m$$$ strip, where all cells initially have darkness $$$0$$$. You want to transform it into a strip where the color at the $$$i$$$-th position has darkness $$$b_i$$$. You can perform the following operation, which consists of two steps:
Let $$$f(b)$$$ be the minimum number of operations required to achieve the desired configuration. It can be proven that the goal can always be achieved in a finite number of operations.
You are given an array $$$a$$$ of length $$$n$$$. Evaluate
$$$$$$\sum_{l=1}^n\sum_{r=l}^n f(a_l a_{l+1} \ldots a_r)$$$$$$
modulo $$$998\,244\,353$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \leq n \leq 2 \cdot 10^5$$$) — the length of the array $$$a$$$.
The second line contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$0 \leq a_i \leq 10^9$$$) — denoting the array $$$a$$$.
It is guaranteed that the sum of all values of $$$n$$$ across all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output a single integer — the required sum modulo $$$998\,244\,353$$$.