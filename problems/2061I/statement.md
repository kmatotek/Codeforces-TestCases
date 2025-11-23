# Problem Description


Kevin and Nivek are competing for the title of "The Best Kevin". They aim to determine the winner through $$$n$$$ matches.
The $$$i$$$-th match can be one of two types:
Kevin wants to know the minimum amount of time he needs to spend to ensure he wins at least $$$k$$$ matches.
Output the answers for $$$k = 0, 1, \ldots, n$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 3 \cdot 10^5$$$) — the number of matches.
The second line contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$-1 \leq a_i \leq 10^9$$$).
If $$$a_i = -1$$$, the $$$i$$$-th match is ofType 2. Otherwise, the $$$i$$$-th match is ofType 1, and $$$a_i$$$ represents the amount of time Kevin needs to spend to win this match.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$3 \cdot 10^5$$$.

## Output
For each test case, output $$$n + 1$$$ integers. The $$$i$$$-th integer represents the minimum amount of time to win at least $$$i-1$$$ matches.