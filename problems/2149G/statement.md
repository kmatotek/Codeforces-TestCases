# Problem Description

In the ruthless world of Blue Lock,Buratsuta 3is a trio selected to overthrow the reigning champions and lead the Japan U-20 team to glory.Sae Itoshihas already secured his place as the first participant; the remaining two spots will be contested in the tough Side-B selection.
To test the strategic abilities of the candidates, Buratsuta has posed the following challenge:
You are given an array of $$$n$$$ integers called "performance records" and $$$q$$$ queries. Each query specifies a subarray $$$[l, r]$$$. In this subarray, find all record values that occurstrictly morethan $$$\lfloor\tfrac{r - l + 1}{3}\rfloor$$$ times.

## Input
Each test consists of several test cases.
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The following describes the test cases.
The first line of each test case contains two integers $$$n$$$ and $$$q$$$ $$$(1 \le n, q \le 2\cdot10^5)$$$ — the number of records and the number of queries.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ $$$(1 \le a_i \le 10^9)$$$ — the performance records.
Each of the following $$$q$$$ lines contains two integers $$$l$$$ and $$$r$$$ $$$(1 \le l \le r \le n)$$$ — the boundaries of the query.
It is guaranteed that the sum of $$$n$$$ and sum of $$$q$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each query, output in one line all record values (in sorted order) that occurstrictly morethan $$$\lfloor\tfrac{r - l + 1}{3}\rfloor$$$ times in the segment $$$[l, r]$$$. If there are no such values, output $$$-1$$$.