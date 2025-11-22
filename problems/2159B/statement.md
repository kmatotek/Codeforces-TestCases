# Problem Description

You are given a binary grid$$$^{\text{∗}}$$$ $$$G$$$ of dimensions $$$n \times m$$$.
Let us define arectangleas a tuple $$$(u,d,l,r)$$$ that satisfies the following conditions:
Then, theareaof a rectangle $$$(u,d,l,r)$$$ is defined as $$$(d-u+1) \cdot (r-l+1)$$$.
For example, consider the following binary grid given below.
$$$$$$\begin{matrix} 1 & 0 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 \end{matrix}$$$$$$
Here, you may see two rectangles $$$(1,2,1,3)$$$ and $$$(1,3,3,5)$$$$$$^{\text{†}}$$$, each of which has area $$$6$$$ and $$$9$$$, respectively.
For each cell $$$(i,j)$$$, find theminimum areaof any rectangle $$$(u,d,l,r)$$$ such that $$$u \le i \le d$$$ and $$$l \le j \le r$$$.
$$$^{\text{∗}}$$$A binary grid is a grid where each cell contains $$$0$$$ or $$$1$$$. The cell on the $$$j$$$-th column of the $$$i$$$-th row is denoted as cell $$$(i,j)$$$.
$$$^{\text{†}}$$$Note that these are the only rectangles in the grid; for example, $$$(1,1,1,5)$$$ isnota rectangle as it does not satisfy $$$u<d$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$2 \le n,m$$$, $$$n\cdot m \le 250\,000$$$).
Each of the $$$n$$$ following lines contains a string of length $$$m$$$ denoting the $$$i$$$-th row of $$$G$$$ ($$$G_{i,j} \in \{0,1\}$$$).
It is guaranteed that the sum of $$$n\cdot m$$$ over all test cases does not exceed $$$250\,000$$$.

## Output
For each test case, output a grid of $$$n$$$ rows and $$$m$$$ columns. On the $$$j$$$-th column of the $$$i$$$-th row, you should output: