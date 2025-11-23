# Problem Description


You are given an undirected graph withnvertices, labeled from1ton. This graph encodes a hidden permutation∗pof sizen. The graph is constructed as follows:
Your task is to reconstruct and output the permutationp. It can be proven that permutationpcan be uniquely determined.
∗A permutation of lengthnis an array consisting ofndistinct integers from1tonin arbitrary order. For example,[2,3,1,5,4]is a permutation, but[1,2,2]is not a permutation (2appears twice in the array), and[1,3,4]is also not a permutation (n=3but there is4in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤500). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤1000).
Thei-th of the nextnlines contains a string ofncharactersgi,1gi,2…gi,n(gi,j=0orgi,j=1) — the adjacency matrix.gi,j=1if and only if there is an edge between vertexiand vertexj.
It is guaranteed that there exists a permutationpwhich generates the given graph. It is also guaranteed that the graph is undirected and has no self-loops, meaninggi,j=gj,iandgi,i=0.
It is guaranteed that the sum ofnover all test cases does not exceed1000.

## Output
For each test case, outputnintegersp1,p2,…,pnrepresenting the reconstructed permutation.