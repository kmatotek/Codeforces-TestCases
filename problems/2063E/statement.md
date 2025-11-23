# Problem Description


You are given a rooted tree∗containingnvertices rooted at vertex1. A pair of vertices(u,v)is called agood pairifuis not an ancestor†ofvandvis not an ancestor ofu. For any two vertices,dist(u,v)is defined as the number of edges on the unique simple path fromutov, andlca(u,v)is defined as theirlowest common ancestor.
A functionf(u,v)is defined as follows.
You need to find the following value:n−1∑i=1n∑j=i+1f(i,j).
∗A tree is a connected graph without cycles.  A rooted tree is a tree where one vertex is special and called the root.
†An ancestor of vertexvis any vertex on the simple path fromvto the root, including the root, but not includingv. The root has no ancestors.
‡A triangle with side lengthsa,b,cis non-degenerate whena+b>c,a+c>b,b+c>a.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤3⋅105).
Each of the nextn−1lines contains two integersuiandvi, denoting the two vertices connected by an edge (1≤ui,vi≤n,ui≠vi).
It is guaranteed that the given edges form a tree.
It is guaranteed that the sum ofnover all test cases does not exceed3⋅105.

## Output
For each test case, output the answer on a separate line.