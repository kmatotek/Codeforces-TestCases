# Problem Description


It's already a hot April outside, and Polycarp decided that this is the perfect time to finally take down the spruce tree he set up several years ago. As he spent several hours walking around it, gathering his strength, he noticed something curious: the spruce is actually a tree∗— and not just any tree, but one consisting of anoddnumber of verticesn. Moreover, onn−1of the vertices hang Christmas ornaments, painted in exactlyn−12distinct colors, with exactly two ornaments painted in each color. The remaining vertex, as tradition dictates, holds the tree's topper.
At last, after several days of mental preparation, Polycarp began dismantling the spruce. First, he removed the topper and had already started taking apart some branches when suddenly a natural question struck him: how can he remove one of the tree's edges and rearrange the ornaments in such a way that the sum of the lengths of the simple paths between ornaments of the same color is as large as possible?
In this problem, removing an edge from the tree is defined as follows: choose a pair of adjacent verticesaandb(a<b), then remove vertexbfrom the tree and reattach all ofb's adjacent vertices (except fora) directly toa.
Polycarp cannot continue dismantling his spruce until he gets an answer to this question. However, checking all possible options would take him several more years. Knowing your experience in competitive programming, he turned to you for help. But can you solve this dispute?
∗A tree is a connected graph without cycles.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains anoddnumbern(3≤n<2⋅105) — the number of vertices in the tree.
The followingn−1lines describe the tree, given by pairs of adjacent verticesu,v(1≤u,v≤n,u≠v).
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, you need to output two lines.
In the first line, output the pair of verticesu,v, the edge between which Polycarp is going to remove.
In the next line, output the arraycofnnumbers from0ton−12, wherec[i]— the positive color number assigned to vertexi. Note thatc[max(u,v)]=0, since this vertex has been removed.