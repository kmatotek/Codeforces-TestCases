# Problem Description

A cat lives on a tree withnnodes. The cat starts on node1, and you live on noden. You are going to leave the cat a note written in the parkour language to help it reach you.
The parkour language has two types of instructions:
Additionally, there cannot be two consecutive instances of the second instruction.
Unfortunately, the parkour language is ambiguous because the cat may have multiple options for each instance of the first instruction. So you should construct a sequence of instructions of length at most3nso that if the cat follows them, it will end at noden, no matter what choices it makes. It can be proven that such a sequence exists for any tree.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each testcase contains an integern(2≤n≤2⋅105) — the size of the tree.
Thenn−1lines follow, each of them contains two integersuandv(1≤u,v≤n,u≠v) which describe a pair of vertices connected by an edge. It is guaranteed that the given graph is a tree and has no loops or multiple edges.
The sum ofnacross all testcases does not exceed2⋅105.

## Output
For each testcase, output a single integerk(0≤k≤3n) — the number of operations you will perform.
Then outputklines of either of the following formats: