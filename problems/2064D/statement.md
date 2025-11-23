# Problem Description

There arenslimes on a line, thei-th of which has weightwi. Slimeiis able to eat another slimejifwi≥wj; afterwards, slimejdisappears and the weight of slimeibecomeswi⊕wj∗.
The King of Slimes wants to run anexperiment with parameterxas follows:
The King of Slimes is going to ask youqqueries. In each query, you will be given an integerx, and you need to determine the score of the experiment with parameterx.
Note that the King does not want you to actually perform each experiment; his slimes would die, which is not ideal. He is only asking what the hypothetical score is; in other words, the queries arenotpersistent.
∗Here⊕denotes thebitwise XOR operation.

## Input
The first line contains an integert(1≤t≤104) — the number of test cases.
The first line of each test case contains integersnandq(1≤n,q≤2⋅105) — the number of slimes and the number of queries, respectively.
The following line containsnintegersw1,w2,…,wn(1≤wi<230) — the weights of the slimes.
The followingqlines contain a single integerx(1≤x<230) — the parameter for the experiment.
The sum ofndoes not exceed2⋅105and the sum ofqdoes not exceed2⋅105across all test cases.

## Output
For each query, output a single integer — the score of the experiment.