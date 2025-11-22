# Problem Description


We say that an array $$$a$$$ of size $$$n$$$ isbadif and only if there exists $$$1 \leq i \leq n - 4$$$ such that one of the following conditions holds:
An array isgoodif and only if it's notbad. For example:
You're given a permutation$$$^{\text{∗}}$$$ $$$p_1, p_2, \ldots, p_n$$$.
You must perform $$$n$$$ turns. At each turn, you must remove either the leftmost or the rightmost remaining element in $$$p$$$. Let $$$q_i$$$ be the element removed at the $$$i$$$-th turn.
Choose which element to remove at each turn so that the resulting array $$$q$$$ isgood. We can show that under the given constraints, it's always possible.
$$$^{\text{∗}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10\,000$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$5 \leq n \leq 100\,000$$$) — the length of the array.
The second line of each test case contains $$$n$$$ integers $$$p_1, p_2, \ldots, p_n$$$ ($$$1 \leq p_i \leq n$$$, $$$p_i$$$ are pairwise distinct) — elements of the permutation.
It is guaranteed that the sum of $$$n$$$ over all test cases doesn't exceed $$$200\,000$$$.

## Output
For each test case, you must output a string $$$s$$$ of length $$$n$$$. For every $$$1 \leq i \leq n$$$, at the $$$i$$$-th turn:
We can show that an answer always exists. If there are multiple solutions, print any of them.