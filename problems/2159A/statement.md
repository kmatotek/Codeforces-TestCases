# Problem Description


This is an interactive problem.
There is a secret sequence $$$a_1, a_2, \ldots, a_{2n-1},a_{2n}$$$, which contains each integer from $$$1$$$ to $$$n$$$exactly twice.
Your task is to guess the sequence by using queries of the following type:
We define the $$$\operatorname{MAD}$$$ (Maximum Appearing Duplicate) of an integer sequence as the largest integer that appears at least twice. Specifically, if there is no number that appears at least twice, the $$$\operatorname{MAD}$$$ value is $$$0$$$. Some examples are as follows:
Please identify the secret sequenceusing at most $$$3n$$$ queries.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 3000$$$). The description of the test cases follows.
The first line of each test case contains one integer $$$n$$$ ($$$2 \le n \le 300$$$).
It is guaranteed that the sum of $$$n^2$$$ over all test cases does not exceed $$$10^5$$$.
After you read this line of input, the interaction begins with your first query.
