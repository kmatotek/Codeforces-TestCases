# Problem Description

With the approach of Valentine's Day, Skibidus desperately needs a way to rizz up his crush! Fortunately, he knows of just the way: creating the perfect Binary String!
Given a binary string∗t, letxrepresent the number of0intandyrepresent the number of1int. Itsbalance-valueis defined as the value ofmax(x−y,y−x).
Skibidus gives you three integersn,m, andk. He asks for your help to construct a binary stringsof lengthn+mwith exactlyn0's andm1's such that the maximumbalance-valueamong all of its substrings†isexactlyk. If it is not possible, output-1.
∗A binary string only consists of characters0and1.
†A stringais a substring of a stringbifacan be obtained frombby the deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

## Input
The first line contains an integert(1≤t≤104) — the number of test cases.
The first and only line of each test case contains three integersn,m, andk(0≤n,m≤2⋅105,1≤k≤n+m,n+m≥1).
It is guaranteed that the sum ofnand the sum ofmover all test cases does not exceed2⋅105.

## Output
For each test case, if it is possible to constructs, output it on a new line. If there are multiple possibles, output any. Otherwise, output-1on a new line.