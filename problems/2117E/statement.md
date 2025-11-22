# Problem Description

You are given two integer arrays $$$a$$$ and $$$b$$$, each of length $$$n$$$.
You may perform the following operation any number of times:
Beforeperforming any operations, you are allowed to choose an index $$$i$$$ $$$(1 \le i \le n)$$$ and remove both $$$a_i$$$ and $$$b_i$$$ from the arrays. This removal can be doneat most once.
Let the number of matches between two arrays $$$c$$$ and $$$d$$$ of length $$$m$$$ be the number of positions $$$j$$$ $$$(1 \le j \le m)$$$ such that $$$c_j = d_j$$$.
Your task is to compute the maximum number of matches you can achieve.

## Input
The first line of the input contains an integer $$$t$$$ $$$(1 \le t \le 10^4)$$$ — the number of test cases. The description of each test case follows.
The first line contains an integer $$$n$$$ $$$(2 \le n \le 2 \cdot 10^5)$$$ — the length of $$$a$$$ and $$$b$$$.
The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ $$$(1 \le a_i \le n)$$$ — the elements of $$$a$$$.
The third line contains $$$n$$$ integers $$$b_1, b_2, \dots, b_n$$$ $$$(1 \le b_i \le n)$$$ — the elements of $$$b$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, print a single integer — the answer for the test case.