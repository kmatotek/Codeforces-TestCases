# Problem Description


You are given a permutationaandbof lengthn∗. You can perform the following operation at mostntimes:
Determine whetheraandbcan be reverses of each other after operations. In other words, for eachi=1,2,…,n,ai=bn+1−i.
If it is possible, output any valid sequence of operations. Otherwise, output−1.
∗A permutation of lengthnis an array consisting ofndistinct integers from1tonin arbitrary order. For example,[2,3,1,5,4]is a permutation, but[1,2,2]is not a permutation (2appears twice in the array), and[1,3,4]is also not a permutation (n=3but there is4in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(2≤n≤2⋅105) — the length of the permutations.
The second line containsnintegersa1,a2,…,an(1≤ai≤n).
The third line containsnintegersb1,b2,…,bn(1≤bi≤n).
It is guaranteed thataandbare permutations of lengthn.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, if it is impossible, output−1in the only line. Otherwise, output a single integerm(0≤m≤n) — the number of operations in the first line. In the followingmlines, output two integers — the indicesiandj(1≤i,j≤n,i≠j) in each operation in order. If there are multiple solutions, print any of them.