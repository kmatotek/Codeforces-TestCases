# Problem Description

You are given a string $$$s$$$ consisting of charactersAandB.
Your task is to split it into blocks of length $$$1$$$ and $$$2$$$ in such a way that
Strings "AA" and "BB" are prohibited. Each character of the initial string $$$s$$$ should belong to exactly one block.

## Input
The first line contains one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases. Next, $$$t$$$ independent cases follow.
The first line of each test case contains a single string $$$s$$$ ($$$1 \le |s| \le 5 \cdot 10^5$$$) consisting only of charactersAand/orB.
The second line of each test case contains four integers $$$a$$$, $$$b$$$, $$$ab$$$, and $$$ba$$$ ($$$0 \le a, b, ab, ba \le 5 \cdot 10^5$$$) — the maximum allowed number of strings "A", "B", "AB", and "BA" correspondingly.
It's guaranteed that the total length of $$$s$$$ doesn't exceed $$$5 \cdot 10^5$$$ over all test cases.

## Output
For each test case, printYESif it's possible to split string $$$s$$$. Otherwise, printNO.