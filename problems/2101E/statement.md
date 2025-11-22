# Problem Description


You are given a binary stringsof lengthnand a treeTwithnvertices. Letkbe the number of1s ins. We will construct a complete undirected weighted graph withkvertices as follows:
Asimplepath†that visits vertices labeledv1,v2,…,vmin this order isniceif for all1≤i≤m−2, the condition2⋅w(vi,vi+1)≤w(vi+1,vi+2)holds. In other words, the weight of each edge in the path must be at least twice the weight of the previous edge. Note thatsvi=1has to be satisfied for all1≤i≤m, as otherwise, there would be no vertex with the corresponding label.
For each vertex labeledi(1≤i≤nandsi=1) in the complete undirected weighted graph, determine the maximum number of vertices in any nice simple path starting from the vertex labeledi.
∗The distance between two verticesaandbin a tree is equal to the number of edges on the unique simple path between vertexaand vertexb.
†A path is a sequence of verticesv1,v2,…,vmsuch that there is an edge betweenviandvi+1for all1≤i≤m−1. A simple path is a path with no repeated vertices, i.e.,vi≠vjfor all1≤i<j≤m.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤7⋅104) — the length of the binary stringsand the number of vertices in the treeT.
The second line of each test case contains a binary string withncharacterss1s2…sn(si∈{0,1}) — the string representing the vertices to be constructed in the complete undirected weighted graph.
Each of the nextn−1lines contains two integersuandv(1≤u,v≤n) — the endpoints of the edges of the treeT.
It is guaranteed that the given edges form a tree.
It is guaranteed that the sum ofnover all test cases does not exceed7⋅104.

## Output
For each test case, outputnintegers, thei-th integer representing the maximum number of vertices in any nice simple path starting from the vertex labeledi. If there is no vertex labeledi, i.e.,si=0, output−1instead.