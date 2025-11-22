# Problem Description


You are given a tree withnvertices, where each vertex can be colored red, blue, or white. Thecoolnessof a coloring is defined as the maximum distance∗between a red and a blue vertex.
Formally, if we denote the color of thei-th vertex asci, the coolness of a coloring ismaxd(u,v)over all pairs of vertices1≤u,v≤nwherecuisredandcvisblue. If there are no red or no blue vertices, the coolness is zero.
Your task is to calculate the sum of coolness over all3npossible colorings of the tree, modulo998244353.
∗The distance between two verticesaandbin a tree is equal to the number of edges on the unique simple path between vertexaand vertexb.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤50). The description of the test cases follows.
The first line of each test case contains a single integern(2≤n≤3000) — the number of vertices in the tree.
Each of the nextn−1lines contains two integersuandv(1≤u,v≤n) — the endpoints of the edges of the tree.
It is guaranteed that the given edges form a tree.
It is guaranteed that the sum ofnover all test cases does not exceed3000.

## Output
For each test case, output the sum of coolness over all3npossible colorings of the tree, modulo998244353.