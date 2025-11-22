# Problem Description

Recall that a permutation of length $$$n$$$ is a sequence of length $$$n$$$ such that each integer from $$$1$$$ to $$$n$$$ appears in it exactly once.
Let's define the cost of a permutation as the minimum length of its contiguous subsegment (possibly empty) that needs to be sorted so that the entire permutation becomes sorted in ascending order.
You are given an integer array $$$p$$$ consisting of integers from $$$0$$$ to $$$n$$$, where no positive (strictly greater than zero) integer appears more than once. You should replace zeros with integers so that the array $$$p$$$ becomes a permutation.
Your task is to calculate the maximum possible cost of the resulting permutation.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 2 \cdot 10^5$$$).
The second line contains $$$n$$$ integers $$$p_1, p_2, \dots, p_n$$$ ($$$0 \le p_i \le n$$$). No positive integer appears more than once in this sequence.
Additional constraint on the input: the sum of $$$n$$$ over all test cases doesn't exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, print a single integer — the maximum possible cost of the resulting permutation.