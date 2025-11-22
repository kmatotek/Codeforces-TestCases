# Problem Description

Given an array $$$a$$$ and $$$n$$$ integers. It is sorted in non-decreasing order, that is, $$$a_i \le a_{i + 1}$$$ for all $$$1 \le i < n$$$.
You can remove any number of elements from the array (including the option of not removing any at all) without changing the order of the remaining elements. After the removals, the following will occur:
For example, if $$$a=[1, 2, 4, 6]$$$, then:
Your task is to remove elements in such a way that the described algorithm creates as many arrays as possible. If you remove all elements from the array, no new arrays will be created.

## Input
The first line of input contains one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first line of each test case contains one integer $$$n$$$ ($$$1 \le n \le 2 \cdot 10^5$$$) — the length of the array.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^6$$$, $$$a_i \le a_{i + 1}$$$) — the elements of the array.
It is guaranteed that the sum of $$$n$$$ across all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output one integer — the maximum number of arrays that can be obtained by removing any (possibly zero) number of elements.