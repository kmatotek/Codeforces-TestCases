# Problem Description


This is an interactive problem.
There is a hidden permutation$$$^{\text{∗}}$$$ $$$p$$$ of length $$$n$$$. You are allowed to interact with it by asking the following query at most $$$2n$$$ times:
Important: You cannot make queries involving the last element $$$p_n$$$ (because $$$i\le n - 1$$$).
Your goal is to determine the value of the last element of the permutation, $$$p_n$$$, using at most $$$2n$$$ queries.
Note that the interactor is non-adaptive. This means that the hidden permutation $$$p$$$ is fixed at the beginning and will not change based on your queries.
$$$^{\text{∗}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).
$$$^{\text{†}}$$$$$$\&$$$ denotes thebitwise AND operation.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^3$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$2 \leq n \leq 2 \cdot 10^4$$$) — the length of permutation $$$p$$$.
For each test case, after reading $$$n$$$, you should begin the interaction and find the answer before proceeding to the next test case.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^4$$$.
