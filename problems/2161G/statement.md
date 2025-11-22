# Problem Description

There is an array of integers $$$a_1, a_2, \ldots, a_n$$$, and there is an integer $$$X$$$.
You may perform the following operation zero or more times:
Let $$$a'$$$ be the final state of the array. Your goal is to perform the operation above the smallest number of times such that $$$a'_1 \,\&\, a'_2 \,\&\, \ldots \,\&\, a'_n = X$$$. $$$\&$$$ denotes thebitwise AND operation.
There are $$$q$$$ such query integers $$$X$$$: $$$X_1, X_2, \ldots, X_q$$$. Compute the answer for each $$$X = X_i$$$. Note that all queries are processed separately and independently, from the same initial state $$$a$$$.

## Input
The first line contains integers $$$n$$$ and $$$q$$$ ($$$2 \le n \le 200\,000$$$, $$$1 \le q \le 200\,000$$$) — the length of the array and the number of queries.
The second line contains integers $$$a_1, a_2, \ldots, a_n$$$ (for each $$$i$$$, $$$0 \le a_i < 2^{20}$$$).
The next $$$q$$$ lines each contain a single integer $$$X_i$$$ ($$$0 \le X_i < 2^{20}$$$).

## Output
For each query $$$i$$$ out of $$$q$$$, print the smallest number of operations to get to the array $$$a'$$$ such that $$$a'_1 \,\&\, a'_2 \,\&\, \ldots \,\&\, a'_n = X_i$$$.
It's possible to show, that it's always possible to obtain such array $$$a'$$$ in finite number of operations.