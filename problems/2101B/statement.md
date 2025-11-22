# Problem Description


You are given a permutationaof lengthn∗. You are allowed to do the following operation any number of times (possibly zero):
Determine the lexicographically smallest permutation†that can be obtained by applying the above operation any number of times.
∗A permutation of lengthnis an array consisting ofndistinct integers from1tonin arbitrary order. For example,[2,3,1,5,4]is a permutation, but[1,2,2]is not a permutation (2appears twice in the array), and[1,3,4]is also not a permutation (n=3but there is4in the array).
†An arrayxis lexicographically smaller than an arrayyof the same size if and only if the following holds:

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤1000). The description of the test cases follows.
The first line of each test case contains a single integern(4≤n≤2⋅105) — the length of permutationa.
The second line containsnintegersa1,a2,…,an(1≤ai≤n) — the elements of permutationa.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output the lexicographically smallest permutation that can be obtained by applying the above operation any number of times.