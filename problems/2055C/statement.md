# Problem Description


In the wilderness lies a region of mountainous terrain represented as a rectangular grid withnrows andmcolumns. Each cell in the grid is identified by its position(i,j), whereiis the row index andjis the column index. The altitude of cell(i,j)is denoted byai,j.
However, this region has been tampered with. A path consisting ofn+m−1cells, starting from the top-left corner(1,1)and ending at the bottom-right corner(n,m), has been cleared. For every cell(i,j)along this path, the altitudeai,jhas been set to0. The path moves strictly via downward (D) or rightward (R) steps.
To restore the terrain to its original state, it is known that the region possessed a magical property before it was tampered with: all rows and all columns shared the same sum of altitudes. More formally, there exists an integerxsuch that∑mj=1ai,j=xfor all1≤i≤n, and∑ni=1ai,j=xfor all1≤j≤m.
Your task is to assign new altitudes to the cells on the path such that the above magical property is restored. It can be proven that a solution always exists. If there are multiple solutions that satisfy the property, any one of them may be provided.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains two integersnandm(2≤n,m≤1000) — the number of rows and columns in the grid.
The second line of each test case contains a stringsof lengthn+m−2(si=Dorsi=R) — the steps the path makes from(1,1)to(n,m). The characterDrepresents a downward step, andRrepresents a rightward step.
Thei-th of the nextnlines each containmintegersai,1,ai,2,…,ai,m(−106≤ai,j≤106) — the altitude of each cell in the grid. It is guaranteed that if a cell(i,j)lies on the path, thenai,j=0.
It is guaranteed that the sum ofn⋅mover all test cases does not exceed106.

## Output
For each test case, outputnlines ofmintegers representing the restored grid of altitudesbi,j. The altitudes must satisfy−1015≤bi,j≤1015, and additionallyai,j=bi,jif(i,j)is not on the path. If multiple solutions exist, output any of them.