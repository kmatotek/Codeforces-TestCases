# Problem Description

Aquadtreeis a tree data structure in which each node has at most four children and accounts for a square-shaped region.
Formally,for all tuplesof nonnegative integersk,a,b≥0, there existsexactly one nodeaccounting for the following region∗.
[a⋅2k,(a+1)⋅2k]×[b⋅2k,(b+1)⋅2k]
All nodes whose region is larger than1×1contain four children corresponding to the regions divided equally into four, and the nodes whose region is1×1correspond to the leaf nodes of the tree.
The Frontman hates the widespread misconception, such that the quadtree can perform range queries inO(logn)time when there arenleaf nodes inside the region. In fact, sometimes it is necessary to query much more thanO(logn)regions for this, and the time complexity isO(n)in some extreme cases. Thus, the Frontman came up with this task to educate you about this worst case of the data structure.
The pink soldiers have given you a finite region[l1,r1]×[l2,r2], whereliandri(li<ri) are nonnegative integers. Please find the minimum number of nodes that you must choose in order to make the union of regions accounted for by the chosen nodesexactlythe same as the given region. Here, two sets of points are considered different if there exists a point included in one but not in the other.
∗Regions are sets of pointswith real coordinates, where the point(x,y)is included in the region[p,q]×[r,s]if and only ifp≤x≤qandr≤y≤s. Here,×formally refers toCartesian product of sets.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The only line of each test case contains four integersl1,r1,l2,r2— the boundaries of the region in each axis (0≤li<ri≤106).

## Output
For each test case, output the minimum number of nodes necessary to satisfy the condition on a separate line.