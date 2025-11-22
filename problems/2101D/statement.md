# Problem Description


An arraybof length|b|iscuteif the sum of the length of its Longest Increasing Subsequence (LIS) and the length of its Longest Decreasing Subsequence (LDS)∗isexactlyone more than the length of the array. More formally, the arraybis cute ifLIS(b)+LDS(b)=|b|+1.
You are given a permutationaof lengthn†. Your task is to count the number of non-empty subarrays‡of permutationathat are cute.
∗A sequencexis a subsequence of a sequenceyifxcan be obtained fromyby the deletion of several (possibly, zero or all) element from arbitrary positions.
The longest increasing (decreasing) subsequence of an array is the longest subsequence such that its elements are ordered in strictly increasing (decreasing) order.
†A permutation of lengthnis an array consisting ofndistinct integers from1tonin arbitrary order. For example,[2,3,1,5,4]is a permutation, but[1,2,2]is not a permutation (2appears twice in the array), and[1,3,4]is also not a permutation (n=3but there is4in the array).
‡An arrayxis a subarray of an arrayyifxcan be obtained fromyby the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤2⋅105) — the length of permutationa.
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤n) — the elements of permutationa.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output the number of cute non-empty subarrays of permutationa.