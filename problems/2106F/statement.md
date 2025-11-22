# Problem Description

Dr. TC has a new patient called Goblin. He wants to test Goblin's intelligence, but he has gotten bored of his standard test. So, he decided to make it a bit harder.
First, he creates a binary string$$$^{\text{∗}}$$$ $$$s$$$ having $$$n$$$ characters. Then, he creates $$$n$$$ binary strings $$$a_1, a_2, \ldots, a_n$$$. It is known that $$$a_i$$$ is created by first copying $$$s$$$, then flipping the $$$i$$$-th character ($$$\texttt{1}$$$ becomes $$$\texttt{0}$$$ and vice versa). After creating all $$$n$$$ strings, he arranges them into an $$$n \times n$$$ grid $$$g$$$ where $$$g_{i, j} = a_{i_j}$$$.
A set $$$S$$$ of size $$$k$$$ containing distinct integer pairs $$$\{(x_1, y_1), (x_2, y_2), \ldots, (x_k, y_k)\}$$$ is considered good if:
Goblin's task is to find the maximum possible size of a good set $$$S$$$. Because Dr. TC is generous, this time he gave him two seconds to find the answer instead of one. Goblin is not known for his honesty, so he has asked you to help him cheat.
$$$^{\text{∗}}$$$A binary string is a string that only consists of characters $$$\texttt{1}$$$ and $$$\texttt{0}$$$.

## Input
The first line of the input consists of a single integer $$$t$$$ $$$(1 \le t \le 10^3)$$$ — the number of test cases.
The first line of each test contains a single integer $$$n$$$ $$$(1 \le n \le 2 \cdot 10^5)$$$ — the length of the binary string $$$s$$$.
The second line of each test contains a single binary string $$$s$$$ of length $$$n$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output a single number, the maximum possible size of a good set of cells from the grid.