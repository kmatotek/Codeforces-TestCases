# Problem Description

Of course, a problem with the letter D is sponsored by Declan Akaba.
You are given a simple, connected, undirected graph withnvertices andmedges. The graph contains no self-loops or multiple edges. You are also given a multisetAconsisting ofℓelements:A={A1,A2,…,Aℓ}
Starting from vertex1, you may perform the following moveany numberof times, as long as the multisetAis not empty:
For eachi(1≤i≤n), determine whether there exists a sequence of such moves that starts at vertex1and ends at vertexi, using the original multisetA.
Note that the check for each vertexiis independent — you restart from vertex1and use the original multisetAfor each case.
∗A walk of lengthkis a sequence of verticesv0,v1,…,vk−1,vksuch that each consecutive pair of vertices(vi,vi+1)is connected by an edge in the graph. The sequence may include repeated vertices.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains three integersn,m, andℓ(2≤n≤2⋅105,n−1≤m≤4⋅105,1≤ℓ≤2⋅105) — the number of vertices, the number of edges, and the size of the multiset, respectively.
The second line of each test case containsℓintegersA1,A2,…,Aℓ(1≤Ai≤104) — the elements of the multiset.
Each of the followingmlines contains two integersuandv(1≤u<v≤n) — the endpoints of an edge in the graph.
It is guaranteed that the edges form a simple, connected graph without self-loops or multiple edges.
It is guaranteed that the sum ofn, the sum ofm, and the sum ofℓover all test cases does not exceed2⋅105,4⋅105, and2⋅105, respectively.

## Output
For each test case, output a binary string of lengthn, where thei-th character is1if there exists a sequence of moves ending at vertexi, and0otherwise.