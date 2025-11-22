# Problem Description


We call an arraybalancedif and only if the numbers of occurrences of any of its elements are the same. For example, $$$[1,1,3,3,6,6]$$$ and $$$[2,2,2,2]$$$ arebalanced, but $$$[1,2,3,3]$$$ is notbalanced(the numbers of occurrences of elements $$$1$$$ and $$$3$$$ are different). Note that an empty array is alwaysbalanced.
You are given a non-decreasing array $$$a$$$ consisting of $$$n$$$ integers. Find the length of its longestbalancedsubsequence$$$^{\text{∗}}$$$.
$$$^{\text{∗}}$$$A sequence $$$b$$$ is a subsequence of a sequence $$$a$$$ if $$$b$$$ can be obtained from $$$a$$$ by the deletion of several (possibly, zero or all) element from arbitrary positions.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 500$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \leq n \leq 100$$$) — the length of $$$a$$$.
The second line contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$1\le a_1\le a_2\le \cdots \le a_n\le n$$$) — the elements of $$$a$$$.

## Output
For each test case, output a single integer — the length of the longestbalancedsubsequence of $$$a$$$.