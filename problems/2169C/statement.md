# Problem Description

You are given an integer arrayaof lengthn.
You can perform the following operation: choose a range[l,r](1≤l≤r≤n) and replace the value of elementsal,al+1,…,arwith(l+r).
Your task is to calculate the maximum possible total array sum if you can perform the aforementioned operation at most once.

## Input
The first line contains a single integert(1≤t≤104) — the number of test cases.
The first line of each test case contains a single integern(1≤n≤2⋅105).
The second line containsnintegersa1,a2,…,an(0≤ai≤2n).
Additional constraint on the input: the sum ofnover all test cases doesn't exceed2⋅105.

## Output
For each test case, print a single integer — the maximum possible total array sum if you can perform the aforementioned operation at most once.