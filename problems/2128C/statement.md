# Problem Description

Consider an array $$$a_1, \ldots, a_n$$$. Initially, $$$a_i = 0$$$ for every $$$i$$$.
You can do operations of the following form.
For example, if $$$a = [6, 8, 2, 1]$$$ and you choose $$$x = 6$$$, then $$$i$$$ will be equal to $$$3$$$ (since $$$a_1 \geq 6$$$, $$$a_2 \geq 6$$$, and $$$a_3 < 6$$$) and $$$a$$$ will become $$$[6, 8, 8, 1]$$$.
You can do as many operations as you want. Can you reach a target array $$$b_1, \ldots, b_n$$$?

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10\,000$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$2 \leq n \leq 200\,000$$$).
The second line of each test case contains $$$n$$$ integers $$$b_1, b_2, \ldots, b_n$$$ ($$$1 \le b_i \le 10^9$$$).
The sum of $$$n$$$ over all test cases does not exceed $$$200\,000$$$.

## Output
For each test case, printYESif you can reach the target array andNOotherwise.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.