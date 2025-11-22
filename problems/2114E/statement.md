# Problem Description

Once, Kirei stealthily infiltrated the trap-filled estate of the Ainzbern family but was discovered by Kiritugu's familiar. Assessing his strength, Kirei decided to retreat. The estate is represented as a tree with $$$n$$$ vertices, with therootat vertex $$$1$$$. Each vertex of the tree has a number $$$a_i$$$ recorded, which represents thedangerof vertex $$$i$$$. Recall that a tree is a connected undirected graph without cycles.
For a successful retreat, Kirei must compute thethreatvalue for each vertex. Thethreatof a vertex is equal to themaximumalternatingsum along the vertical path starting from that vertex. Thealternatingsum along the vertical path starting from vertex $$$i$$$ is defined as $$$a_i - a_{p_i} + a_{p_{p_i}} - \ldots$$$, where $$$p_i$$$ is the parent of vertex $$$i$$$ on the path to the root (to vertex $$$1$$$).
For example, in the tree below, vertex $$$4$$$ has the following vertical paths:
Help Kirei compute thethreatvalues for all vertices and escape the estate.

## Input
The first line contains an integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The following describes the test cases.
The first line contains an integer $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$) — the number of vertices in the tree.
The second line contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \le a_i \le 10^9$$$) — thedangersof the vertices.
The next $$$n - 1$$$ lines contain the numbers $$$v, u$$$ ($$$1 \le v, u \le n$$$, $$$v \neq u$$$) — the description of the edges of the tree.
It is guaranteed that the sum of $$$n$$$ across all test cases does not exceed $$$2 \cdot 10^5$$$. It is also guaranteed that the given set of edges forms a tree.

## Output
For each test case, output $$$n$$$ integers — thethreatof each vertex.