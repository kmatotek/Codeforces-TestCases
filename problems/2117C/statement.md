# Problem Description

Yousef has an array $$$a$$$ of size $$$n$$$. He wants to partition the array into one or more contiguous segments such that each element $$$a_i$$$ belongs to exactly one segment.
A partition is calledcoolif, for every segment $$$b_j$$$, all elements in $$$b_j$$$ also appear in $$$b_{j + 1}$$$ (if it exists). That is, every element in a segment must also be present in the segment following it.
For example, if $$$a = [1, 2, 2, 3, 1, 5]$$$, acoolpartition Yousef can make is $$$b_1 = [1, 2]$$$, $$$b_2 = [2, 3, 1, 5]$$$. This is acoolpartition because every element in $$$b_1$$$ (which are $$$1$$$ and $$$2$$$) also appears in $$$b_2$$$. In contrast, $$$b_1 = [1, 2, 2]$$$, $$$b_2 = [3, 1, 5]$$$ is not acoolpartition, since $$$2$$$ appears in $$$b_1$$$ but not in $$$b_2$$$.
Note that after partitioning the array, you donotchange the order of the segments. Also, note that if an element appears several times in some segment $$$b_j$$$, it only needs to appear at least once in $$$b_{j + 1}$$$.
Your task is to help Yousef by finding the maximum number of segments that make acoolpartition.

## Input
The first line of the input contains integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first line of each test case contains an integer $$$n$$$ ($$$1 \le n \le 2 \cdot 10^5$$$) — the size of the array.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le n$$$) — the elements of the array.
It is guaranteed that the sum of $$$n$$$ over all test cases doesn't exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, print one integer — the maximum number of segments that make acoolpartition.