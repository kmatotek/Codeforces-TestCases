# Problem Description

Alice and Bob are playing a game. They have $$$n$$$ cards numbered from $$$1$$$ to $$$n$$$. At the beginning of the game, some of these cards are given to Alice, and the rest are given to Bob.
Card with number $$$i$$$ beats card with number $$$j$$$ if and only if $$$i > j$$$,with one exception: card $$$1$$$ beats card $$$n$$$.
The game continues as long as each player has at least one card. During each turn, the following occurs:
A player can use a card that they have taken during one of the previous turns.
The player who has no cards at the beginning of a turn loses. Determine who will win if both players play optimally.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 5000$$$) — the number of test cases.
Each test case consists of two lines:
Additional constraint on the input: in each test case, at least one card is initially given to Alice, and at least one card is initially given to Bob.

## Output
For each test case, outputAliceif Alice wins with optimal play, orBobif Bob wins. It can be shown that if both players play optimally, the game will definitely end in a finite number of turns with one of the players winning.