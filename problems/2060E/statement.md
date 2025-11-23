# Problem Description

You are given two simple undirected graphsFandGwithnvertices.Fhasm1edges whileGhasm2edges. You may perform one of the following two types of operations any number of times:
Determine the minimum number of operations required such that for all integersuandv(1≤u,v≤n), there is a path fromutovinFif and only ifthere is a path fromutovinG.

## Input
The first line contains an integert(1≤t≤104) — the number of independent test cases.
The first line of each test case contains three integersn,m1, andm2(1≤n≤2⋅105,0≤m1,m2≤2⋅105) — the number of vertices, the number of edges inF, and the number of edges inG.
The followingm1lines each contain two integersuandv(1≤u,v≤n) — there is an edge betweenuandvinF. It is guaranteed that there are no repeated edges or self loops.
The followingm2lines each contain two integersuandv(1≤u,v≤n) — there is an edge betweenuandvinG. It is guaranteed that there are no repeated edges or self loops.
It is guaranteed that the sum ofn, the sum ofm1, and the sum ofm2over all test cases do not exceed2⋅105.

## Output
For each test case, output a single integer denoting the minimum operations required on a new line.