# Problem Description


Thedistanceof a valuexin an arrayc, denoted asdx(c), is defined as the largest gap between any two occurrences ofxinc.
Formally,dx(c)=max(j−i)over all pairsi<jwhereci=cj=x. Ifxappears only once or not at all inc, thendx(c)=0.
Thebeautyof an array is the sum of the distances of each distinct value in the array. Formally, the beauty of an arraycis equal to∑1≤x≤ndx(c).
Given an arrayaof lengthn, an arraybisniceif it also has lengthnand its elements satisfy1≤bi≤aifor all1≤i≤n. Your task is to find the maximum possible beauty of any nice array.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤2⋅105) — the length of arraya.
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤n) — the elements of arraya.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output a single integer representing the maximum possible beauty among all nice arrays.