# Problem Description


Pizano built an arrayaofntowers, each consisting ofai≥0blocks.
Pizano can knock down a tower so that the nextaitowers grow by1. In other words, he can take the elementai, increase the nextaielements by one, and then setaito0. The blocks that fall outside the array of towers disappear. If Pizano knocks down a tower with0blocks, nothing happens.
Pizano wants to knock down allntowers in any order,each exactly once. That is, for eachifrom1ton, he will knock down the tower at positioniexactly once.
Moreover, the resulting array of tower heightsmust be non-decreasing. This means that after he knocks down allntowers, for anyi<j, the tower at positionimust not be taller than the tower at positionj.
You are required to output the maximumMEXof the resulting array of tower heights.
TheMEXof an array is the smallest non-negative integer that is not present in the array.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains an integern(1≤n≤105) — the number of towers.
The second line of each test case containsnintegers — the initial heights of the towersa1,…,an(0≤ai≤109).
It is guaranteed that the sum ofnover all test cases does not exceed105.

## Output
For each test case, output a single integer — the maximumMEXof the final array.