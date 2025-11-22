# Problem Description

For a set of pairsS={(a1,b1),(a2,b2),…,(am,bm)}, whereai<bifor all1≤i≤m, we definef(S)andg(S)as follows:

For example,S={(1,2),(2,4),(1,4),(4,5),(6,7)}, we can getf(S)=5andg(S)=3.
You are givenndistinctpairs. Your task is to select a subsetS′of these pairs such thatf(S′)−g(S′)is maximized. You need to output the indices of the selected pairs.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains an integern(1≤n≤3⋅103).
Nextnlines each contain two integersaiandbi(1≤ai<bi≤2n), representing a pair.
It is guaranteed that all pairs aredistinctwithin the same test case.
It is guaranteed that the sum ofn2over all test cases will not exceed9⋅106.

## Output
For each test case, the first line contains an integerk(0≤k≤n) — the size of the subsetS′.
Next line containskintegersi1,i2,…,im(1≤i1,i2,…,ik≤n) — the indices of the selected pairs. Note the indices must bedistinct.