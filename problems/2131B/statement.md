# Problem Description


You are given an integer $$$n$$$. Call an array $$$a$$$ of length $$$n$$$goodif:
Additionally, we say a good array $$$a$$$ of length $$$n$$$ isbetterthan another good array $$$b$$$ of length $$$n$$$ if $$$[|a_1|, |a_2|, \ldots, |a_n|]$$$ is lexicographically smaller$$$^{\text{‡}}$$$ than $$$[|b_1|, |b_2|, \ldots, |b_n|]$$$. Note that $$$|z|$$$ denotes theabsolute valueof integer $$$z$$$.
Output a good array of length $$$n$$$ such that it is better than every other good array of length $$$n$$$.
$$$^{\text{∗}}$$$An array $$$c$$$ is a subarray of an array $$$d$$$ if $$$c$$$ can be obtained from $$$d$$$ by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.
$$$^{\text{†}}$$$An integer $$$x$$$ is positive if $$$x > 0$$$.
$$$^{\text{‡}}$$$A sequence $$$a$$$ is lexicographically smaller than a sequence $$$b$$$ if and only if one of the following holds:

## Input
The first line contains an integer $$$t$$$ ($$$1 \leq t \leq 500$$$) — the number of test cases.
The single line of each test case contains one integer $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$) — the length of your array.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$-10^9 \leq a_i \leq 10^9$$$), the elements of your array on a new line.