# Problem Description


You are given an array of integersa1,a2,…,an. An arrayx1,x2,…,xmisbeautifulif there exists an arrayy1,y2,…,ymsuch that the elements ofyare distinct (in other words,yi≠yjfor all1≤i<j≤m), and the product ofxiandyiis the same for all1≤i≤m(in other words,xi⋅yi=xj⋅yjfor all1≤i<j≤m).
Your task is to determine the maximum size of a subsequence∗of arrayathat is beautiful.
∗A sequencebis a subsequence of a sequenceaifbcan be obtained fromaby the deletion of several (possibly, zero or all) element from arbitrary positions.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤500). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤100) — the length of the arraya.
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤n) — the elements of arraya.
Note that there arenoconstraints on the sum ofnover all test cases.

## Output
For each test case, output the maximum size of a subsequence of arrayathat is beautiful.