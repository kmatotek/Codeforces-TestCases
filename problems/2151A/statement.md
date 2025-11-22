# Problem Description

James is learning numbers, and he is having fun writing them on a huge blackboard, from left to right.
For example, for $$$n = 5$$$, the numbers written by James make the array $$$b = [1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5]$$$.
James has a list of favorite numbers $$$a_1, a_2, \ldots, a_m$$$, and he wants to calculate how many subarrays of the array $$$b$$$ are equal to $$$a_1, a_2, \ldots, a_m$$$. $$$^{\text{∗}}$$$
James is already sure that $$$a_1, a_2, \ldots, a_m$$$ is a subarray of $$$b$$$, so the answer is at least $$$1$$$.
$$$^{\text{∗}}$$$The subarrays of an array $$$[v_1, v_2, \ldots, v_k]$$$ are generated as follows: for each $$$l, r$$$ such that $$$1 \leq l \leq r \leq k$$$, the array $$$[v_l, v_{l+1}, \ldots, v_r]$$$ is a subarray. So there are $$$k(k+1)/2$$$ subarrays in total, and some of them may be equal.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 500$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$1 \leq n \leq 10^5$$$, $$$1 \leq m \leq 200$$$) — the maximum number written by James, and the length of the array $$$a_1, a_2, \ldots, a_m$$$.
The second line of each test case contains $$$m$$$ integers $$$a_1, a_2, \ldots, a_m$$$ ($$$1 \leq a_i \leq 10^5$$$) — James' favorite numbers.
It is guaranteed that for the given input, the answer is always at least $$$1$$$.
Note that there are no constraints on the sum of $$$n$$$ and $$$m$$$ over all test cases.

## Output
For each test case, output a single line containing an integer: the number of subarrays of the array $$$b$$$ which are equal to $$$a_1, a_2, \ldots, a_m$$$.