# Problem Description


There arenhaystacks labelled from1ton, where haystackicontainsaihaybales. One of the haystacks has a needle hidden beneath it, but you do not know which one. Your task is to move the haybales so that each haystack is emptied at least once, allowing you to check if the needle is hidden under that particular haystack.
However, the process is not that simple. Once a haystackiis emptied for the first time, it will be assigned a height limit and can no longer contain more thanbihaybales. More formally, a move is described as follows:
Note: Before a haystack is emptied, it has no height limit, and you can move as many haybales as you want onto that haystack.
Compute the minimum number of moves required to ensure that each haystack is emptied at least once, or report that it is impossible.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(2≤n≤5⋅105) — the number of haystacks.
Thei-th of the nextnlines contains two integersaiandbi(1≤ai,bi≤109) — the initial number of haybales in thei-th haystack, and the height limit that it is assigned after it is emptied for the first time.
It is guaranteed that the sum ofnover all test cases does not exceed5⋅105.

## Output
For each test case, print a single integer — the minimum number of moves required to ensure that each haystack is emptied at least once. If it is not possible to empty each haystack at least once, output-1.