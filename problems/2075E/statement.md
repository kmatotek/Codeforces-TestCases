# Problem Description

For two arraysa=[a1,a2,…,an]andb=[b1,b2,…,bm], we define the XOR matrixXof sizen×m, where for each pair(i,j)(1≤i≤n;1≤j≤m) it holds thatXi,j=ai⊕bj. The symbol⊕denotes the bitwise XOR operation.
You are given four integersn,m,A,B. Count the number of such pairs of arrays(a,b)such that:

## Input
The first line contains one integert(1≤t≤104) — the number of test cases.
Each test case consists of one line containing four integersn,m,A,B(2≤n,m,A,B≤229−1).

## Output
For each test case, output one integer — the number of pairs of arrays(a,b)that satisfy all three conditions. Since this number can be very large, output it modulo998244353.