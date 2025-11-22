# Problem Description


You are given a tree consisting of $$$n$$$ vertices, numbered from $$$1$$$ to $$$n$$$. Each of the $$$n - 1$$$ edges is associated with two non-negative integers $$$x$$$ and $$$y$$$.
Consider a permutation$$$^{\text{∗}}$$$ $$$p$$$ of the integers $$$1$$$ through $$$n$$$, where $$$p_i$$$ represents the value assigned to vertex $$$i$$$.
For an edge $$$(u, v)$$$, such that $$$u < v$$$ with associated values $$$x$$$ and $$$y$$$, itscontributionis defined as follows: $$$$$$ \begin{cases} x & \text{if } p_u > p_v, \\ y & \text{otherwise.} \end{cases} $$$$$$
Thevalueof the permutation is the sum of the contributions from all edges.
Your task is to find any permutation $$$p$$$ thatmaximizesthis total value.
$$$^{\text{∗}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line contains a single integer $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$) — the number of vertices in the tree.
Each of the next $$$n - 1$$$ lines contains four integers $$$u$$$, $$$v$$$, $$$x$$$, and $$$y$$$ ($$$1 \le u < v \le n$$$, $$$1 \le x, y \le 10^9$$$) — describing an edge between vertices $$$u$$$ and $$$v$$$ with associated values $$$x$$$ and $$$y$$$. It is guarranteed that the given edges form a tree.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, you must output a permutation $$$p$$$ of the integers $$$1$$$ through $$$n$$$ that maximizes the total value as defined in the problem. If there are multiple answers, you can print any of them.