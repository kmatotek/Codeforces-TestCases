# Problem Description

Call an array $$$b$$$ of length $$$m$$$ aderangementif the following property holds:
For example,
You are given an array $$$a$$$ of length $$$n$$$. In one operation, you can delete an element from $$$a$$$. The order of the remaining elements is preserved after each deletion.
Output whether it is possible to perform some (possibly none) operations such that the remaining elements form aderangement. If it is possible, output any possible remaining array. The remaining array must be non-empty.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 100$$$). The description of the test cases follows.
The first line of each test case contains an integer $$$n$$$ ($$$1 \leq n \leq 100$$$) — the length of array $$$a$$$.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \leq a_i \leq n$$$) — denoting the array $$$a$$$.

## Output
For each test case, on a new line, if it is possible to perform operations such that the remaining array is aderangement, outputYES. Otherwise, outputNO.
You can output in any case (upper or lower). For example, the strings"yEs","yes","Yes", and"YES"will be recognized as positive responses.
If your response was positive, output two more lines in the following format: