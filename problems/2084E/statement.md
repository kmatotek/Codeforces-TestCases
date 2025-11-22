# Problem Description


You are given a permutationaof lengthn∗where some elements are missing and represented by−1.
Define the value of a permutation as the sum of the MEX†of all its non-empty subsegments‡.
Find the sum of the value of all possible valid permutations that can be formed by filling in the missing elements ofamodulo109+7.
∗A permutation of lengthnis an array consisting ofndistinct integersfrom0ton−1in arbitrary order. For example,[1,2,0,4,3]is a permutation, but[0,1,1]is not a permutation (1appears twice in the array), and[0,2,3]is also not a permutation (n=3but there is3in the array).
†The minimum excluded (MEX) of a collection of integersc1,c2,…,ckis defined as the smallest non-negative integerxwhich does not occur in the collectionc.
‡A sequenceais a subsegment of a sequencebifacan be obtained frombby the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤1000). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤5000).
The second line containsnintegersa1,a2,…,an(−1≤ai<n).
It is guaranteed that the elements ofathat are not−1are distinct.
It is guaranteed that the sum ofnover all test cases does not exceed5000.

## Output
For each test case, output a single integer — the sum of the value of all possible valid permutations modulo109+7.