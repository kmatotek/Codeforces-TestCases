# Problem Description

You are given an array of integers $$$a_1,a_2,\dots,a_n$$$. A tournament is held with $$$n$$$ players. Player $$$i$$$ has strength $$$a_i$$$.
While more than $$$k$$$ players remain,
Given integers $$$j$$$ and $$$k$$$ ($$$1 \leq j,k \leq n$$$), determine if there is any way for player $$$j$$$ to be one of the last $$$k$$$ remaining players.

## Input
The first line contains an integer $$$t$$$ ($$$1 \leq t \leq 10^4$$$)  — the number of test cases.
The first line of each test case contains three integers $$$n$$$, $$$j$$$, and $$$k$$$ ($$$2\leq n \leq 2\cdot 10^5$$$, $$$1\leq j, k\leq n$$$).
The second line of each test case contains $$$n$$$ integers, $$$a_1,a_2,\dots,a_n$$$ ($$$1\leq a_i\leq n$$$).
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2\cdot 10^5$$$.

## Output
For each test case, output on a single line "YES" if player $$$j$$$ can be one of the last $$$k$$$ remaining players, and "NO" otherwise.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.