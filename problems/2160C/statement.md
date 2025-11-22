# Problem Description


Given apositiveinteger $$$x$$$, let $$$f(x)$$$ be the positive integer formed by reversing the binary representation of $$$x$$$ without leading zeroes. For example, if $$$x=12=1100_2$$$, then $$$f(x)=0011_2=3$$$.
You are given an integer $$$n$$$. Please determine if there exists a positive integer $$$x$$$ such that $$$x \oplus f(x) = n$$$$$$^{\text{∗}}$$$.
$$$^{\text{∗}}$$$Here, $$$\oplus$$$ denotes thebitwise XOR operation.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains an integer $$$n$$$ ($$$0 \leq n <2^{30}$$$).

## Output
For each test case, outputYESif there exists a positive integer $$$x$$$ such that $$$x \oplus f(x) = n$$$, andNOotherwise.
You can output the answer in any case. For example, the strings "yEs", "yes", and "Yes" are also recognized as positive responses.