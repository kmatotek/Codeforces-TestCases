# Problem Description

You are given an integer arrayaof sizen. Initially, all elements of the array are colored red.
You have to choose exactlykelements of the array and paint them blue. Then, while there is at least one red element, you have to select any red element with a blue neighbor and make it blue.
The cost of painting the array is defined as the sum of the firstkchosen elements and the last painted element.
Your task is to calculate the maximum possible cost of painting for the given array.

## Input
The first line contains a single integert(1≤t≤103) — the number of test cases.
The first line of each test case contains two integersnandk(2≤n≤5000;1≤k<n).
The second line containsnintegersa1,a2,…,an(1≤ai≤109).
Additional constraint on the input: the sum ofnover all test cases doesn't exceed5000.

## Output
For each test case, print a single integer — the maximum possible cost of painting for the given array.