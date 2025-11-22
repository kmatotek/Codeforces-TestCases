# Problem Description


Maple wants to bake some cakes for Chocola and Vanilla.
One day, she discovers $$$n$$$ magical cake ovens. The $$$i$$$-th oven bakes $$$a_i$$$ cakes every second. The cakes remain in their respective ovens until they are collected.
At the end of each second, she may teleport to any oven (including the one she is currently at) and collect all the cakes that have accumulated in that oven up to that point.
Your task is to determine the maximum number of cakes Maple can collect in $$$m$$$ seconds.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 1000$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$1 \leq n \leq 10^5$$$, $$$1\leq m\leq 10^8$$$) — the number of magical ovens and the number of seconds during which Maple will collect cakes.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \leq a_i \le 10^5$$$) — the number of cakes the $$$i$$$-th oven bakes every second.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output a single integer representing the maximum number of cakes Maple can collect in $$$m$$$ seconds.