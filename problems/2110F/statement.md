# Problem Description

In 2077, after the world was enslaved by robots, the robots decided to implement an educational reform, and now the operation of taking the modulus is only taught in the faculty of "Ancient World History". Here is one of the entrance tasks for this faculty:
We define thebeautyof an array of positive integersbas the maximumf(bi,bj)over all pairs1≤i,j≤n, wheref(x,y)=(xmody)+(ymodx).
Given an array of positive integersaof lengthn, outputnnumbers, where thei-th number (1≤i≤n) is thebeautyof the arraya1,a2,…,ai.
xmodyis the remainder of the division ofxbyy.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤106) — the size of the arraya.
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤109).
It is guaranteed that the sum ofnacross all test cases does not exceed106.

## Output
For each test case, outputnintegers — the beauties of all prefixes of the arraya.