# Problem Description

There is a directed acyclic graph withnnodes andmedges. Each node is initially colored blue.
Let's define thefun graph gameas follows:
Since the graph is acyclic, it can be shown that the game always ends in a finite number of turns.
Note that Cry and River can win the game immediately if the starting nodesdoesn't have outgoing edges, or is red respectively.
You must handleqqueries of the following kind:

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains three integersn,m,q(2≤n≤2⋅105,1≤m,q≤2⋅105).
The followingmlines each contain two integersuandv(1≤u,v≤n), meaning that there is an edge fromutov.
The followingqlines each contain two integersxandu(1≤x≤2,1≤u≤n) – denoting the type of query and the node that the query is done on.
It is guaranteed that the given graph is a directed acyclic graph. Additionally, no edge is given more than once.
It is guaranteed that the sum ofn, the sum ofm, and the sum ofqeach do not exceed2⋅105over all test cases.

## Output
For each query of the second type, outputYESif Cry wins. Otherwise, outputNO. Each letter may be outputted in uppercase or lowercase.