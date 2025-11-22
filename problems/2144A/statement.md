# Problem Description

You are given an array of $$$n$$$ non-negative integers $$$[a_1, a_2, \dots, a_n]$$$.
Your task is to cut it into three non-empty parts: a prefix, a middle part, and a suffix. Formally, you need to choose two integers $$$l$$$ and $$$r$$$ such that $$$1 \le l < r < n$$$, and obtain three parts:
Let $$$s_1, s_2, s_3$$$ be the remainders of the sums of these parts modulo $$$3$$$. In other words:
Your task is to find such boundaries $$$l$$$ and $$$r$$$ that either all numbers $$$s_1, s_2, s_3$$$ are different, or all numbers $$$s_1, s_2, s_3$$$ are the same.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases.
Each test case consists of two lines:

## Output
For each test case, if a suitable pair of integers $$$l$$$ and $$$r$$$ ($$$1 \le l < r < n$$$) exists, output these two integers (if there are multiple suitable pairs, you can output any of them). Otherwise, output two integers equal to $$$0$$$.