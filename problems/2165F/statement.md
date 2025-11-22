# Problem Description


You are given a permutation$$$^{\text{∗}}$$$ $$$a_1,a_2,\ldots,a_n$$$ of length $$$n$$$.
An interval $$$[l,r]$$$ ($$$1\le l\le r\le n$$$) isjaggedif and only if it contains a 21435-subsequence; that is, there exist integers $$$i_1,i_2,i_3,i_4,i_5$$$ such that $$$l\le i_1<i_2<i_3<i_4<i_5\le r$$$, and $$$a_{i_2}<a_{i_1}<a_{i_4}<a_{i_3}<a_{i_5}$$$.
Your task is to calculate how many of the $$$\frac{n(n+1)}2$$$ intervals arejagged.
$$$^{\text{∗}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1\le n\le10^6$$$) — the length of the permutation.
The second line of each test case contains $$$n$$$ distinct integers $$$a_1,a_2,\ldots,a_n$$$ ($$$1\le a_i\le n$$$).
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^6$$$.

## Output
For each test case, output the number ofjaggedsubarrays.