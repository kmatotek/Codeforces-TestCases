# Problem Description

You are given a grid $$$a$$$ of $$$2$$$ rows and $$$n$$$ columns, where every cell has value from $$$1$$$ to $$$2n$$$.
Let $$$f(l, r)$$$, where $$$1 \le l \le r \le 2n$$$, represent a binary$$$^{\text{∗}}$$$ grid $$$b$$$ of $$$2$$$ rows and $$$n$$$ columns, such that $$$b_{i, j} = 1$$$ if and only if $$$l \le a_{i, j} \le r$$$. Note that cell $$$(i, j)$$$ denotes the cell $$$i$$$ rows from the top and $$$j$$$ columns from the left.
Count the number of pairs of integers $$$(l, r)$$$ such that $$$1 \le l \le r \le 2n$$$, and in $$$f(l, r)$$$ there exists adown-rightpath of adjacent cells$$$^{\text{†}}$$$ with value of $$$1$$$ from cell $$$(1, 1)$$$ to $$$(2, n)$$$.
$$$^{\text{∗}}$$$A grid is considered binary if and only if every cell of it has value of $$$\mathtt{0}$$$ or $$$\mathtt{1}$$$.
$$$^{\text{†}}$$$A down-right path of adjacent cells is a sequence of cells such that each cell in the sequence shares either its top side or its left side with a side of the previous cell in the sequence.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$) — the number of columns in the grid.
The second line contains exactly $$$n$$$ integers $$$a_{1, 1}$$$, $$$a_{1, 2}$$$, ..., $$$a_{1, n}$$$ ($$$1 \le a_{1, i} \le 2n$$$) — the values of the cells of the first row of the grid.
The third line contains exactly $$$n$$$ integers $$$a_{2, 1}$$$, $$$a_{2, 2}$$$, ..., $$$a_{2, n}$$$ ($$$1 \le a_{2, i} \le 2n$$$) — the values of the cells of the second row of the grid.
It is guaranteed that the sum of $$$n$$$ across all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For every test case, output on a separate line a single integer representing the number of pairs of integers $$$(l, r)$$$ such that $$$1 \le l \le r \le 2n$$$, and in $$$f(l, r)$$$ there exists a down-right path of adjacent cells with value of $$$1$$$ from cell $$$(1, 1)$$$ to $$$(2, n)$$$.