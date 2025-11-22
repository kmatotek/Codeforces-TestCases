# Problem Description

Every airport has a baggage claim area, and Balbesovo Airport is no exception. At some point, one of the administrators at Sheremetyevo came up with an unusual idea: to change the traditional shape of the baggage claim conveyor from a carousel to a more complex form.
Suppose that the baggage claim area is represented as a rectangular grid of sizen×m. The administration proposed that the path of the conveyor should pass through the cellsp1,p2,…,p2k+1, wherepi=(xi,yi).
For each cellpiand the next cellpi+1(where1≤i≤2k), these cells must share a common side. Additionally, the path must be simple, meaning that for no pair of indicesi≠jshould the cellspiandpjcoincide.
Unfortunately, the route plan was accidentally spoiled by spilled coffee, and only the cells with odd indices of the path were preserved:p1,p3,p5,…,p2k+1. Your task is to determine the number of ways to restore the original complete pathp1,p2,…,p2k+1given thesek+1cells.
Since the answer can be very large, output it modulo109+7.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤3⋅104). The description of the test cases follows.
The first line of each test case contains three integersn,m, andk(1≤n,m≤1000,n⋅m≥3,1≤k≤⌊12(nm−1)⌋) — the dimensions of the grid and a parameter defining the length of the path.
Next, there arek+1lines, thei-th of which contains two integersx2i−1andy2i−1(1≤x2i−1≤n,1≤y2i−1≤m) — the coordinates of the cellp2i−1that lies on the path.
It is guaranteed that all pairs(x2i−1,y2i−1)are distinct.
It is guaranteed that the sumn⋅mover all test cases does not exceed106.

## Output
For each test case, output a single integer — the number of ways to restore the original complete path modulo109+7.