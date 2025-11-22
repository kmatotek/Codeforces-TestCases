# Problem Description

Teto is playing the hit rhythm gameosu!. The game can be described by a binary string$$$^{\text{∗}}$$$ $$$s$$$ of length $$$n$$$ and a positive integer $$$k$$$ where the following will happen in order:
You dislike Teto (for some reason). So determine the minimum number of positions you need to protect to force her to leave $$$s$$$ unchanged.
$$$^{\text{∗}}$$$A binary string is a string that only consists of characters $$$\mathtt{0}$$$ and $$$\mathtt{1}$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 100$$$). The description of the test cases follows.
The first line of each testcase contains integers $$$n$$$ and $$$k$$$ ($$$2 \le n \le 1000$$$; $$$2 \le k \le n$$$) — the length of $$$s$$$ and $$$k$$$.
The second line of each test case contains a binary string $$$s$$$ of length $$$n$$$ consisting of characters $$$\mathtt{0}$$$ and $$$\mathtt{1}$$$.
The sum of $$$n$$$ across all testcases does not exceed $$$1000$$$.

## Output
For each testcase, output the minimum number of positions you need to protect to force Teto to leave the string unchanged.