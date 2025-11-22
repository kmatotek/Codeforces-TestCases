# Problem Description

If I was also hit by an apple falling from an apple tree, could I become as good at physics as Newton?
To be better at physics, Ain wants to build an apple tree so that she can get hit by apples on it. Her apple tree hasnnodes and is rooted at1. She defines theweightof an apple tree asn∑i=1n∑j=i+1dep(lca(i,j)).
Here,dep(x)is defined as the number of edges on the unique shortest path from node1to nodex.lca(i,j)is defined as the unique nodexwith the largest value ofdep(x)and which is present on both the paths(1,i)and(1,j).
From some old books Ain reads, she knows that Newton's apple tree's weight is aroundk, but the exact value of it is lost.
As Ain's friend, you want to build an apple tree withnnodes for her, and the absolute difference between your tree's weight andkshould beat most1, i.e.|weight−k|≤1. Unfortunately, this is not always possible, in this case please report it.


## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains two numbersn,k(2≤n≤105,0≤k≤1015).
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, first outputYesif a solution exists orNoif no solution exists. You may print each character in either case, for exampleYESandyEswill also be accepted.
If there's at least one solution, printn−1lines and each line contains two numbersu,v(1≤u,v≤n)represents the apple tree.