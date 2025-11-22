# Problem Description

Call a permutation$$$^{\text{∗}}$$$ $$$p$$$ of length $$$n$$$goodif $$$\gcd(p_i, i)$$$$$$^{\text{†}}$$$ $$$ > 1$$$ for all $$$2 \leq i \leq n$$$. Find a good permutation with theminimumnumber offixed points$$$^{\text{‡}}$$$ across all good permutations of length $$$n$$$. If there are multiple such permutations, print any of them.
$$$^{\text{∗}}$$$ A permutation of length $$$n$$$ is an array that contains every integer from $$$1$$$ to $$$n$$$ exactly once, in any order.
$$$^{\text{†}}$$$$$$\gcd(x, y)$$$ denotes thegreatest common divisor (GCD)of $$$x$$$ and $$$y$$$.
$$$^{\text{‡}}$$$Afixed pointof a permutation $$$p$$$ is an index $$$j$$$ ($$$1\leq j\leq n$$$) such that $$$p_j = j$$$.

## Input
The first line contains an integer $$$t$$$ ($$$1 \leq t \leq 10^4$$$)  — the number of test cases.
The only line of each test case contains an integer $$$n$$$ ($$$2 \leq n \leq 10^5$$$) — the length of the permutation.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^5$$$.

## Output
For each test case, output on a single line an example of a good permutation of length $$$n$$$ with the minimum number of fixed points.