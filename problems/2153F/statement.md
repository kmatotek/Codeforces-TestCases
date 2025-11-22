# Problem Description


An array $$$b$$$ of length $$$m$$$ iscuteif there do not exist four indices $$$1\le i < j < k < l \le m$$$ such that $$$b_i\neq b_j$$$, $$$b_i = b_k$$$ and $$$b_j = b_l$$$.
Thebeautyof an array $$$b$$$ of length $$$m$$$ is defined as the sum of all distinct values that appear an odd number of times in array $$$b$$$. Formally, let $$$\operatorname{cnt}(b, x)$$$ denote the number of times the value $$$x$$$ appears in array $$$b$$$. Then, the beauty is given by $$$$$$\sum\limits_{\substack{x\in \mathbb{Z}\\\operatorname{cnt}(b, x)\text{ is odd}}}x.$$$$$$
You are given a cute array $$$a$$$ of length $$$n$$$, and you need to answer $$$q$$$ queries online. Each query consists of two integers $$$l$$$ and $$$r$$$ ($$$1\le l\le r\le n$$$), and you must compute the beauty of the subarray $$$a_{l\ldots r}$$$$$$^{\text{∗}}$$$. Note that the queries are encoded; each subsequent query can only be decoded after calculating the answer to the preceding query.
$$$^{\text{∗}}$$$The subarray $$$a_{l \ldots r}$$$ refers to the contiguous segment of the array $$$a$$$ that starts at index $$$l$$$ and ends at index $$$r$$$, i.e., $$$[a_l, a_{l+1}, \ldots, a_r]$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$q$$$ ($$$1\le n, q\le 5\cdot 10^5$$$) — the length of array $$$a$$$ and the number of queries.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1\le a_i\le n$$$) — the elements of the cute array $$$a$$$.
The $$$i$$$-th of the next $$$q$$$ lines contains two integers $$$x'_i$$$ and $$$y'_i$$$ ($$$1\le x'_i, y'_i\le n$$$) — the endpoints of the queried subarray in an encoded form.
Let $$$\text{ans}_i$$$ be the answer to the $$$i$$$-th query, with $$$\text{ans}_0 = 0$$$. Then, we calculate $$$x_i = ((x'_i - 1 + \text{ans}_{i - 1}) \bmod n) + 1$$$ and $$$y_i = ((y'_i - 1 + \text{ans}_{i - 1}) \bmod n) + 1$$$. The endpoints of the $$$i$$$-th queried subarray, $$$l_i$$$ and $$$r_i$$$, are decoded as $$$l_i = \min(x_i, y_i)$$$ and $$$r_i = \max(x_i, y_i)$$$.
It is guaranteed that the given array $$$a$$$ satisfies the conditions of a cute array.
It is guaranteed that the sum of $$$n$$$ and the sum of $$$q$$$ over all test cases does not exceed $$$5\cdot 10^5$$$.

## Output
For each test case, output $$$q$$$ integers representing the answers to each query.