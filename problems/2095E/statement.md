# Problem Description

You are given aprimenumberp,nintegersa1,a2,…,an, and an integerk.
Find the number of pairs of indexes(i,j)(1≤i<j≤n) for which(ai⊕aj)(a2i⊕a2j)≡kmodp.
Here⊕denotes thebitwise XOR operation.

## Input
The first line contains integersn,p,k(2≤n≤3⋅105,2≤p≤109,0≤k≤p−1).pis guaranteed to be prime.
The second line containsnintegersa1,a2,…,an(0≤ai≤p−1). It is guaranteed that all elements are different.

## Output
Output a single integer — answer to the problem.