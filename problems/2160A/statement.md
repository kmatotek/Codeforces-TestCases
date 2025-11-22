# Problem Description


Let apartitionof a multiset $$$B$$$ be a collection of multisets $$$s_1, s_2,\ldots, s_k$$$ such that each element appears the same number of times in $$$B$$$ and across all of $$$s_1,s_2,\ldots,s_k$$$.
For example, some partitions of $$$\{1,2,3,3\}$$$ include $$$\{1,3\}+\{2,3\}, \{1,2,3,3\}$$$, and $$$\{2\}+\{1,3\}+\{3\}$$$, but not $$$\{1,2\}+\{3\}$$$.
A partition is calledvalidif the $$$\operatorname{mex}$$$$$$^{\text{∗}}$$$ of all multisets in the partition is the same. Thescoreof a valid partition is the $$$\operatorname{mex}$$$ of any multiset in the partition.
You are given a multiset $$$A$$$ of size $$$n$$$. Find theminimumscoreover all valid partitions of $$$A$$$.
$$$^{\text{∗}}$$$The minimum excluded (MEX) of a collection of integers $$$c_1, c_2, \ldots, c_k$$$ is defined as the smallest non-negative integer $$$x$$$ which does not occur in the collection $$$c$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 100$$$). The description of the test cases follows.
The first line of each test case contains an integer $$$n$$$ ($$$1 \leq n \leq 100$$$).
The second line contains $$$n$$$ integers $$$A_1, A_2, \ldots, A_n$$$ denoting the elements of $$$A$$$ ($$$0 \leq A_i \leq 100$$$).
It isnot guaranteedthat the elements are given in non-decreasing order.

## Output
For each test case, output the minimumscoreover all valid partitions.