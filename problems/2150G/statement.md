# Problem Description

You are given three positive integers $$$x$$$, $$$y$$$, and $$$k$$$.
You are also given a binary string$$$^{\text{∗}}$$$ $$$a$$$ ($$$|a| = x + y$$$).
Count the number of binary strings $$$b$$$, modulo $$$998\,244\,353$$$, such that:
$$$^{\text{∗}}$$$A binary string is a string that only consists of characters $$$\mathtt{0}$$$ and $$$\mathtt{1}$$$.
$$$^{\text{†}}$$$A sequence $$$a$$$ is a subsequence of a sequence $$$b$$$ if $$$a$$$ can be obtained from $$$b$$$ by the deletion of several (possibly, zero or all) elements. For example, subsequences of $$$\mathtt{1011101}$$$ are $$$\mathtt{0}$$$, $$$\mathtt{1}$$$, $$$\mathtt{11111}$$$, $$$\mathtt{0111}$$$, but not $$$\mathtt{000}$$$ nor $$$\mathtt{11100}$$$.
$$$^{\text{‡}}$$$A string $$$p$$$ is lexicographically larger than another string $$$q$$$ if and only if one of the following holds:

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 5000$$$). The description of the test cases follows.
The first line of each test case contains three integers $$$x$$$, $$$y$$$, and $$$k$$$ ($$$1 \le x, y \le 5000$$$, $$$1 \leq k < x + y$$$).
The second line of each test case contains a binary string $$$a$$$ ($$$|a| = x+y$$$) consisting of characters $$$\mathtt{0}$$$ and $$$\mathtt{1}$$$.
It is guaranteed that neither the sum of $$$x$$$ nor the sum of $$$y$$$ over all test cases exceeds $$$5000$$$.

## Output
For each test case, output an integer on a new line, the number of binary strings that satisfy the conditions modulo $$$998\,244\,353$$$.