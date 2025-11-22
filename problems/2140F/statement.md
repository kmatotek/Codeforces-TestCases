# Problem Description


You are given an array $$$a$$$ of size $$$n$$$, and you can perform the following operation on the array $$$a$$$ any number of times (including zero):
Your task is to determine the minimum possible value of the sum of elements of the array $$$a$$$ that can be achieved after performing the operation any number of times or report that it can be decreased indefinitely.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each testcase contains a single integer $$$n$$$ ($$$1 \le n \le 10^6$$$) — the length of the array $$$a$$$.
The second line of each testcase contains $$$n$$$ integers $$$a_1,a_2,a_3,\ldots,a_n$$$ ($$$1 \le a_i \le 10^9$$$) — the elements of the array $$$a$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^6$$$.

## Output
For each testcase, print the minimum possible value of the sum of elements of the array $$$a$$$ that can be achieved after performing the above mentioned operation any number of times.
If the sum of elements of the array $$$a$$$ can be decreased indefinitely, print $$$-1$$$.