# Problem Description


Mani has locked Hamid in a $$$1 \times n$$$ grid. Initially, some cells of the grid contain walls and the rest are empty, and Hamid is in an empty cell.
In each day, the following events happen in order:
Here is an example of a possible sequence of actions when $$$n=6$$$:
Hamid isalwaysaware of where the walls are. He wants to minimize the number of days that he needs to escape the grid, while Mani wants to maximize it.
You have to determine the number of days Hamid needs to escape the grid if they both act optimally.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$x$$$ ($$$2 \leq n \leq 2 \cdot 10^5$$$, $$$1 \leq x \leq n$$$) — the size of the grid and the initial position of Hamid. He is at the $$$x$$$-th cell from left to right initially.
The second line contains a string $$$s$$$ of length $$$n$$$ ($$$s_i=\texttt{"#"}$$$ or $$$\texttt{"."}$$$) — the initial state of the grid. The $$$i$$$-th cell of the grid contains a wall if $$$s_i= \texttt{"#"}$$$, and it is empty if $$$s_i=\texttt{"."}$$$.
It is guaranteed that the $$$x$$$-th cell is empty, and there are at least two empty cells in the grid.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output a single integer — the number of days Hamid needs to escape the grid if they both act optimally.