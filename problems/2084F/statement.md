# Problem Description


You are given a permutationaof lengthn∗.
We say that a permutationbof lengthnisgoodif the two permutationsaandbcan become the same after performing the following operationat mostntimes(possibly zero):
You are also given a permutationcof lengthnwhere some elements are missing and represented by0.
You need to find agoodpermutationb1,b2,…,bnsuch thatbcan be formed by filling in the missing elements ofc(i.e., for all1≤i≤n, ifci≠0, thenbi=ci). If it is impossible, output−1.
∗A permutation of lengthnis an array consisting ofndistinct integers from1tonin arbitrary order. For example,[2,3,1,5,4]is a permutation, but[1,2,2]is not a permutation (2appears twice in the array), and[1,3,4]is also not a permutation (n=3but there is4in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(2≤n≤5⋅105).
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤n). It is guaranteed thatais a permutation of lengthn.
The third line of each test case containsnintegersc1,c2,…,cn(0≤ci≤n). It is guaranteed that the elements ofcthat are not0are distinct.
It is guaranteed that the sum ofnover all test cases does not exceed5⋅105.

## Output
For each test case: