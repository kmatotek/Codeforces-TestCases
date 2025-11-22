# Problem Description


Behruzbek receiveda tree$$$^{\text{∗}}$$$ with $$$n$$$ nodes. For a chosenroot$$$^{\text{†}}$$$ $$$r$$$, Behruzbek wants to findcutenessof the tree.
Consider every set of $$$k$$$ distinct nodes of the tree. For each such set, compute itslowest common ancestor(LCA) in the tree when it is rooted at $$$r$$$. Let $$$S_r$$$ be the set of all distinct nodes obtained this way; thencutenessof the tree is $$$|S_r|$$$, where $$$|S|$$$ means the number of distinct elements.
After discovering thecutenessof trees, Behruzbek became interested in finding thekawaiinessof the tree!Kawaiinessis defined as:
$$$$$$ \sum_{r = 1}^{n} |S_r| = |S_1| + |S_2| + \dots + |S_n| $$$$$$
Unfortunately, Behruzbek is feeling sleepy now. Please help Behruzbek by finding thekawaiinessof the tree!
$$$^{\text{∗}}$$$A tree is a connected graph without cycles.
$$$^{\text{†}}$$$A rooted tree is a tree where one vertex is special and called the root.

## Input
The first line contains the number of test cases $$$t$$$ ($$$1 \leq t \leq 10^{4}$$$).
The first line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$2 \leq k \leq n \leq 2\cdot 10^{5}$$$) — the number of vertices in the tree and the number of distinct integers to be chosen.
The following $$$n-1$$$ lines of each test case describe the tree. Each of the lines contains two integers $$$u$$$ and $$$v$$$ ($$$1 \leq u,v \leq n$$$, $$$u \ne v$$$) that indicate an edge between vertex $$$u$$$ and $$$v$$$. It is guaranteed that these edges form a tree.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2\cdot 10^{5}$$$.

## Output
For each test case, output one integer — the value of $$$\sum\limits_{r=1}^n |S_r|$$$.