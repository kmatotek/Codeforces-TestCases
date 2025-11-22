# Problem Description

Given an integer $$$x$$$ and an integer $$$k$$$. In one operation, you can perform one of two actions:
Find the minimum number of operations required to make the number $$$x$$$ equal to $$$y$$$, or determine that it is impossible.

## Input
The first line of the input contains one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The only line of each test case contains three integers $$$x$$$, $$$y$$$ and $$$k$$$ ($$$1 \le x, y, k \le 10^6$$$).
It is guaranteed that the sum of $$$x$$$ and the sum of $$$y$$$ across all test cases does not exceed $$$10^8$$$.

## Output
For each test case, output $$$-1$$$ if it is impossible to achieve $$$x=y$$$ using the given operations, and the minimum number of required operations otherwise.