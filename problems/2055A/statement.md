# Problem Description

There arenlilypads arranged in a row, numbered from1tonfrom left to right. Alice and Bob are frogs initially positioned on distinct lilypads,aandb, respectively. They take turns jumping, starting with Alice.
During a frog's turn, it can jump either one space to the left or one space to the right, as long as the destination lilypad exists. For example, on Alice's first turn, she can jump to either lilypada−1ora+1, provided these lilypads are within bounds. It is important to note that each frogmust jumpduring its turn and cannot remain on the same lilypad.
However, there are some restrictions:
Determine whether Alice can guarantee a win, assuming that both players play optimally. It can be proven that the game will end after a finite number of moves if both players play optimally.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤500). The description of the test cases follows.
The first and only line of each test case contains three integersn,a, andb(2≤n≤100,1≤a,b≤n,a≠b) — the number of lilypads, and the starting positions of Alice and Bob, respectively.
Note that there arenoconstraints on the sum ofnover all test cases.

## Output
For each test case, print a single line containing either "YES" or "NO", representing whether or not Alice has a winning strategy.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.