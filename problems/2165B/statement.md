# Problem Description


You are given a multiset $$$a$$$, which consists of $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$. You would like to generate a new multiset $$$s$$$ through the following procedure:
Please count the number of different multisets $$$s$$$ that can be generated through the procedure, modulo $$$998\,244\,353$$$.
Please note that the number of differentmultisetsis counted, which means that the order of elements does not matter. However, the count of each element does matter, i.e. $$$\{1,1,2\},\{1,2\},\{1,1,2,2\}$$$ are all considered different.
$$$^{\text{∗}}$$$The mode of a multiset is defined as the element which appears the most; if several elements are tied as the maximum, then all of them are considered modes.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 5000$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1\le n\le5000$$$) — the size of multiset $$$a$$$.
The second line of each test case contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$1\le a_i\le n$$$).
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$5000$$$.

## Output
For each test case, print one line containing a single integer — the number of different multisets you can obtain, modulo $$$998\,244\,353$$$.