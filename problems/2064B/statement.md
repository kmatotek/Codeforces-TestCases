# Problem Description

Define the score of an arbitrary arraybto be the length ofbminus the number of distinct elements inb. For example:
You have an arraya. You need to remove somenon-emptycontiguous subarray fromaat mostonce.
More formally, you can do the followingat mostonce:
Output an operation such that the score ofaismaximum; if there are multiple answers, output one thatminimisesthe final length ofaafter the operation. If there are still multiple answers, you may output any of them.

## Input
The first line contains an integert(1≤t≤104) — the number of testcases.
The first line of each testcase contains an integern(1≤n≤2⋅105) — the length of the arraya.
The second line of each testcase containsnintegersa1,a2,…,an(1≤ai≤n).
The sum ofnacross all testcases does not exceed2⋅105.

## Output
For each testcase, if you wish to not make a move, output0.
Otherwise, output two integerslandr(1≤l≤r≤n), representing the left and right bound of the removed subarray.
The removed subarray should be chosen such that the score is maximized, and over all such answers choose any of them that minimises the final length of the array.