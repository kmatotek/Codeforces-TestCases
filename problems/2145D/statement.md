# Problem Description

A permutation of length $$$n$$$ is an array of $$$n$$$ integers, where each number from $$$1$$$ to $$$n$$$ appears exactly once. Aninversionin a permutation $$$p$$$ is a pair of indices $$$(i, j)$$$ such that $$$i < j$$$ and $$$p_i > p_j$$$.
For a permutation $$$p$$$, we define itsinversion valueas the number of its subsegments that contain at least one inversion. Formally, this is the number of pairs of integers $$$(l, r)$$$ ($$$1 \le l < r \le n$$$) for which there exists a pair of indices $$$(i, j)$$$ satisfying the following conditions: $$$l \le i < j \le r$$$ and $$$p_i > p_j$$$.
For example, for the permutation $$$[3, 1, 4, 2]$$$, the inversion value is $$$5$$$.
You are given two integers $$$n$$$ and $$$k$$$. Your task is to construct a permutation of length $$$n$$$ with aninversion value equal to exactly $$$k$$$.

## Input
The first line contains one integer $$$t$$$ ($$$1 \le t \le 500$$$) — the number of test cases.
Each test case consists of a single line containing two integers $$$n$$$ and $$$k$$$ ($$$2 \le n \le 30$$$; $$$0 \le k \le \dfrac{n(n-1)}{2}$$$).

## Output
For each test case, output the answer as follows: