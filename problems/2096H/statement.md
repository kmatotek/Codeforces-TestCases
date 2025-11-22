# Problem Description

You are the proud... never mind, just solve this problem.
There arenintervals[l1,r1],[l2,r2],…[ln,rn]. For eachxfrom0to2m−1, find the number, modulo998244353, of sequencesa1,a2,…ansuch that:

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line contains two integersnandm(1≤n≤2⋅105,1≤m≤18).
Thei-th of the nextnlines contains two integersliandri(0≤li≤ri<2m).
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105, and the sum of2mover all test cases does not exceed218.

## Output
For eachxfrom0to2m−1, let:
Here,fxandgxare both integers in the interval[0,998244352].
Leth=g0⊕g1⊕…⊕g2m−1.
Output a single integer — the value ofhitself.Do notperform a modulo operation.