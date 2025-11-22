# Problem Description


We define that ablockis an array where all elements in it are equal to the length of the array. For example, $$$[3, 3, 3]$$$, $$$[1]$$$, and $$$[4, 4, 4, 4]$$$ areblocks, while $$$[1, 1, 1]$$$ and $$$[2, 3, 3]$$$ are not.
An array is calledneatif it can be obtained by the concatenation of an arbitrary number ofblocks(possibly zero). Note that an empty array is alwaysneat.
You are given an array $$$a$$$ consisting of $$$n$$$ integers. Find the length of its longestneatsubsequence$$$^{\text{∗}}$$$.
$$$^{\text{∗}}$$$A sequence $$$c$$$ is a subsequence of a sequence $$$a$$$ if $$$c$$$ can be obtained from $$$a$$$ by the deletion of several (possibly, zero or all) element from arbitrary positions.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains an integer $$$n$$$ ($$$1 \le n \le 2\cdot 10^5$$$) — the length of $$$a$$$.
The second line contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$1 \le a_i \le n$$$) — the elements of $$$a$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2\cdot 10^5$$$.

## Output
For each test case, output a single integer — the length of the longestneatsubsequence of $$$a$$$.