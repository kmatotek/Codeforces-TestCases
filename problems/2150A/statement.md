# Problem Description

Hacks are disabled in this problem.
There is a strip containing $$$10^9$$$ cells, numbered from $$$1$$$ to $$$10^9$$$. Each cell is either black or white. Initially, $$$m$$$ distinct cells $$$a_1, a_2, \ldots, a_m$$$ are black, and the others are white.
If a person is on some cell $$$x$$$, he might be given two types of commands:
There is a string $$$s$$$ of length $$$n$$$, consisting of $$$n$$$ commands. For each $$$i$$$ from $$$1$$$ to $$$n$$$ in order, a person
You wonder which cells are black at the end of the process. Print them in increasing order.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$1 \leq n \leq 10^5$$$, $$$1 \leq m \leq 10^5$$$) — the number of commands and the number of black cells at the beginning.
The second line of each test case contains a string $$$s$$$ of length $$$n$$$, consisting of characters $$$\texttt{A}$$$ and $$$\texttt{B}$$$, representing the commands.
The third line of each test case contains $$$m$$$ integers $$$a_1, a_2, \ldots, a_m$$$ ($$$1 \leq a_1 < a_2 < \ldots < a_m \leq 10^9$$$) — the initial black cells.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^5$$$, and the sum of $$$m$$$ over all test cases does not exceed $$$10^5$$$.

## Output
For each test case, print two lines: