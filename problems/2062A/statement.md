# Problem Description

You are given a string $$$s$$$ of length $$$n$$$ consisting of $$$\mathtt{0}$$$ and/or $$$\mathtt{1}$$$. In one operation, you can select a non-empty subsequence $$$t$$$ from $$$s$$$ such that any two adjacent characters in $$$t$$$ are different. Then, you flip each character of $$$t$$$ ($$$\mathtt{0}$$$ becomes $$$\mathtt{1}$$$ and $$$\mathtt{1}$$$ becomes $$$\mathtt{0}$$$). For example, if $$$s=\mathtt{\underline{0}0\underline{101}}$$$ and $$$t=s_1s_3s_4s_5=\mathtt{0101}$$$, after the operation, $$$s$$$ becomes $$$\mathtt{\underline{1}0\underline{010}}$$$.
Calculate the minimum number of operations required to change all characters in $$$s$$$ to $$$\mathtt{0}$$$.
Recall that for a string $$$s = s_1s_2\ldots s_n$$$, any string $$$t=s_{i_1}s_{i_2}\ldots s_{i_k}$$$ ($$$k\ge 1$$$) where $$$1\leq i_1 < i_2 < \ldots <i_k\leq n$$$ is a subsequence of $$$s$$$.

## Input
The first line of input contains a single integer $$$t$$$ ($$$1 \leq t \leq 10^4$$$) — the number of input test cases.
The only line of each test case contains the string $$$s$$$ ($$$1\le |s|\le 50$$$), where $$$|s|$$$ represents the length of $$$s$$$.

## Output
For each test case, output the minimum number of operations required to change all characters in $$$s$$$ to $$$\mathtt{0}$$$.