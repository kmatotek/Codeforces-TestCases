# Problem Description

In a two-dimensional universe, a star can be represented by a point(x,y)on a two-dimensional plane. Two stars are directly connected if and only if theirxorycoordinates are the same, and there are no other stars on the line segment between them. Define a galaxy as a connected component composed of stars connected directly or indirectly (through other stars).
For a set of stars, its value is defined as the minimum number of galaxies that can be obtained after performing the following operation for any (possibly, zero) times: in each operation, you can select a point(x,y)without stars. If a star can be directly connected to at least3stars after creating it here, then you create a star here.
You are given an×nmatrixaconsisting of0and1describing a setSof stars. There is a star at(x,y)if and only ifax,y=1. Calculate the sum, modulo109+7, of the values of all non-empty subsets ofS.

## Input
The first line of input contains a single integert(1≤t≤100) — the number of test cases.
For each test case, the first line contains a single integern(1≤n≤14) — the size of matrixa.
Thennlines follow; thei-th line contains a stringaiof lengthn— thei-th row of matrixa.
It is guaranteed that the sum of2nover all test cases does not exceed214.

## Output
For each test case, output the sum, modulo109+7, of the values of all non-empty subsets ofS.