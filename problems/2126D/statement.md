# Problem Description

You are given $$$n$$$ casinos, numbered from $$$1$$$ to $$$n$$$. Each casino is described by three integers: $$$l_i$$$, $$$r_i$$$, and $$$real_i$$$ ($$$l_i \le real_i \le r_i$$$). You initially have $$$k$$$ coins.
You can play at casino $$$i$$$ only if the current number of coins $$$x$$$ satisfies $$$l_i \le x \le r_i$$$. After playing, your number of coins becomes $$$real_i$$$.
You can visit the casinos in any order and are not required to visit all of them. Each casino can be visited no more than once.
Your task is to find the maximum final number of coins you can obtain.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le n \le 10^5$$$, $$$0 \le k \le 10^9$$$) — the number of casinos and the initial number of coins.
This is followed by $$$n$$$ lines. In the $$$i$$$-th line, there are three integers $$$l_i$$$, $$$r_i$$$, $$$real_i$$$ ($$$0 \le l_i \le real_i \le r_i \le 10^9$$$) — the parameters of the $$$i$$$-th casino.
It is guaranteed that the sum of all $$$n$$$ across all test cases does not exceed $$$10^5$$$.

## Output
For each test case, output a single integer — the maximum number of coins you can obtain after optimally choosing the order of visiting the casinos.