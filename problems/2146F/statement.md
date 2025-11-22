# Problem Description


You have just learned the algorithmbubble sort, which is able to sort an array in non-descending order. Let's define the function $$$\text{sort}(a)$$$ as in the following pseudocode:
As it is shown, the return value of $$$\text{sort}(a)$$$ represents the number of rounds needed to make array $$$a$$$ sorted in non-descending order by usingbubble sort.
You are given an integer $$$n$$$, as well as $$$m$$$ integer tuples $$$(k_i,l_i,r_i)$$$ ($$$1\le i\le m$$$). Count the number of permutations$$$^{\text{∗}}$$$ $$$p$$$ of length $$$n$$$, modulo $$$998\,244\,353$$$, so that the following restrictions are satisfied:
$$$^{\text{∗}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$2\leq n\leq 10^6$$$, $$$0\leq m\leq 1000$$$).
Then $$$m$$$ lines follow, the $$$i$$$-th line containing three integers $$$k_i$$$, $$$l_i$$$, and $$$r_i$$$ ($$$0\le k_i\le n - 1$$$, $$$1\le l_i\le r_i\le n$$$) — the restrictions.
It is guaranteed that the sum of $$$m^2$$$ over all test cases does not exceed $$$10^6$$$.

## Output
For each test case, output a single integer — the number of possible permutations, modulo $$$998\,244\,353$$$.