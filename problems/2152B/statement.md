# Problem Description

Doran and the Krug are playing a game on a grid consisting of $$$(n + 1) \times (n + 1)$$$ cells whose coordinates are pairs of integers from $$$0$$$ to $$$n$$$, inclusive. The Krug's goal is not to becaughtby Doran for as long as possible, while Doran's goal is tocatchthe Krug as early as possible. We say Dorancaughtthe Krug if they stand on the same grid cell.
To play the game, the Krug and Doran take turns alternately, starting from the Krug:
The Krug'ssurvival timeis defined as the number of Doran's turns until Dorancatchesthe Krug for the given starting cells of the players. Assuming that both players play optimally, find the Krug'ssurvival timeor report that the Krug can survive for infinite turns.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
Each test case consists of a single line containing five integers $$$n$$$, $$$r_K$$$, $$$c_K$$$, $$$r_D$$$, and $$$c_D$$$ ($$$1 \le n \le 10^9$$$, $$$0 \le r_K, c_K, r_D, c_D \le n$$$, $$$(r_K, c_K) \ne (r_D, c_D)$$$) — $$$n$$$ is the size of the grid, $$$(r_K, c_K)$$$ represents the Krug's starting cell, and $$$(r_D, c_D)$$$ represents Doran's starting cell.

## Output
For each test case, output the Krug'ssurvival timewhen both players play optimally. If the Krug can survive for infinite turns, print $$$-1$$$.