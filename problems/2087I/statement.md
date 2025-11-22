# Problem Description

You are given a directed acyclic graph withnvertices andmedges. The graph contains no cycles or multiple edges.
You need to partition all the edges of this graph into Hamiltonian cycles (cycles that visit each of thenvertices of the graph exactly once) such that each edge belongs to exactly one cycle. It is obvious that this is impossible for the original graph, so before partitioning, you must add theminimumnumber of edges to the graph so that such a partition exists.
After adding edges, the graph may contain cycles and/or multiple edges, but it should still not have any self-loops.

## Input
The first line contains two integersnandm(2≤n≤100;1≤m≤n(n−1)2).
The nextmlines contain two integersxiandyiin thei-th line (1≤xi,yi≤n;xi≠yi), representing a directed edge from vertexxito vertexyi.
Additional constraints on the input:

## Output
In the first line, output a single integerk(1≤k≤n⋅m) — the number of edges you add.
Then outputklines, in thei-th of which there should be two integersxiandyi(1≤xi,yi≤n;xi≠yi), denoting the start and end of the next edge.
Then in a single line, output a single integerc(1≤c≤m) — the number of Hamiltonian cycles into which you partition all the edges of the graph.
In the last line, outputm+kintegersa1,a2,…,am+k(1≤ai≤c), whereaiis the Hamiltonian cycle to which you assign thei-th edge (the edges of the original graph are numbered from1tom, and the new ones are fromm+1tom+k).
If there are multiple answers that minimize the number of added edges, output any of them.