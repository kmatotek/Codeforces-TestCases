# Problem Description

Mouf, the clever master of Darkness, and Fouad, the brave champion of Light, have entered the Grid Realm once more. This time, they have found the exit, but it is guarded by fierce monsters! They must fight with their bare hands instead of summoning monsters!
Mouf and Fouad are standing on ann×ngrid. Each cell(i,j)has a valueai,jand a color. The color of a cell is white ifci,j=0and black ifci,j=1.
Mouf starts at the top-left corner(1,1), and Fouad starts at the bottom-left corner(n,1). Both are trying to reach the exit cell at(r,n).
A path is defined as a sequence of adjacent cells (sharing a horizontal or vertical edge). The cost of a path is the maximum value ofai,jamong all cells included in the path (including the first and last cells).
Let:
Before moving, Mouf can perform up tokoperations. In each operation, he may select any black cell and increment its value by1(possibly choosing the same cell multiple times).
Mouf wants to maximizedisFwhile ensuring that his own costdisMremainsunchanged(as if he performed no operations). If Mouf acts optimally, what are the values ofdisManddisF?

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤103). The description of the test cases follows.
The first line of each test case contains three integersn,r, andk(2≤n≤300,1≤r≤n,0≤k≤106) — the length of the grid, the row number of the exit cell, and the number of allowed operations.
Thei-th of the nextnlines containsnintegersai,1,ai,2,…,ai,n(1≤aij≤106) — the values of the cells in thei-th row.
Thei-th of the nextnlines contains a binary stringciof lengthn— denoting the color of the cells in thei-th row (cell(i,j)is white ifci,j=0and black ifci,j=1).
It is guaranteed that the sum ofn2over all test cases does not exceed9⋅104.

## Output
For each test case, output two integers —disManddisFif Mouf performs the operations optimally.