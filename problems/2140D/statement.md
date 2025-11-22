# Problem Description

You are givennsegments on a number line. Thei-th segment is represented as[li,ri]. Initially, all the segments areunmarked.
You perform the following operation repeatedly until there are no unmarked segments left:
Your task is to determine the maximum possible sum of lengths of all the marked segments at the end of the process. Note that the length of a segment([l,r])isr−l.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤2⋅105) — the number of segments.
Each of the nextnlines contains two integersliandri(1≤li≤ri≤109) — thei-th segment.
It is guaranteed that the sum ofnacross all test cases does not exceed2⋅105.

## Output
For each test case, print a single integer — the maximum possible total length of all marked segments at the end of the process.