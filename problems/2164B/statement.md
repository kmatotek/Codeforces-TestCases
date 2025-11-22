# Problem Description


You are given astrictly increasingsequence of positive integers $$$a_1 < a_2 < \ldots < a_n$$$. Find two distinct elements $$$x$$$ and $$$y$$$ from the sequence such that $$$x < y$$$ and $$$y \bmod x$$$ is even, or determine that no such pair exists.
$$$p \bmod q$$$ denotes the remainder from dividing $$$p$$$ by $$$q$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 2\cdot 10^4$$$). The description of the test cases follows.
The first line of each test case contains one integer $$$n$$$ ($$$2 \le n \le 10^5$$$) — the length of the sequence.
The second line of each test case contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$1\le a_1 < \ldots < a_n\le 10^9$$$) — the given sequence.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^5$$$.

## Output
For each test case:
If there are multiple valid pairs, you may output any of them.