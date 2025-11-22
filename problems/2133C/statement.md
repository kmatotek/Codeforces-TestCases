# Problem Description


This is an interactive problem.
Having recently discovered The Nether, Steve has built a network of $$$n$$$ nether portals, each at a different location in his world.
Each portal is connected in one direction to some number (possibly zero) of other portals. To avoid getting lost, Steve has carefully built the network of portals so that there is no sequence of jumps through portals that will bring you from a location back to itself; formally, the network forms a directed acyclic graph.
Steve refuses to tell you which portals are connected to which, but he will allow you to ask queries. In each query, you give Steve a set of locations $$$S = \{s_1, s_2, \ldots, s_k\}$$$ and a starting location $$$x \in S$$$. Steve will figure out the longest path starting at $$$x$$$ that only passes through locations in $$$S$$$ and tell you the number of locations in it. (If it is impossible to reach any other location in $$$S$$$ from $$$x$$$, Steve will reply with $$$1$$$.)
As you are looking to obtain the achievement "Hot Tourist Destinations", you want to find any path that visits as many locations as possible. Steve is feeling particularly generous and will give you $$$2 \cdot n$$$ queries to find it.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 1000$$$). The description of the test cases follows.
The only line of each test case contains a single integer $$$n$$$ ($$$2 \le n \le 500$$$) — the number of locations.
It is guaranteed that the sum of $$$n^3$$$ over all test cases does not exceed $$$500^3$$$.
