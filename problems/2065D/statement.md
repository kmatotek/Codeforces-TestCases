# Problem Description

Let's denote the score of an arraybwithkelements as∑ki=1(∑ij=1bj). In other words, letSidenote the sum of the firstielements ofb. Then, the score can be denoted asS1+S2+…+Sk.
Skibidus is givennarraysa1,a2,…,an, each of which containsmelements. Being the sigma that he is, he would like to concatenate them inany orderto form a single array containingn⋅melements. Please find the maximum possible score Skibidus can achieve with his concatenated array!
Formally, among all possible permutations∗pof lengthn, output the maximum score ofap1+ap2+⋯+apn, where+represents concatenation†.
∗A permutation of lengthncontains all integers from1tonexactly once.
†The concatenation of two arrayscanddwith lengthseandfrespectively (i.e.c+d) isc1,c2,…,ce,d1,d2,…df.

## Input
The first line contains an integert(1≤t≤104) — the number of test cases.
The first line of each test case contains two integersnandm(1≤n⋅m≤2⋅105) — the number of arrays and the length of each array.
Thei'th of the nextnlines containsmintegersai,1,ai,2,…,ai,m(1≤ai,j≤106) — the elements of thei'th array.
It is guaranteed that the sum ofn⋅mover all test cases does not exceed2⋅105.

## Output
For each test case, output the maximum score among all possible permutationspon a new line.