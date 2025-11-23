# Problem Description

For an array of integers $$$a_1, a_2, \dots, a_n$$$, we define itsequality characteristicas the array $$$b_2, b_3, \dots, b_{n-1}$$$, where $$$b_i = 1$$$ if the $$$i$$$-th element of the array $$$a$$$ is equal to both of its neighbors, and $$$b_i = 0$$$ if the $$$i$$$-th element of the array $$$a$$$ is not equal to at least one of its neighbors.
For example, for the array $$$[1, 2, 2, 2, 3, 3, 4, 4, 4, 4]$$$, the equality characteristic will be $$$[0, 1, 0, 0, 0, 0, 1, 1]$$$.
You are given the array $$$b_2, b_3, \dots, b_{n-1}$$$. Your task is to determine whether there exists such an array $$$a$$$ for which the given array is the equality characteristic.

## Input
The first line contains one integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases.
Each test case consists of two lines:

## Output
For each test case, outputYESif the array $$$a$$$ exists, orNOif such an array does not exist. Each letter can be printed in any case.