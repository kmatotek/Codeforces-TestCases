# Problem Description

You are given an integer array $$$a$$$ of size $$$n$$$.
You can perform the following operations any number of times (possibly, zero):
Let's say that an array isidealif both of the following conditions hold:
Let's say that an array isbeautifulif it can be transformed into an ideal array using the aforementioned operations, provided that you initially have no coins. If the array is already ideal, then it is also beautiful.
The given array is not necessarily beautiful or ideal. You can remove any elements from it (including removing the entire array or not removing anything at all). Your task is to calculate the minimum number of elements you have to remove (possibly, zero) from the array $$$a$$$ to make itbeautiful.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 4 \cdot 10^5$$$).
The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$2 \le a_i \le 10^9$$$).
Additional constraint on the input: the sum of $$$n$$$ over all test cases doesn't exceed $$$4 \cdot 10^5$$$.

## Output
For each test case, print a single integer — the minimum number of elements you have to remove (possibly, zero) from the array $$$a$$$ to make itbeautiful.