# Problem Description

You are given an integerm(2≤m≤5⋅105) and an arrayaconsisting of nonnegative integers smaller thanm.
Answer queries of the following form:
Note that instances of query2are independent; that is, no actual operations are taking place. Instances of query1are persistent.
∗a(modm)is defined as the unique integerbsuch that0≤b<manda−bis an integer multiple ofm.
†An arrayaof sizenis called nondecreasing if and only ifai≤ai+1for all1≤i<n.

## Input
The first line contains an integert(1≤t≤104)  — the number of test cases.
The first line of each test case contains three integers,n,m, andq(2≤n≤105,2≤m≤5⋅105,1≤q≤105) — the size of the arraya, the integerm, and the number of queries.
The second line of each test case containsnintegers,a1,a2,…,an(0≤ai<m).
Then followsqlines. Each line is of one of the following forms:
It is guaranteed that the sum ofnand the sum ofqover all test cases each do not exceed105.

## Output
For each instance of query2, output on a single line "YES" if there exists some sequence of (possibly zero) operations to makeanondecreasing, and "NO" otherwise.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.