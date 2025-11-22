# Problem Description

This problem differs from problem B. In this problem, you must output themaximumsum of prefix minimums over all operations that cost at least $$$x$$$ for each integer $$$x$$$ from $$$0$$$ to $$$n-1$$$.
You are given an array $$$a$$$ of length $$$n$$$, with elements satisfying $$$\boldsymbol{0 \le a_i \le n}$$$. You can perform the following operationat most once:
Let thecostof one operation be the value of $$$j-i$$$. The cost of not performing an operation is $$$0$$$.
For each integer $$$x$$$ from $$$0$$$ to $$$n-1$$$ inclusive, output themaximumpossible value of $$$\min(a_1) + \min(a_1,a_2) + \ldots + \min(a_1, a_2, \ldots, a_n)$$$ over all possible operations that have a cost ofat least$$$x$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains an integer $$$n$$$ ($$$2 \leq n \leq 10^6$$$) — the length of $$$a$$$.
The following line contains $$$n$$$ space-separated integers $$$a_1, a_2, \ldots, a_n$$$ ($$$0 \le a_i \le n$$$) — denoting the array $$$a$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^6$$$.

## Output
For each test case, output $$$n$$$ integers on a new line: the $$$i$$$-th integer denoting the maximum answer over all operations that have a cost of at least $$$i-1$$$.