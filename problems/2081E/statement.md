# Problem Description

Given a rooted tree with $$$n+1$$$ nodes labeled from $$$0$$$ to $$$n$$$, where the root is node $$$0$$$, andits only child is node $$$1$$$. There are $$$m$$$distinctchips labeled from $$$1$$$ to $$$m$$$, each colored either black or white. Initially, they are arranged on edge $$$(0,1)$$$ from top to bottom in ascending order of labels.
You can perform the following operations any number of times (possibly zero) in any order:
Each chip $$$i$$$ has a movement range, defined as all edges on the simple path from the root to node $$$d_i$$$. During operations, you must ensure that no chip is moved to an edge outside its movement range.
Finally, you must move all chips back to edge $$$(0,1)$$$. It can be found that the order of the chips may change. Compute the number of possible permutations of chips for the final arrangement on the edge $$$(0,1)$$$ modulo $$$998\,244\,353$$$.
A permutation of chips is defined as a sequence of length $$$m$$$ consisting of thelabelsof the chips from top to bottom.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 5000$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$1 \le n, m \le 5000$$$) — the size of the tree minus one (i. e., the tree has $$$n+1$$$ nodes) and the number of chips.
The second line contains $$$n$$$ integers $$$p_1, p_2, \ldots, p_n$$$ ($$$0 \le p_i < i$$$) — the parent nodes for nodes from $$$1$$$ to $$$n$$$. It is guaranteed that $$$p_i = 0$$$ if and only if $$$i = 1$$$ (the root's only child is node $$$1$$$).
The third line contains $$$m$$$ integers $$$c_1, c_2, \ldots, c_m$$$ ($$$c_i \in \{0, 1\}$$$) — the color of each chip ($$$0$$$ for black, $$$1$$$ for white).
The fourth line contains $$$m$$$ integers $$$d_1, d_2, \ldots, d_m$$$ ($$$1\le d_i \le n$$$) — the movement range of each chip.
It is guaranteed that the sum of $$$n$$$ does not exceed $$$5000$$$ and the sum of $$$m$$$ does not exceed $$$5000$$$ across all test cases.

## Output
For each test case, output a single integer — the number of possible permutations of chips modulo $$$998\,244\,353$$$.