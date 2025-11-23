# Problem Description

Skibidus thinks he's Him! He proved it by solving this difficult task. Can you also prove yourself?
Given a binary string∗t,f(t)is defined as the minimum number of contiguous substrings, each consisting of identical characters, into whichtcan be partitioned. For example,f(00110001)=4becausetcan be partitioned as[00][11][000][1]where each bracketed segment consists of identical characters.
Skibidus gives you a binary stringsandqqueries. In each query, a single character of the string is flipped (i.e.0changes to1and1changes to0); changes are saved after the query is processed. After each query, output the sum over allf(b)wherebis a non-empty subsequence†ofs, modulo998244353.
∗A binary string consists of only characters0and1.
†A subsequence of a string is a string which can be obtained by removing several (possibly zero) characters from the original string.

## Input
The first line contains an integert(1≤t≤104) — the number of test cases.
The first line of each test case contains a binary strings(1≤|s|≤2⋅105).
The following line of each test case contains an integerq(1≤q≤2⋅105) — the number of queries.
The following line containsqintegersv1,v2,…,vq(1≤vi≤|s|), denotingsviis flipped for thei'th query.
It is guaranteed that the sum of|s|and the sum ofqover all test cases does not exceed2⋅105.

## Output
For each test case, outputqintegers on a single line — the answer after each query modulo998244353.