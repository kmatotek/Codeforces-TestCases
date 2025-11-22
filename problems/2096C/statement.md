# Problem Description

You are the proud leader of a city in Ancient Berland. There aren2buildings arranged in a grid ofnrows andncolumns. The height of the building in rowiand columnjishi,j.
The city isbeautifulif no two adjacent by side buildings have the same height. In other words, it must satisfy the following:
There arenworkers at company A, andnworkers at company B. Each worker can be hiredat most once.
It costsaicoins to hire workeriat company A. After hiring, workeriwill:
It costsbjcoins to hire workerjat company B. After hiring, workerjwill:
Find the minimum number of coins needed to make the city beautiful, or report that it is impossible.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤100). The description of the test cases follows.
The first line of each test case contains a single integern(2≤n≤1000) — the size of the grid.
Thei-th of the nextnlines of each test case containsnintegershi,1,hi,2,…,hi,n(1≤hi,j≤109) — the heights of the buildings in rowi.
The next line of each test case containsnintegersa1,a2,…,an(1≤ai≤109) — the costs of hiring the workers at company A.
The next line of each test case containsnintegersb1,b2,…,bn(1≤bj≤109) — the costs of hiring the workers at company B.
It is guaranteed that the sum ofnover all test cases does not exceed1000.

## Output
For each test case, output a single integer — the minimum number of coins needed, or−1if it is impossible.