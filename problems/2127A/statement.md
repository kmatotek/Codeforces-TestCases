# Problem Description


You are given an array $$$a$$$ consisting of $$$n$$$ non-negative integers. However, some elements of $$$a$$$ are missing, and they are represented by $$$−1$$$.
We define that the array $$$a$$$ isgoodif and only if the following holds for every $$$1 \leq i \leq n-2$$$:
$$$$$$ \operatorname{mex}([a_i, a_{i+1}, a_{i+2}]) = \max([a_i, a_{i+1}, a_{i+2}]) - \min([a_i, a_{i+1}, a_{i+2}]), $$$$$$
where $$$\operatorname{mex}(b)$$$ denotes the minimum excluded (MEX)$$$^{\text{∗}}$$$ of the integers in $$$b$$$.
You have to determine whether you can make $$$a$$$goodafter replacing each $$$-1$$$ in $$$a$$$ with a non-negative integer.
$$$^{\text{∗}}$$$The minimum excluded (MEX) of a collection of integers $$$b_1, b_2, \ldots, b_k$$$ is defined as the smallest non-negative integer $$$x$$$ which does not occur in the collection $$$b$$$.  For example, $$$\operatorname{mex}([2,2,1])=0$$$ because $$$0$$$ does not belong to the array, and $$$\operatorname{mex}([0,3,1,2])=4$$$ because $$$0$$$, $$$1$$$, $$$2$$$, and $$$3$$$ appear in the array, but $$$4$$$ does not.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 500$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$3 \leq n \leq 100$$$) — the length of $$$a$$$.
The second line contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$-1 \leq a_i \leq 100$$$) — the elements of $$$a$$$. $$$a_i = -1$$$ denotes that this element is missing.

## Output
For each test case, output "YES" if it is possible to make $$$a$$$good, and "NO" otherwise.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.