# Problem Description

Petya and Vasya love participating in Codeforces contests. Vasya made a bet with Petya that he will take part in more rated rounds than him. Initially, Vasya's rating is $$$R_0$$$. There will be $$$n$$$ rounds conducted in total, each of one of two types:
In an unrated round, Vasya cannot change his rating. If Vasya's rating before a rated round was $$$R$$$, then for anynon-negativeinteger $$$x$$$ between $$$R-D$$$ and $$$R+D$$$ (inclusive) Vasya can adopt a strategy such that his rating becomes exactly $$$x$$$ afterwards (here $$$D$$$ is a positive integer). Note that rating may never become negative.
Help Vasya determine the maximum number of rated rounds he can participate in.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 1000$$$). The description of the test cases follows.
The first line of each test case contains four integers: $$$R_0, X, D, n$$$ ($$$0 \leq R_0 \leq 10^9$$$, $$$1 \leq X \leq 10^9$$$, $$$1 \leq D, n \leq 1000$$$) — Vasya's initial rating, the rating threshold between divisions, the maximum rating delta, and the number of rounds.
The second line of each test case contains a string of size $$$n$$$. The string will only contain the characters "1" and "2", representing div. 1 and div. 2 rounds respectively.
The sum of $$$n$$$ across all test cases does not exceed $$$3 \cdot 10^4$$$.

## Output
For each test case, print a single integer — the maximum number of rated rounds Vasya can participate in.