# Problem Description

You are a cat selling fun algorithm problems. Today, you want to recommend your fun algorithm problems tokcities.
There are a total ofncities, each with two parametersaiandbi. Between any two citiesi,j(i≠j), there is a bidirectional road with a length ofmax(ai+bj,bi+aj). The cost of a path is defined as the total length of roads between every two adjacent cities along the path.
Fork=2,3,…,n, find the minimum cost among all simple paths containing exactlykdistinctcities.

## Input
The first line of input contains a single integert(1≤t≤1500) — the number of test cases.
For each test case, the first line contains a single integern(2≤n≤3⋅103) — the number of cities.
Thennlines follow, thei-th line contains two integersai,bi(0≤ai,bi≤109) — the parameters of cityi.
It is guaranteed that the sum ofn2over all test cases does not exceed9⋅106.

## Output
For each test case, printn−1integers in one line. Thei-th integer represents the minimum cost whenk=i+1.