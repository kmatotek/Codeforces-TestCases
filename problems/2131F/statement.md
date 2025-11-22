# Problem Description


Yuri is given two binary strings $$$a$$$ and $$$b$$$, both of which are of length $$$n$$$. The two strings dynamically define an $$$n \times n$$$ grid. Let $$$(i, j)$$$ denote the cell in the $$$i$$$-th row and $$$j$$$-th column. The initial value of cell $$$(i, j)$$$ has the value of $$$a_i \oplus b_j$$$, where $$$\oplus$$$ denotes thebitwise XOR operation. .
Yuri's journey always starts at cell $$$(1, 1)$$$. From a cell $$$(i, j)$$$, she can only move down to $$$(i + 1, j)$$$ or right to $$$(i, j + 1)$$$. Her journey is possible if there exists a valid path such that all cells on the path, including $$$(1, 1)$$$, have a value of 0.
Before her departure, she can do the following operation for any number of times:
Let $$$f(x, y)$$$ denote the minimum required operations so that Yuri can make her journey to the cell $$$(x,y)$$$. You must determine thesumof $$$f(x, y)$$$ over all $$$1 \leq x, y \leq n$$$.
Note that each of these $$$n^2$$$ cases is independent, meaning you need to assume the grid is in its original state in each case (i.e., no actual operations are performed).

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains one integer $$$n$$$ ($$$1 \le n \le 2 \cdot 10^5$$$).
The second line of each test case contains a binary string $$$a$$$ ($$$|a| = n$$$, $$$a_i \in \{0, 1\}$$$).
The third line of each test case contains a binary string $$$b$$$ ($$$|b| = n$$$, $$$b_i \in \{0, 1\}$$$).
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output one integer — the sum of minimum operations over all possible cells.