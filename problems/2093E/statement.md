# Problem Description

You are given an arrayaof lengthnand a numberk.
A subarray is defined as a sequence of one or more consecutive elements of the array. You need to split the arrayaintoknon-overlapping subarraysb1,b2,…,bksuch that the union of these subarrays equals the entire array. Additionally, you need to maximize the value ofx, which is equal to the minimum MEX(bi), fori∈[1..k].
MEX(v)denotes the smallest non-negative integer that is not present in the arrayv.

## Input
The first line contains an integert(1≤t≤104)— the number of test cases.
The first line of each test case contains two integersn,k(1≤k≤n≤2⋅105)— the length of the array and the number of segments to split the array into.
The second line of each test case containsnintegersai(0≤ai≤109)— the elements of the array.
It is guaranteed that the sum ofnacross all test cases does not exceed2⋅105.

## Output
For each query, output a single number  — the maximum valuexsuch that there exists a partition of the arrayaintoksubarrays where the minimum MEX equalsx.