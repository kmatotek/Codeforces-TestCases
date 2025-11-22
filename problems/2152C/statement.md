# Problem Description


Tired of supporting ranged carries, Keria is now creating a data structure problem about supporting range queries.
For an array $$$b = [b_1, b_2, \ldots, b_m]$$$ of length $$$m$$$ where $$$b_i=0$$$ or $$$b_i=1$$$, consider the followingtriple removaloperation:
We want to make the array $$$b$$$ empty using thetriple removaloperation. Hence, we define thetotal costof an array as the minimum possible sum of the costs oftriple removaloperations required to make the array empty. If it is impossible to make the array empty, the cost is defined to be $$$-1$$$.
Keria wants to test his data structure. For this, you must answer $$$q$$$ independent queries. Initially, you are given an array $$$a = [a_1, a_2, \ldots, a_n]$$$ of length $$$n$$$ where $$$a_i=0$$$ or $$$a_i=1$$$. For each query, you are given a range $$$1 \le l \le r \le n$$$ and must find the cost for the array $$$[a_l, a_{l+1}, \ldots, a_r]$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$q$$$ ($$$1 \le n, q \le 250\,000$$$) — the length of the array and the number of queries.
The next line contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$a_i = 0$$$ or $$$a_i=1$$$) — the elements of the array.
Then $$$q$$$ lines follow. The $$$i$$$-th of them contains two integers $$$l_i$$$ and $$$r_i$$$ ($$$1 \le l_i \le r_i \le n$$$) — the range of the subarray for the $$$i$$$-th query.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$250\,000$$$.
It is guaranteed that the sum of $$$q$$$ over all test cases does not exceed $$$250\,000$$$.

## Output
For each test case, output $$$q$$$ lines. The $$$i$$$-th line should contain a single integer representing the answer to the $$$i$$$-th query.