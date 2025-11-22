# Problem Description


You are given an integerkandnpositive integersa1,a2,…,anwritten on a whiteboard, where1≤ai≤n. You may perform the following operations:
Thebeautyof a collection of integersbis defined as the greatest common divisor of all the elements inb. Formally, it is the largest integerdsuch thatddividesxfor everyxthat is an element ofb.
Your task is to determine the maximum possible beauty of the integers on the whiteboard after performing at mostkEraseoperations and any number ofSplitoperations.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains two integersnandk(1≤n≤2⋅105,0≤k≤n−1) — the number of integers on the whiteboard, and the maximum number ofEraseoperations allowed.
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤n) — the integers initially written on the whiteboard.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output a single integer representing the maximum beauty of the elements written on the whiteboard after performing the operations.