# Problem Description

Mouf is bored with themes, so he decided not to use any themes for this problem.
You are given a binary∗stringsof lengthn. You are to perform the following operation exactlyktimes:
You need to count the number of possible ways to perform allkoperations.
Since the answer could be ginormous, print it modulo998244353.
Two sequences of operations are considered different if they differ in the index selected at any step.
∗A binary string is a string that consists only of the characters0and1.
†Flipping a binary character is changing it from0to1or vice versa.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤100). The description of the test cases follows.
The first line of each test case contains two integersnandk(1≤k≤n≤500) — the length of the binary stringsand the number of times the operation must be performed, respectively.
The second line of each test case contains a binary stringsof lengthnconsisting of only characters0and1.
It is guaranteed that the sum ofndoes not exceed500over all test cases.

## Output
For each test case, output a single integer — the number of ways you can perform exactlykoperations, modulo998244353.