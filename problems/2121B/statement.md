# Problem Description

You are given a string $$$s$$$ of length $$$n$$$, consisting of lowercase letters of the Latin alphabet. Determine whether there exist threenon-emptystrings $$$a$$$, $$$b$$$, and $$$c$$$ such that:
$$$^{\text{∗}}$$$Concatenation of strings $$$a$$$ and $$$b$$$ is defined as the string $$$a + b = a_1a_2 \ldots a_pb_1b_2 \ldots b_q$$$, where $$$p$$$ and $$$q$$$ are the lengths of strings $$$a$$$ and $$$b$$$, respectively. For example, the concatenation of the strings "code" and "forces" is "codeforces".
$$$^{\text{†}}$$$A string $$$a$$$ is a substring of a string $$$b$$$ if $$$a$$$ can be obtained from $$$b$$$ by the deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

## Input
Each test consists of multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \leq t \leq 10^4$$$) — the number of test cases. The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$3 \leq n \leq 10^5$$$) — the length of the string $$$s$$$.
The second line of each test case contains the string $$$s$$$ of length $$$n$$$, consisting of lowercase letters of the Latin alphabet.
It is guaranteed that the sum of $$$n$$$ across all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output "Yes" if there exist three non-empty strings $$$a$$$, $$$b$$$, and $$$c$$$ that satisfy the conditions, and "No" otherwise.
You may output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive answers.