# Problem Description


You are given a binary string$$$^{\text{∗}}$$$ $$$s$$$ of length $$$n$$$, as well as an integer $$$k$$$.
Aquawave wants to construct a permutation$$$^{\text{†}}$$$ $$$p$$$ of length $$$n$$$, so that for each $$$1\le i\le n$$$, where $$$s_i=\mathtt{1}$$$, the following holds:
Note that there arenosuch constraints on indices with $$$s_i = \mathtt{0}$$$.
You have to find such a permutation, or determine that such permutations do not exist.
$$$^{\text{∗}}$$$A binary string is a string where each character is either $$$\mathtt{0}$$$ or $$$\mathtt{1}$$$.
$$$^{\text{†}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$1 \leq n \leq 2 \cdot 10^5$$$, $$$1 \leq k \leq n$$$) — the length of $$$s$$$ and the integer in the statements.
The second line contains the binary string $$$s$$$ of length $$$n$$$ ($$$s_i = \mathtt{0}$$$ or $$$\mathtt{1}$$$).
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case:
You can output the tokens in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
If there are multiple answers, you may output any of them.