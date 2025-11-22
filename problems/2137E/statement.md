# Problem Description


You are given an array $$$a$$$ of size $$$n$$$ and an integer $$$k$$$. You do the following procedure $$$k$$$ times:
Please find the sum of elements in the array after all $$$k$$$ operations.
$$$^{\text{∗}}$$$The minimum excluded (MEX) of a collection of integers $$$d_1, d_2, \ldots, d_k$$$ is defined as the smallest non-negative integer $$$x$$$ which does not occur in the collection $$$d$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line contains two integers $$$n$$$ and $$$k$$$ ($$$2 \leq n \leq 2\cdot 10^5, 1 \leq k \leq 10^9$$$) – the number of elements in $$$a$$$ and the number of operations done.
The second line contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$0 \leq a_i \leq n$$$).
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2\cdot 10^5$$$.

## Output
For each test case, output the sum of elements after all $$$k$$$ operations on a new line.