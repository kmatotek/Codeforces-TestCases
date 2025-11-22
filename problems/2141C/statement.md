# Problem Description

There is a variable $$$sum$$$, which is initially equal to $$$0$$$.
There is also a data structure that can perform the following operations:
The operationspopback,popfront, andmincannot be applied to an empty structure!
Using this structure, you would like to be able to find the sum of the minimums of all non-empty subarrays of an array $$$a$$$ of $$$n$$$ elements.
More formally, your task is to find a sequence of no more than $$$n \cdot (n + 2)$$$ commands such that after all operations, the variable $$$sum$$$ will be equal to $$$\sum_{0 \le l \le r < n} \min(a[l],\dots, a[r])$$$ for any possible array $$$a$$$.

## Input
The first line contains a single integer $$$n$$$ ($$$1 \le n \le 500$$$) — the number of elements in the array.

## Output
Output $$$k$$$ ($$$1 \le k \le n \cdot (n + 2)$$$) commands. Each command must be one of the following five lines:
If there are multiple valid answers, output any.