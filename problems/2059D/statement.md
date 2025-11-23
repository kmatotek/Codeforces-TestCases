# Problem Description

You are given two connected undirected graphs with the same number of vertices. In both graphs, there is a token located at some vertex. In the first graph, the token is initially at vertexs1, and in the second graph, the token is initially at vertexs2. The following operation is repeated aninfinitenumber of times:
Determine the minimum possible total cost of all operations or report that this value will be infinitely large.

## Input
Each test consists of multiple test cases. The first line contains one integert(1≤t≤500) — the number of test cases. The description of the test cases follows.
The first line of each test case contains three integersn,s1, ands2(2≤n≤1000,1≤s1,s2≤n) — the number of vertices in each graph, the number of the vertex in the first graph where the token is initially located, and the number of the vertex in the second graph where the token is initially located.
The second line of each test case contains one integerm1(1≤m1≤1000) — the number of edges in the first graph.
Thei-th of the followingm1lines contains two integersaiandbi(1≤ai,bi≤n,ai≠bi) — the numbers of the endpoints of thei-th edge in the first graph.
The next line of each test case contains one integerm2(1≤m2≤1000) — the number of edges in the second graph.
Thej-th of the followingm2lines contains two integerscjanddj(1≤cj,dj≤n,cj≠dj) — the numbers of the endpoints of thej-th edge in the second graph.
It is guaranteed that the sum ofn, the sum ofm1, and the sum ofm2over all test cases do not exceed1000.
It is guaranteed that both graphs are connected.

## Output
For each test case, output one integer — the minimum total cost of all operations or−1, if this value will be infinitely large.