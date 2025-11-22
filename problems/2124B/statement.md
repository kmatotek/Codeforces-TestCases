# Problem Description

This problem differs from problem G. In this problem, you must output theminimumsum of prefix minimums after at most one operation.
You are given an arrayaof lengthn, with elements satisfying0≤ai≤n. You can perform the following operationat most once:
Output theminimumpossible value ofmin(a1)+min(a1,a2)+…+min(a1,a2,…,an)that you can get.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains an integern(2≤n≤2⋅105) — the length ofa.
The following line containsnspace-separated integersa1,a2,…,an(0≤ai≤n) — denoting the arraya.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output an integer on a new line, the minimum possible value ofmin(a1)+min(a1,a2)+…+min(a1,a2,…,an).