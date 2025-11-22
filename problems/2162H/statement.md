# Problem Description

For an arrayaof lengthnand three integersx,l, andr（1≤l≤r≤n), define:
f(a,x,l,r)={0,if(x−minrj=l(aj))⋅(x−maxrj=l(aj)))<01,if(x−minrj=l(aj))⋅(x−maxrj=l(aj)))≥0
You are given an arrayaof lengthn(1≤ai≤n), andmintervals[li,ri](1≤li≤ri≤n).
For eachx=1,2,…,n, answer the following questionindependently:

## Input
The first line contains a single integert(1≤t≤2⋅104) — the number of test cases. Description of each testcase follows.
The first line contains two integersnandm(2≤n≤2000,1≤m≤2000).
The next line containsnspace-separated integersa1,a2,⋯,an(1≤ai≤n).
The nextmlines each contain two space-separated integersli,ri(1≤li≤ri≤n), each denoting an interval.
It is guaranteed that the sum ofn2and the sum ofm2over all test cases does not exceed4⋅106, respectively.

## Output
For each test case, output a binary strings. Forx=1,2,…,n,sx=1only if there exists a rearrangementa′ofa, such that forall1≤i≤m,f(a′,x,li,ri)=1. Otherwise,sx=0.