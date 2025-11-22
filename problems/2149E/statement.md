# Problem Description

In the world ofDeepwoken, there exists an ancient artifact —Tablet of Infinite Knowledge, on which a sequence of $$$n$$$ mysterious symbols (each symbol is an integer) is engraved.
It is said that the true power of the artifact can only be revealed by finding allsacred fragments— continuous segments of the tablet that contain exactly $$$k$$$ distinct numbers, and their length must be between $$$l$$$ and $$$r$$$ (inclusive).
Formally: Given a sequence $$$a$$$ of length $$$n$$$ and integers $$$k$$$, $$$l$$$, $$$r$$$. You need to find the number of such boundaries $$$b$$$ and $$$c$$$ such that:

## Input
Each test consists of several test cases.
The first line contains one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The following describes the test cases.
The first line of each test case contains four integers: $$$n$$$, $$$k$$$, $$$l$$$, and $$$r$$$ $$$( 1 \le k \le n \le 2 \cdot 10^5, 1 \le l \le r \le n)$$$.
The second line contains $$$n$$$ numbers $$$a_i$$$ $$$(1 \le a_i \le 10^9)$$$ — the mysterious symbols.
It is guaranteed that the total value of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test, output a single integer on a separate line — the number of continuous subarrays that meet the specified conditions.