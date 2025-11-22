# Problem Description

Let's call an integer sequencebeautifulif the following conditions hold:
For example,[1,2],[42],[1,4,2,4,7], and[1,2,4,8]are beautiful, but[2,2,4]and[1,3,5,3]are not.
Recall that a subsequence is a sequence that can be obtained from another sequence by removing some elements (possibly zero) without changing the order of the remaining elements.
You are given an integer arrayaof sizen. Find the longest beautiful subsequence of the arrayaand print its length.

## Input
The first line contains one integert(1≤t≤104) — the number of test cases. Next,tindependent cases follow.
The first line of each test case contains a single integern(1≤n≤5⋅105) — the length of arraya.
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤106) – the arraya.
Additional constraint on the input: the total sum ofnover all test cases doesn't exceed5⋅105.

## Output
For each test case, print one integer — the length of the longest beautiful subsequence of arraya.