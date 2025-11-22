# Problem Description

D. Pippy is preparing for a "black-and-white" party at his home. He only needs to repaint the floor in his basement, which can be represented as a board of sizen×m𝑛×𝑚.
After the last party, the entire board is painted green, except for somekcells(x1,y1),(x2,y2),…,(xk,yk), each of which is painted either white or black. For the upcoming party, D. Pippy wants to painteachof the remaining green cells either black or white. At the same time, he wants the number of pairs of adjacent cells with different colors on the board to be even after repainting.
Formally, ifA={((i1,j1),(i2,j2))|1≤i1,i2≤n,1≤j1,j2≤m,i1+j1<i2+j2,|i1−i2|+|j1−j2|=1,color(i1,j1)≠color(i2,j2)},wherecolor(x,y)denotes the color of the cell(x,y), then it is required that|A|be even.
Help D. Pippy find the number of ways to repaint the floor so that the condition is satisfied. Since this number can be large, output the remainder of its division by109+7.

## Input
Each test consists of several test cases. The first line of the input data contains one integert(1≤t≤104) — the number of test cases. The description of the test cases follows.
The first line of each test case contains three integersn,m,k(3≤n,m≤109;1≤k≤2⋅105) — the dimensions of the board and the number of cells that are initially not green.
In thei-th of the followingklines of each test case, there are three integersxi,yiandci(1≤xi≤n;1≤yi≤m;ci∈{0,1}) — the coordinates of the cell and its color (if white, thenci=0; if black, thenci=1). It is guaranteed that all cells are distinct.
It is guaranteed that the sum ofkacross all test cases does not exceed2⋅105.

## Output
For each test case, output a single integer — the answer modulo109+7.