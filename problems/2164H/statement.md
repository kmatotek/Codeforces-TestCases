# Problem Description

We define thehumor valueof a string $$$t$$$ as the length of the longest palindrome string which occurs at least twice in it.
Formally, a string $$$p$$$ ishumor with respect to $$$t$$$, if and only if both of the following conditions are met:
Thehumor valueof $$$t$$$ is defined as the maximum length among allhumorstringswith respect to $$$t$$$.
You are given a string $$$s$$$ of length $$$n$$$ which only contains lowercase Latin letters and $$$q$$$ queries. Each query contains two integers $$$l_i$$$, $$$r_i$$$, and you need to find the humor value of the string $$$s[l_i, r_i]$$$.
Here, $$$a[l, r]$$$ is defined as the string $$$a_l,a_{l+1},\ldots,a_r$$$.

## Input
The first line contains two integers $$$n$$$, $$$q$$$ ($$$1\le n,q\le 5\cdot10^5$$$).
The second line contains a string $$$s$$$.
The next $$$q$$$ lines contain the description of queries. The $$$i$$$-th line contains two integers $$$l_i$$$, $$$r_i$$$ ($$$1\le l_i\le r_i\le n$$$).

## Output
On the $$$i$$$-th line, output the answer to the $$$i$$$-th query.