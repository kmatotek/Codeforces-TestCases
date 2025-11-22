# Problem Description


Let's define a function $$$f(a)$$$ for an array $$$a$$$ of length $$$n$$$ as $$$$$$f(a) = \textrm{cost} + (a_1 - a_2 + a_3 - a_4 \cdots a_n)$$$$$$ where $$$\textrm{cost}$$$ is zero initially.
Now consider the scenario where Alice and Bob are given an array $$$a$$$ of length $$$n$$$. They play a game taking at most $$$10^{100}$$$ turns alternately with Alice going first.
In each turn, they must perform anyone(only one) of the following operations:
Assume that Alice tries to maximize $$$f(a)$$$ and Bob tries to minimize it.
Your task is to determine the final value of $$$f(a)$$$ assuming both players play optimally.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 2\cdot10^5$$$) — the length of the array $$$a$$$.
The second line contains $$$n$$$ integers $$$a_1,a_2,a_3,\ldots,a_n$$$ ($$$1 \le a_i \le 10^9$$$) — the elements of the array $$$a$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2\cdot10^5$$$.

## Output
For each testcase, output a single integer — the final value of $$$f(a)$$$ assuming both players play optimally.