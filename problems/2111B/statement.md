# Problem Description

There arenFibonacci cubes, where the side of thei-th cube is equal tofi, wherefiis thei-th Fibonacci number.
In this problem, the Fibonacci numbers are defined as follows:
There are alsomempty boxes, where thei-th box has a width ofwi, a length ofli, and a height ofhi.
For each of themboxes, you need to determine whether all the cubes can fit inside that box. The cubes must be placed in the box following these rules:

## Input
Each test consists of several test cases. The first line contains a single integert(1≤t≤103) — the number of test cases. The description of the test cases follows.
In the first line of each test case, there are two integersnandm(2≤n≤10,1≤m≤2⋅105) — the number of cubes and the number of empty boxes.
The nextmlines of each test case contain3integerswi,li, andhi(1≤wi,li,hi≤150) — the dimensions of thei-th box.
Additional constraints on the input:

## Output
For each test case, output a string of lengthm, where thei-th character is equal to "1" if allncubes can fit into thei-th box; otherwise, thei-th character is equal to "0".