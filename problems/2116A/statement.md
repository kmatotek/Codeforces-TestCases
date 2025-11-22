# Problem Description

Gellyfish and Flower are playing a game called "Duel".
Gellyfish has $$$a$$$ HP, while Flower has $$$b$$$ HP.
Each of them has a knight. Gellyfish's knight has $$$c$$$ HP, while Flower's knight has $$$d$$$ HP.
They will play a game in rounds until one of the players wins. For $$$k = 1, 2, \ldots$$$ in this order, they will perform the following actions:
As one of the smartest people in the world, you want to tell them who will win before the game. Assume both players play optimally.
It can be proven that the game will never end in a draw. That is, one player has a strategy to end the game in a finite number of moves.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first and only line of each test case contains four integers $$$a$$$, $$$b$$$, $$$c$$$, $$$d$$$ ($$$1 \leq a, b, c, d \leq 10^9$$$) — the HP of Gellyfish, the HP of Flower, the HP of Gellyfish's knight, and the HP of Flower's knight, respectively.

## Output
For each test case, if Flower will win, output "Flower", otherwise output "Gellyfish".