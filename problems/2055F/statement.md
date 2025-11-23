# Problem Description


Apolyominois a connected∗figure constructed by joining one or more equal1×1unit squares edge to edge. A polyomino isconvexif, for any two squares in the polyomino that share the same row or the same column, all squares between them are also part of the polyomino. Below are four polyominoes, only the first and second of which are convex.
You are given a convex polyomino withnrows and an even area. For each rowifrom1ton, the unit squares from columnlito columnriare part of the polyomino. In other words, there areri−li+1unit squares that are part of the polyomino in thei-th row:(i,li),(i,li+1),…,(i,ri−1),(i,ri).
Two polyominoes arecongruentif and only if you can make them fit exactly on top of each other by translating the polyominoes.Note that you are not allowed to rotate or reflect the polyominoes.Determine whether it is possible to partition the given convex polyomino into two disjoint connected polyominoes that are congruent to each other. The following examples illustrate a valid partition of each of the two convex polyominoes shown above:
The partitioned polyominoes do not need to be convex, and each unit square should belong to exactly one of the two partitioned polyominoes.
∗A polyomino is connected if and only if for every two unit squaresu≠vthat are part of the polyomino, there exists a sequence of distinct squaress1,s2,…,sk, such thats1=u,sk=v,siare all part of the polyomino, andsi,si+1share an edge for each1≤i≤k−1.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤2⋅105) — the number of rows of the polyomino.
Thei-th of the nextnlines contains two integersliandri(1≤li≤ri≤109) — the range of columns that are part of the polyomino in thei-th row.
It is guaranteed that the area of the polyomino is even. In other words,∑ni=1ri−li+1≡0(mod2).
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, print a single line containing either "YES" or "NO", representing whether or not the polyomino can be partitioned as described in the problem.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.