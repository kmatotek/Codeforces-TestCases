# Problem Description


Ali and Bahamin decided to spend their summer vacation on the beautiful southern coasts of Iran. They also agreed to do some shopping during the trip — but instead of setting a fixed budget, they decided to determine how much they would spend by playing a game.
The game is played on two arrays $$$a$$$ and $$$b$$$, each containing $$$n$$$ integers.
The game will last for $$$k$$$ rounds. In one round:
After all the $$$k$$$ rounds, thevalueof the game is defined as $$$v=\sum\limits_{i=1}^{n} |a_i-b_i|$$$. Ali and Bahamin will spend exactly $$$v$$$ coins during their trip.
However, their goals are quite different:
You have to find the final amount of coins they will spend if both Ali and Bahamin play optimally.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$2 \leq n \leq 2 \cdot 10^5$$$, $$$1 \leq k \leq n$$$) — the length of $$$a$$$ and $$$b$$$, and the number of rounds.
The second line contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$1 \leq a_i \leq 10^9$$$) — the elements of $$$a$$$.
The third line contains $$$n$$$ integers $$$b_1,b_2,\ldots,b_n$$$ ($$$1 \leq b_i \leq 10^9$$$) — the elements of $$$b$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output a single integer — the final amount of coins they will spend if both Ali and Bahamin play optimally.