# Problem Description


Kagari is preparing to archive a tree, and she knows the cost of doing so will depend on its diameter$$$^{\text{∗}}$$$. To keep the expense down, her goal is to shrink the diameter as much as possible first. She can perform the following operation on the tree:
It can be shown that the graph is still a tree after the operation.
Help her determine the minimum number of operations required to achieve the minimal diameter.
$$$^{\text{∗}}$$$The diameter of a tree is the longest possible distance between any pair of vertices. The distance itself is measured by the number of edges on the unique simple path connecting them.
$$$^{\text{†}}$$$A simple path is a path between two vertices in a tree that does not visit any vertex more than once. It can be shown that the simple path between any two vertices is always unique.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains one integer $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$) — the number of the vertices in the tree.
The following $$$n-1$$$ lines of each test case describe the tree. Each of the lines contains two integers $$$u$$$ and $$$v$$$ ($$$1 \le u, v \le n$$$, $$$u \neq v$$$) that indicate an edge between vertex $$$u$$$ and $$$v$$$. It is guaranteed that these edges form a tree.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output one integer — the minimum number of operations to minimize the diameter.