# Problem Description

Akito decided to study a new powerful spell. Since it possesses immeasurable strength, it certainly requires a lot of space and careful preparation. For this, Akito went out into the field. Let's represent the field as a Cartesian coordinate system.
For the spell, Akito needs to place0≤n≤500staffs atdistinct integer coordinatesin the field such that there will beexactlykpairs(i,j)such that1≤i<j≤nandρ(i,j)=d(i,j).
Here, for two points with integer coordinatesa=(xa,ya)andb=(xb,yb),ρ(a,b)=√(xa−xb)2+(ya−yb)2andd(a,b)=|xa−xb|+|ya−yb|.

## Input
The first line of input contains a single numbert(1≤t≤1000) — the number of test cases.
In the only line of each test case, there is a single numberk(0≤k≤105) — the number of pairs of staffs for which the equalityρ(i,j)=d(i,j)must hold.

## Output
For each test case, the first line of output should print the numbern(0≤n≤500) — the number of placed staffs.
In the followingnlines, pairs ofintegersxi,yi(−109≤xi,yi≤109)should be printed — the coordinates of thei-th staff. The points in which staffs stand must be distinct.