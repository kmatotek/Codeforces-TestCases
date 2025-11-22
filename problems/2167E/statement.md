# Problem Description

khba has $$$n$$$ friends, each standing on a line at position $$$a_i$$$, and each of them is in the range $$$[0, x]$$$.
They all want to come to him. One of his friends, Isamatdin, gave him $$$k$$$ teleports. Each friend will walk to the nearest teleport (choosing the shortest distance). Once a friend reaches a teleport, khba and the friend can instantly meet.
But khba is so tired that he'll be sleeping while his friends are walking toward him. Now he wants to choose $$$k$$$ teleport positions so that their positions are distinct and lie within the range $$$[0, x]$$$, in order to maximize the time it takes for the first friend who reaches a teleport to reach it. Assume that friends move at the same speed.
Since khba isn't good at calculations, you should output the $$$k$$$ chosen teleport positions.

## Input
Each test contains multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \leq t \leq 10^4$$$) — the number of test cases. The description of the test cases follows.
The first line of each test case contains three integers $$$n$$$, $$$k$$$, and $$$x$$$ ($$$1 \leq n, k \leq 2 \cdot 10^5$$$, $$$k - 1 \leq x \leq 10^9$$$) — the number of friends, the number of teleports, and the range of possible positions for the teleports.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$0 \leq a_i \leq x$$$) — the positions of khba's friends.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.
It is guaranteed that the sum of $$$k$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output a single line containing $$$k$$$ integers — the $$$k$$$ chosen teleport positions. The positions must be distinct and lie within the range $$$[0, x]$$$. The positions may be output in any order.
If there are multiple optimal choices, output any of them.