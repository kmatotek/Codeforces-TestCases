# Problem Description


You are given an integer $$$n$$$ and a binary string$$$^{\text{∗}}$$$ $$$s$$$ of length $$$n$$$.
For a permutation$$$^{\text{†}}$$$ $$$p$$$ of length $$$n$$$ and an integer $$$x$$$, we define $$$\text{find}(x)$$$ as in the following pseudocode:
We call an integer $$$x$$$ ($$$1\le x\le n$$$)stableif and only if $$$\text{find}(x)$$$ isalwaysnot undefined and $$$p_{\text{find}(x)}=x$$$alwaysholds, no matter how the value of $$$m$$$ is selected in the process of the pseudocode.
You have to construct a permutation $$$p$$$ of length $$$n$$$, such that:
Or determine that no such permutation exists.
$$$^{\text{∗}}$$$A binary string is a string where each character is either $$$\mathtt{0}$$$ or $$$\mathtt{1}$$$.
$$$^{\text{†}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$2\le n \le 2\cdot 10^5$$$) — the length of the permutation.
The second line contains the binary string $$$s$$$ of length $$$n$$$ ($$$s_i=\mathtt{0}$$$ or $$$\mathtt{1}$$$).
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2\cdot 10^5$$$.

## Output
For each test case:
You can output the token in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
If there are multiple answers, you may print any of them.