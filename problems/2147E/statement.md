# Problem Description

You are given an array ofnnon-negative integers.
You want to answer givenqindependent scenarios. In thei-th scenario, you are allowed to perform the following operationat mostbitimes:
Your goal is to maximize the number of bits that are equal to1in thebitwise ORof all numbers in the array. Find this number for each scenario.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤103). The description of the test cases follows.
The first line of each test case contains two integersnandq(1≤n,q≤105) — the size of the array and the number of scenarios.
The second line containsnintegersa1,a2,…,an(0≤ai≤109) — the elements of the array.
Thei-th of the nextqlines contains a single integerbi(0≤bi≤109) — the maximum number of operations allowed in thei-th scenario.
It is guaranteed that the sum ofnover all test cases does not exceed105, and the sum ofqover all test cases does not exceed105.

## Output
For each test case, outputqlines, thei-th of them containing a single integer — the maximum possible number of bits equal to1in the bitwise OR in thei-th scenario.