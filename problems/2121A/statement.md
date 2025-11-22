# Problem Description

You are given an array of distinct integers $$$x_1, x_2, \ldots, x_n$$$ and an integer $$$s$$$.
Initially, you are at position $$$pos = s$$$ on the $$$X$$$ axis. In one step, you can perform exactly one of the following two actions:
A sequence of steps will be considered successful if, during the entire journey, you visit each position $$$x_i$$$ on the $$$X$$$ axis at least once. Note that the initial position $$$pos = s$$$ is also considered visited.
Your task is to determine the minimum number of steps in any successful sequence of steps.

## Input
Each test consists of multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \leq t \leq 1000$$$) — the number of test cases. The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$s$$$ ($$$1 \leq n \leq 10$$$, $$$1 \leq s \leq 100$$$) — the number of positions to visit and the starting position.
The second line of each test case contains $$$n$$$ integers $$$x_1, x_2, \ldots, x_n$$$ ($$$1 \leq x_i \leq 100$$$). It is guaranteed that for all $$$1 \leq i < n$$$, it holds that $$$x_i < x_{i + 1}$$$.

## Output
For each test case, output the minimum number of steps in any successful sequence of steps.