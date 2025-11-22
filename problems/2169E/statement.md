# Problem Description

Alice and Bob are playing with points on the XY plane. Initially, there arenpoints on the plane: thei-th point is located at(xi,yi)and has a cost ofci.
The game consists of two stages:
After that, the game ends and the total score is calculated. The total score of the game is the sum of the costs of theremovedpoints by Alice and theperimeterof the rectangle drawn by Bob. Alice wants to maximize the score, while Bob wants to minimize it.
Determine the total score of the game if both Alice and Bob play optimally.
Theperimeterof the rectangle is equal to the sum of the lengths of all itsfoursides. Therefore, even if the rectangle degenerates into a line segment of lengthk, its perimeter will be2k. The perimeter of a rectangle that degenerates into a point is0.

## Input
The first line contains a single integert(1≤t≤104) — the number of test cases.
The first line of each test case contains a single integern(1≤n≤3⋅105) — the number of points on the plane.
The second line of each test case containsnintegersx1,x2,…,xn(0≤xi≤1015) — thex-coordinates of the points.
The third line containsnintegersy1,y2,…,yn(0≤yi≤1015) — they-coordinates of the points.
The fourth line containsnintegersc1,c2,…,cn(0≤ci≤109) — the costs of the points.
Additional constraints on the input:

## Output
For each test case, output a single integer — the final score of the game if both Alice and Bob play optimally.