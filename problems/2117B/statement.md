# Problem Description

A shrink operation on an array $$$a$$$ of size $$$m$$$ is defined as follows:
Define thescoreof a permutation$$$^{\text{∗}}$$$ $$$p$$$ as themaximumnumber of times that you can perform the shrink operation on $$$p$$$.
Yousef has given you a single integer $$$n$$$. Construct a permutation $$$p$$$ of length $$$n$$$ with themaximumpossiblescore. If there are multiple answers, you can output any of them.
$$$^{\text{∗}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).

## Input
The first line of the input contains an integer $$$t$$$ ($$$1 \le t \le 10^3$$$) — the number of test cases.
Each test case contains an integer $$$n$$$ ($$$3 \le n \le 2 \cdot 10^5$$$) — the size of the permutation.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output any permutation $$$p_1, p_2, \dots, p_n$$$ that maximizes the number of shrink operations.