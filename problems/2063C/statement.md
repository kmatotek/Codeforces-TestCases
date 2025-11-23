# Problem Description


You are given a tree∗ofnvertices. You must perform the following operationexactly twice.
Please find the maximum number of connected components after performing the operationexactly twice.
Two verticesxandyare in the same connected component if and only if there exists a path fromxtoy. For clarity, note that the graph with0vertices has0connected components by definition.†
∗A tree is a connected graph without cycles.
†But is such a graph connected?

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(2≤n≤2⋅105).
Each of the nextn−1lines contains two integersuiandvi, denoting the two vertices connected by an edge (1≤ui,vi≤n,ui≠vi). It is guaranteed that the given edges form a tree.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output the maximum number of connected components on a separate line.