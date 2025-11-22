# Problem Description

Muhammadali has an integer array $$$a_1,\dots,a_n$$$. He can change (replace) any subset of positions; changing position $$$i$$$ costs $$$c_i$$$ and replaces $$$a_i$$$ with any integer of his choice. The positions that he does not change must retain their original values.
After all changes, we call an index $$$i$$$ ($$$1 \le i < n$$$) adropif the final value at position $$$i$$$ is strictly greater than the final value at position $$$i+1$$$. Muhammadali wants the final array to contain nodrops.
Find the minimum cost of changes required to ensure that there are nodropsin the array.

## Input
The first line contains an integer $$$t$$$ ($$$1 \le t \le 5000$$$) — the number of test cases.
Each test case consists of three lines:
The first line contains a single integer $$$n$$$ ($$$1 \le n \le 8000$$$) — the length of the arrays.
The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^9$$$) — the elements of the array.
The third line contains $$$n$$$ integers $$$c_1, c_2, \dots, c_n$$$ ($$$1 \le c_i \le 10^9$$$) — the costs of changes.
It is guaranteed that the sum of $$$n$$$ across all test cases does not exceed $$$8000$$$.

## Output
For each test case, output a single integer — the minimum possible total cost required to eliminate alldrops.