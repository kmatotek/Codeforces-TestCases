# Problem Description


Given an array $$$a$$$, define $$$f(a)$$$ as follows:
You are given $$$n$$$ integers $$$x_1,x_2,\ldots,x_n$$$. Please determine if there exists a permutation$$$^{\text{‡}}$$$ $$$a$$$ such that $$$f([a_1,a_2,\ldots,a_i])=x_i$$$ for each $$$1 \leq i \leq n$$$. If there is a permutation, print one. If there are multiple possible answers, you may output any one.
$$$^{\text{∗}}$$$An array $$$c$$$ is a subarray of an array $$$d$$$ if $$$c$$$ can be obtained from $$$d$$$ by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.
$$$^{\text{†}}$$$An array $$$c$$$ is lexicographically smaller than an array $$$d$$$ if and only if one of the following holds:
$$$^{\text{‡}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains an integer $$$n$$$ ($$$2 \leq n \leq 2\cdot 10^5$$$) — denoting the length of the array $$$x$$$.
The following line contains $$$n$$$ integers $$$x_1,x_2,\ldots,x_n$$$ ($$$1 \leq x_i \leq i$$$) — denoting the array $$$x$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2\cdot 10^5$$$.

## Output
For each test case, printYESif a permutation exists, andNOotherwise. Each letter may be outputted in uppercase or lowercase. You can output in any case (upper or lower). For example, the strings"yEs","yes","Yes", and"YES"will be recognized as positive responses.
If the answer is positive, output the permutation of $$$n$$$ numbers on the next line.