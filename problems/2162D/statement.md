# Problem Description

This is an interactive problem.
There is apermutation$$$^{\text{∗}}$$$ $$$p$$$ of length $$$n$$$.
Someone secretly chose two integers $$$l, r$$$ ($$$1 \le l \le r \le n$$$) and modified the permutation in the following way:
Let $$$a$$$ denote the resulting array obtained by modifying the permutation.
You are given an integer $$$n$$$ denoting the length of the permutation $$$p$$$.
In one query, you are allowed to choose two integers $$$l, r$$$ ($$$1 \le l \le r \le n$$$) and ask for the sum of the subarray either of the original permutation $$$p[l \dots r]$$$ or of the modified array $$$a[l \dots r]$$$. The answer to such a query will be the corresponding integer sum.
Your task is to find the pair $$$(l, r)$$$ that was chosen to obtain $$$a$$$ in no more than $$$\bf{40}$$$ queries.
$$$^{\text{∗}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in any order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation (the number $$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$, but the array contains $$$4$$$).

## Input
The first line of input contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
Each test case contains a single integer $$$n$$$ ($$$1 \le n \le 2\cdot10^4$$$) — the length of the permutation.
It is guaranteed that the sum of $$$n$$$ over all the test cases does not exceed $$$2\cdot10^4$$$.
