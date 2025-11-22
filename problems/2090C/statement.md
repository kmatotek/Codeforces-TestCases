# Problem Description

Inside the large kingdom, there is an infinite dining hall. It can be represented as a set of cells (x,y), wherexandyare non-negative integers. There are an infinite number of tables in the hall. Each table occupies four cells (3x+1,3y+1), (3x+1,3y+2), (3x+2,3y+1), (3x+2,3y+2), wherexandyare arbitrary non-negative integers. All cells that do not belong to any of the tables are corridors.
There arenguests that come to the dining hall one by one. Each guest appears in the cell(0,0)and wants to reach a table cell. In one step, they can move to any neighboring by sidecorridorcell, and in theirlaststep, they must move to a neighboring by side a freetablecell. They occupy the chosen table cell, and no other guest can move there.
Each guest has a characteristicti, which can either be0or1. They enter the hall in order, starting to walk from the cell (0,0). Ifti=1, thei-th guest walks to the nearest vacant table cell. Ifti=0, they walk to the nearest table cell that belongs to a completely unoccupied table. Note that other guests may choose the same table later.
The distance is defined as the smallest number of steps needed to reach the table cell. If there are multiple table cells at the same distance, the guests choose the cell with the smallestx, and if there are still ties, they choose among those the cell with the smallesty.
For each guest, find the table cell which they choose.

## Input
The first line contains a single integerq(1≤q≤5000) — the number of test cases. Then follows their description.
The first line of each test case contains a single integern(1≤n≤50000) — the number of guests.
The second line of each test case containsnintegerst1,t2,…,tn(ti∈{0,1}) — the characteristics of the guests.
It is guaranteed that the sum ofnfor all test cases does not exceed50000.

## Output
For each test case, outputnlines — for each guest, the cell where they sit.