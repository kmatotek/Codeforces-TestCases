# Problem Description


We call a sequencea1,a2,…,anmagicalif for all1≤i≤n−1it holds that:min(a1,…,ai)≥mex(ai+1,…,an). In particular, any sequence of length1is consideredmagical.
The minimum excluded (MEX) of a collection of integersa1,a2,…,akis defined as the smallest non-negative integertwhich does not occur in the collectiona.
You are given a sequenceaofnnon-negative integers. Find the maximum possible length of amagicalsubsequence∗of the sequencea.
∗A sequenceais a subsequence of a sequencebifacan be obtained frombby the deletion of several (possibly, zero or all) element from arbitrary positions.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains an integern(1≤n≤2⋅105) — the length of the sequencea.
The second line of each test case containsnintegersa1,a2,…,an(0≤ai≤109) — the elements of the sequencea.
It is guaranteed that the sum ofnacross all test cases does not exceed2⋅105.

## Output
For each test case, output a single number — the maximum possible length of amagicalsubsequence of the sequencea.