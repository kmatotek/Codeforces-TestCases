# Problem Description

Let's call an integer sequencebeautifulif the following conditions hold:
For example, $$$[1, 4, 2, 4, 7]$$$ and $$$[1, 2, 4, 8]$$$ are beautiful, but $$$[1, 2]$$$, $$$[2, 2, 4]$$$, and $$$[1, 3, 5, 3]$$$ are not.
Recall that a subsequence is a sequence that can be obtained from another sequence by removing some elements without changing the order of the remaining elements.
You are given an integer array $$$a$$$ of size $$$n$$$, whereevery element is from $$$1$$$ to $$$3$$$. Your task is to calculate the number of beautiful subsequences of the array $$$a$$$. Since the answer might be large, print it modulo $$$998244353$$$.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first line of each test case contains a single integer $$$n$$$ ($$$3 \le n \le 2 \cdot 10^5$$$).
The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 3$$$).
Additional constraint on the input: the sum of $$$n$$$ over all test cases doesn't exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, print a single integer — the number of beautiful subsequences of the array $$$a$$$, taken modulo $$$998244353$$$.