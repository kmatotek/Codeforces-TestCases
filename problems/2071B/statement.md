# Problem Description


A permutation $$$p$$$ of length $$$n$$$$$$^{\text{∗}}$$$ isperfectif, for each index $$$i$$$ ($$$1 \le i \le n$$$), it satisfies the following:
You would like things to be perfect. Given a positive integer $$$n$$$, find aperfectpermutation of length $$$n$$$, or print $$$-1$$$ if none exists.
$$$^{\text{∗}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).
$$$^{\text{†}}$$$A perfect square is an integer that is the square of an integer, e.g., $$$9=3^2$$$ is a perfect square, but $$$8$$$ and $$$14$$$ are not.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first and only line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 5 \cdot 10^5$$$).
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^6$$$.

## Output
For each test case:
If there are multiple solutions, print any of them.