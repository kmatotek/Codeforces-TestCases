# Problem Description

Technically, this is an interactive problem.
An arrayaofmnumbers is calleddivisibleif at least one of the following conditions holds:
You are given a permutationpof integers1,2,…,n. Your task is to answer queries of the following form fast: if we take only the segment [l,r] from the permutation, that is, the numberspl,pl+1,…,pr, is this subarray of numbersdivisible?
Queries will be submitted in interactive mode in groups of10, meaning you will not receive the next group of queries until you output all answers for the current group.

## Input
The first line contains one integern(2≤n≤2⋅105) — the size of the permutation.
The second line containsnintegerspi(1≤pi≤n) — the permutation of natural numbers itself.
The third line contains one integerq(10≤q≤106,qmod10=0) — the number of queries.
The followingqlines contain two integerslandr(1≤l<r≤n) — the parameters of the query.

## Output
For each query, output the string "YES" if the subarray from this query isdivisibleand "NO" otherwise.
After printing the answers to a group of queries, do not forget to output the end of line and flush the output buffer. Otherwise, you may get theIdleness Limit Exceededverdict. To flush the buffer, use:
You have to flush the output buffer after the10-th,20-th,30-th query (and so on), i. e. after each query with index divisible by10. After that, you can read the next group of queries.