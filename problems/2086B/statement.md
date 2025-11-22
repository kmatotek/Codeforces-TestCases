# Problem Description

There is an arrayaconsisting ofnpositiveintegers, and a positive integerk. An arraybis created from arrayaaccording to the following rules:
For example, ifa=[2,3,1,4]andk=3, thenb=[2,3,1,4,2,3,1,4,2,3,1,4].
Given a numberx, it is required to count the number of such positionsl(1≤l≤n⋅k), for which there exists a positionr≥l, such that the sum of the elements of arraybon the segment[l,r]isat leastx(in other words,bl+bl+1+⋯+br≥x).

## Input
Each test consists of several test cases. The first line contains one integert(1≤t≤104) — the number of test cases. The description of the test cases follows.
The first line of each test case contains three integersn,k,x(1≤n,k≤105;1≤x≤1018).
The second line of each test case containsnintegersai(1≤ai≤108).
Additional constraints on the input:

## Output
For each test case, output one integer — the number of suitable positionslin the arrayb.