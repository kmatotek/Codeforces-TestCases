# Problem Description

There is a strip divided into cells, numbered from $$$0$$$ to $$$m$$$ from left to right. You are controlling a chip that is initially in the cell $$$0$$$.
There is a trap in each cell; they are activated according to the following rules:
In one turn, you can either move from the current cell to the next or stay in place. Then all the traps for this turn are activated. If the chip is in a cell with an activated trap at the beginning of the turn, the game ends.
Your task is to calculate the minimum number of turns to reach the cell $$$m$$$, or report that it is impossible.If the chip reaches the cell $$$m$$$ and at the end of the same turn, a trap in the cell $$$m$$$ activates, it is not considered a valid way to reach the cell $$$m$$$.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 100$$$) — the number of test cases.
The first line of each test case contains two integers $$$n$$$ and $$$m$$$ ($$$1 \le n \le 10$$$; $$$1 \le m \le 10^{12}$$$).
The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$2 \le a_i \le 10$$$).
The third line contains $$$n$$$ integers $$$b_1, b_2, \dots, b_n$$$ ($$$0 \le b_i < a_i$$$).

## Output
For each test case, print a single integer — the minimum number of turns to reach cell $$$m$$$. If it is impossible, print-1.