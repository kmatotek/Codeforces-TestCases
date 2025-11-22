# Problem Description

Nezuko suddenly woke up on the number line at point $$$0$$$ and has $$$h$$$ health points. She wants to reach point $$$d$$$. In one turn, she can doexactly oneof two things:
Each movement decreases Nezuko's health; if the movement is the $$$j$$$-th consecutive movement, her health will decrease by $$$j$$$ points. If as a result of a move Nezuko's health drops to $$$0$$$ or below, she cannot make that move.
For example, if Nezuko initially had $$$7$$$ health points and $$$d=4$$$, her moves could look like this:
Find the minimum number of turns required for her to reach point $$$d$$$.

## Input
Each test consists of several test cases.
The first line contains one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases. The following describes the test cases.
The first line of each test case contains two integers $$$h$$$ and $$$d$$$ $$$(1\le h,d \le 10^9)$$$ — the number of health points and the destination point, respectively.

## Output
For each test case, output one number — the minimum number of turns required for Nezuko to reach point $$$d$$$.