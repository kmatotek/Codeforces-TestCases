# Problem Description

For the final of the first Olympiad by IT Campus "NEIMARK", a rectangular venue was prepared. You may assume that the venue is divided intonrows, each containingmspots for participants' desks. A total ofkparticipants have registered for the final, and each participant will sit at an individual desk. Now, the organizing committee must choose the locations for the desks in the venue.
Each desk occupies one of themspots in a row. Moreover, if several desks occupy consecutive spots in the same row, we call such a group of desks abench, and the number of desks in the group is the bench's length. For example, seating7participants on a3×4venue (withn=3,m=4) can be arranged as follows:
In the figure above, the first row has one bench of length3, the second row has one bench of length2, and the third row has two benches of length1.
The organizing committee wants to choose the locations so that the length of the longest bench is as small as possible. In particular, the same7desks can be arranged in a more optimal way, so that the lengths of all benches do not exceed2:
Given the integersn,m, andk, determine the minimum possible length of the longest bench.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
A single line of each test case contains three positive integers —n,m,k(1≤n,m,k≤109,k≤n⋅m).

## Output
For each test case, output a single number — the minimum possible length of the longest bench.