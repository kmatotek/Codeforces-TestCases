# Problem Description


You are given a full binary tree$$$^{\text{∗}}$$$ of $$$n$$$ nodes, rooted at node $$$1$$$. For each node $$$u$$$ ($$$1\le u\le n$$$), we define function $$$f_u : \mathbb R_+ \to \mathbb R_+$$$ as follows:
For two nodes $$$u$$$ and $$$v$$$, we say $$$u\prec v$$$ if and only if one of the following holds:
It can be shown that for any two distinct nodes $$$u$$$ and $$$v$$$, either $$$u\prec v$$$ or $$$v\prec u$$$ holds.
You have to sort the nodes by order $$$\prec$$$. Formally, you need to find a permutation$$$^{\text{§}}$$$ $$$p$$$ of length $$$n$$$, such that for every $$$1\le i<n$$$, $$$p_i\prec p_{i+1}$$$.
$$$^{\text{∗}}$$$A full binary tree is a rooted tree, in which each node has $$$0$$$ or $$$2$$$ children.
$$$^{\text{†}}$$$A leaf is any vertex without children.
$$$^{\text{‡}}$$$Here, $$$f_u(x) < f_v(x)$$$ when $$$x\to\infty$$$ is equivalent to the following description: there exists a positive number $$$N$$$ such that for all $$$x > N$$$, $$$f_u(x) < f_v(x)$$$ holds. The same is defined for $$$f_u(x) = f_v(x)$$$ when $$$x\to \infty$$$.
$$$^{\text{§}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1\le n \le 4\cdot 10^5$$$, $$$n$$$ is odd) — the size of the full binary tree.
Then $$$n$$$ lines follow, the $$$i$$$-th line containing two integers $$$l_i$$$ and $$$r_i$$$ ($$$0\le l_i, r_i\le n$$$) — the left child and the right child of node $$$i$$$. If $$$i$$$ is a leaf, then $$$l_i=r_i=0$$$. It is guaranteed that the given input forms a full binary tree rooted at node $$$1$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$4\cdot 10^5$$$.

## Output
For each test case, output $$$n$$$ integers $$$p_1, p_2, \ldots, p_n$$$ ($$$1\le p_i\le n$$$, all $$$p_i$$$ are distinct) — the permutation you found. You need to guarantee that for each $$$1\le i < n$$$, $$$p_i\prec p_{i+1}$$$.