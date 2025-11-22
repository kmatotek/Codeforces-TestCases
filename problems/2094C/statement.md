# Problem Description

Brr Brrr Patapim is trying to learn of Tiramisù's secret passcode, which is a permutation∗of2⋅nelements. To help Patapim guess, Tiramisù gave him ann×ngridG, in whichGi,j(or the element in thei-th row andj-th column of the grid) containspi+j, or the(i+j)-th element in the permutation.
Given this grid, please help Patapim crack the forgotten code. It is guaranteed that the permutation exists, and it can be shown that the permutation can be determined uniquely.
∗A permutation ofmintegers is a sequence ofmintegers which contains each of1,2,…,mexactly once. For example,[1,3,2]and[2,1]are permutations, while[1,2,4]and[1,3,2,3]are not.

## Input
The first line contains an integert— the number of test cases (1≤t≤200).
The first line of each test case contains an integern(1≤n≤800).
Each of the followingnlines containsnintegers, giving the gridG. The first of these lines containsG1,1,G1,2,…,G1,n; the second of these lines containsG2,1,G2,2,…,G2,n, and so on. (1≤Gi,j≤2⋅n).
It is guaranteed that the grid encodes a valid permutation, and the sum ofnover all test cases does not exceed800.

## Output
For each test case, please output2nnumbers on a new line:p1,p2,…,p2n.