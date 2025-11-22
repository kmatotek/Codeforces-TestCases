# Problem Description

Vadim wanted to understand the infinite sequence of digits that consists of the positive integers written consecutively from $$$1$$$ to infinity. That is, this sequence looks like $$$123456789101112131415 \ldots$$$
To avoid looking into infinity, Vadim cut this sequence at the $$$k$$$-th digit and discarded everything after it. Thus, exactly $$$k$$$ digits remained in the sequence. Help him find the sum of the digits in the remaining sequence.

## Input
Each test consists of several test cases. The first line contains a single integer $$$t$$$ $$$(1 \le t \le 2 \cdot 10^4)$$$ — the number of test cases. The following lines describe the test cases.
In a single line of each test case, there is an integer $$$k$$$ — the number of digits in the remaining sequence $$$(1 \le k \le 10^{15})$$$.

## Output
For each given $$$k$$$, output the sum of the digits in the sequence of length $$$k$$$.