# Problem Description

You are given an arrayaof lengthnand an integerk.
Call a non-empty arraybof lengthmepicif there exists an integeriwhere1≤i<mandmin(b1,…,bi)+max(bi+1,…,bm)=k.
Count the number ofepicsubarrays∗ofa.
∗An arrayais a subarray of an arraybifacan be obtained frombby the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

## Input
The first line contains an integert(1≤t≤104) — the number of testcases.
The first line of each testcase contains integersnandk(2≤n≤2⋅105;n<k<2⋅n) — the length of the arrayaandk.
The second line of each testcase containsnintegersa1,a2,…,an(1≤ai≤n).
The sum ofnacross all testcases does not exceed2⋅105.

## Output
For each testcase, output the number of epic contiguous subarrays ofa.