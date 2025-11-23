# Problem Description

You are given a positive integer $$$n$$$. In one operation, you can add to $$$n$$$ any positive integer whose decimal representation contains only the digit $$$9$$$, possibly repeated several times.
What is the minimum number of operations needed to make the number $$$n$$$ contain at least one digit $$$7$$$ in its decimal representation?
For example, if $$$n = 80$$$, it is sufficient to perform one operation: you can add $$$99$$$ to $$$n$$$, after the operation $$$n = 179$$$, which contains the digit $$$7$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The only line of each test case contains an integer $$$n$$$ ($$$10 \leq n \leq 10^9$$$).

## Output
For each test case, output the minimum number of operations required for the number $$$n$$$ to contain the digit $$$7$$$.