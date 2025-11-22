# Problem Description


You are given a tree∗withnvertices. Over time, each vertexi(1≤i≤n) has a probability ofpiqiof falling. Determine the expected value of the number of unordered pairs†ofdistinctvertices that become leaves‡in the resulting forest§, modulo998244353.
Note that when vertexvfalls, it is removed along with all edges connected to it. However, adjacent vertices remain unaffected by the fall ofv.
∗A tree is a connected graph without cycles.
†An unordered pair is a collection of two elements where the order in which the elements appear does not matter. For example, the unordered pair(1,2)is considered the same as(2,1).
‡A leaf is a vertex that is connected to exactly one edge.
§A forest is a graph without cycles

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤105).
Thei-th line of the followingnlines contains two integerspiandqi(1≤pi<qi<998244353).
Each of the followingn−1lines contains two integersuandv(1≤u,v≤n,u≠v) — the indices of the vertices connected by an edge.
It is guaranteed that the given edges form a tree.
It is guaranteed that the sum ofnover all test cases does not exceed105.

## Output
For each test case, output a single integer — the expected value of the number of unordered pairs of distinct vertices that become leaves in the resulting forest modulo998244353.
Formally, letM=998244353. It can be shown that the exact answer can be expressed as an irreducible fractionpq, wherepandqare integers andq≢0(modM). Output the integer equal top⋅q−1modM. In other words, output such an integerxthat0≤x<Mandx⋅q≡p(modM).