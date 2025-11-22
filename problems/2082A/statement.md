# Problem Description

A matrix is called binary if all its elements are either $$$0$$$ or $$$1$$$.
Ecrade calls a binary matrix $$$A$$$goodif the following two properties hold:
Ecrade has a binary matrix of size $$$n \cdot m$$$. He is interested in the minimum number of elements that need to be changed for the matrix to becomegood.
However, it seems a little difficult, so please help him!

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 400$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n, m$$$ ($$$1 \le n, m \le 100$$$).
This is followed by $$$n$$$ lines, each containing exactly $$$m$$$ characters consisting only of $$$0$$$ and $$$1$$$, describing the elements of Ecrade's matrix.
It is guaranteed that the sum of $$$n \cdot m$$$ across all test cases does not exceed $$$5 \cdot 10^4$$$.

## Output
For each test case, output a single integer, the minimum number of elements that need to be changed.