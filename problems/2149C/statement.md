# Problem Description

You are given an array $$$a$$$ of length $$$n$$$ and a number $$$k$$$, where $$$0 \le k \le n$$$.
In one operation, you can choose any index $$$i$$$ ($$$1 \le i \le n$$$) and set $$$a_i$$$ to any integer value $$$x$$$ from the range $$$[0,n]$$$.
Find the minimum number of such operations required to satisfy the condition: $$$\operatorname{MEX}(a)$$$$$$^{\text{∗}}$$$$$$=k$$$
$$$^{\text{∗}}$$$The minimum excluded (MEX) of a set of numbers $$$a_1,a_2,\dots,a_n$$$ is the smallest non-negative integer $$$x$$$ that does not appear among the $$$a_i$$$.

## Input
Each test consists of several sets of input data.
The first line contains one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of sets of input data. The description of the sets of input data follows.
The first line of each set of input data contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le n \le 2 \cdot 10^5,\,\, 0 \le k \le n$$$) — the length of the array $$$a$$$ and the required $$$\operatorname{MEX}(a)$$$.
The second line contains $$$n$$$ integers $$$a_1,a_2,\dots,a_n$$$ ($$$0 \le a_i \le n$$$) — the elements of the array $$$a$$$.
It is guaranteed that the sum of the values of $$$n$$$ across all sets of input data does not exceed $$$2 \cdot 10^5$$$.

## Output
For each set of input data, output one integer — the minimum number of operations required to satisfy the condition $$$\operatorname{MEX}(a)=k$$$.