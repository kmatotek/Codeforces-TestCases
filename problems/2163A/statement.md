# Problem Description

Two players, Souvlaki and Kalamaki, are given a sequence $$$a$$$ of $$$n$$$ integers.
They will play a game that consists of $$$n-1$$$ rounds, which are numbered from $$$1$$$ to $$$n-1$$$. Souvlaki plays on odd-numbered rounds, and Kalamaki on even-numbered rounds.
On the $$$i$$$-th round, a player can choose to take exactlyoneof the following actions:
Souvlaki wins if after the end of the last round, $$$a$$$ is sorted innon-decreasingorder. In other words, he wins if $$$a_i \le a_{i+1}$$$ holds for every $$$1 \le i < n$$$. Otherwise, Kalamaki wins.
However, Souvlaki does not like losing, sobeforethe start of the game, he may re-order the elements of $$$a$$$ in anyway he wants. Is it possible for him to do so such that he has a guaranteed winning strategy?

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 100$$$). The description of the test cases follows.
The first line of each test case contains a single integer, $$$n$$$ ($$$3 \le n \le 100$$$) — the number of integers in $$$a$$$.
The second line contains exactly $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \le a_i \le n$$$) — where $$$a_i$$$ represents the $$$i$$$-th element of $$$a$$$.

## Output
For each test case, output on a separate line "'YES"' if it is possible for Souvlaki to re-order the elements of $$$a$$$ such that he has a guaranteed winning strategy, and "'NO"' otherwise.
You can output the answer in any case (upper or lower). For example, the strings "'yEs"', "'yes"', "'Yes"', and "'YES"' will be recognized as positive responses.