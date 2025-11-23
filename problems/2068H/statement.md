# Problem Description

The mayor of a city wants to placenstatues at intersections around the city. The intersections in the city are at all points(x,y)with integer coordinates. Distances between intersections are measured using Manhattan distance, defined as follows:distance((x1,y1),(x2,y2))=|x1−x2|+|y1−y2|.
The city council has provided the following requirements for the placement of the statues:
It is allowed to place multiple statues at the same intersection.
Help the mayor find a valid arrangement of thenstatues, or determine that it does not exist.

## Input
The first line contains an integern(3≤n≤50) — the number of statues.
The second line contains two integersaandb(0≤a,b≤109) — the coordinates of the intersection where then-th statue must be placed.
The third line containsn−1integersd1,…,dn−1(0≤di≤109) — the distance between thei-th statue and the(i+1)-th statue.

## Output
PrintYESif there is a valid arrangement of thenstatues. Otherwise, printNO.
If there is a valid arrangement, print a valid arrangement in the followingnlines. Thei-th of these lines must contain two integersxiandyi— the coordinates of the intersection where thei-th statue is placed. You can print any valid arrangement if multiple exist.