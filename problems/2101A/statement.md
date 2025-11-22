# Problem Description


You are givenn2cards with values from0ton2−1. You are to arrange them in anbyngrid such that there isexactlyone card in each cell.
The MEX (minimum excluded value) of a subgrid∗is defined as the smallest non-negative integer that does not appear in the subgrid.
Your task is to arrange the cards such that the sum of MEX values over all(n(n+1)2)2subgrids is maximized.
∗A subgrid of anbyngrid is specified by four numbersl1,r1,l2,r2satisfying1≤l1≤r1≤nand1≤l2≤r2≤n. The element in thei-th row and thej-th column of the grid is part of the subgrid if and only ifl1≤i≤r1andl2≤j≤r2.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤100). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤500) — the side length of the grid.
It is guaranteed that the sum ofnover all test cases does not exceed1000.

## Output
For each test case, outputnlines, each containingnintegers representing the elements of the grid.
If there are multiple answers, you can output any of them.