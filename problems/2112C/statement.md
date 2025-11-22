# Problem Description

Alice and Bob are playing a game using an integer array $$$a$$$ of size $$$n$$$.
Initially, all elements of the array are colorless. First, Alice chooses $$$3$$$ elements and colors them red. Then Bob chooses any element and colors it blue (if it was red — recolor it). Alice wins if the sum of the red elements is strictly greater than the value of the blue element.
Your task is to calculate the number of ways that Alice can choose $$$3$$$ elements in order to win regardless of Bob's actions.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases.
The first line of each test case contains a single integer $$$n$$$ ($$$3 \le n \le 5000$$$).
The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_1 \le a_2 \le \cdots \le a_n \le 10^5$$$).
Additional constraint on the input: the sum of $$$n$$$ over all test cases doesn't exceed $$$5000$$$.

## Output
For each test case, print a single integer — the number of ways that Alice can choose $$$3$$$ elements in order to win regardless of Bob's actions.