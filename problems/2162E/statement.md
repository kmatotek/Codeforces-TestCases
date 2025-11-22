# Problem Description

We call an array $$$[b_1, b_2, \dots, b_m]$$$ of length $$$m$$$palindromicif the following condition holds:
In other words, an array is palindromic if it reads the same forward and backward.
You are given an array $$$[a_1, a_2, \dots , a_n]$$$ of $$$n$$$ integers where $$$1 \le a_i \le n$$$ and an integer $$$k$$$.
You are required to perform the following operationexactly$$$k$$$ times:
Your goal is to perform these $$$k$$$ operations in such a way that the number of palindromic subarrays$$$^{\text{∗}}$$$ in the resulting array is minimized.
Output the $$$k$$$ integers you chose for each operation, in the order they were appended.
$$$^{\text{∗}}$$$An array $$$b$$$ is a subarray of an array $$$a$$$ if $$$b$$$ can be obtained from $$$a$$$ by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end. In particular, an array is a subarray of itself.

## Input
The first line of input contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$3 \le n \le 2\cdot10^5, 1 \le k \le n$$$) — the length of the array $$$a$$$.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots , a_n$$$ ($$$1 \le a_i \le n$$$) — the elements of the array $$$a$$$.
It is guaranteed that the sum of $$$n$$$ over all the test cases does not exceed $$$2\cdot10^5$$$.

## Output
For each test case, print the $$$k$$$ integers chosen for the append operations, in the order they were appended, such that the total number of palindromic subarrays in the resulting array is minimized.
If there are multiple answers, you may output any one of them.