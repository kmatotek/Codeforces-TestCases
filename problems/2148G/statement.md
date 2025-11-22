# Problem Description

Bessie has found an arrayaof lengthnon the floor. There appears to be a handwritten note lying next to the array, seemingly written by Farmer John. The note reads:
Help me, dear Bessie! Letf(a)denote the maximum integerkin the range[1,n)such thatgcd(a1,a2,…,ak)>gcd(a1,a2,…,ak+1), or0if no suchkexists.
Bessie decides to help FJ. She definesg(a)to represent the maximum value off(a)over all possible reorderings ofa.
Bessie decides to not only findg(a), but also the value ofg(p)for all prefixespofa. Outputnintegers, thei'th of which isg([a1,a2,…,ai]).

## Input
The first line contains an integert(1≤t≤104)  — the number of test cases.
The first line of each test case contains an integern(1≤n≤2⋅105).
The following line containsnspace-separated integersa1,a2,…,an(1≤ai≤n).
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, outputnintegers on a new line: thei'th of which should beg([a1,a2,…,ai]).