# Problem Description

Initially, the integers from $$$0$$$ to $$$n-1$$$ are written on a blackboard.
In one round,
Rounds take place in succession until a player is unable to make a move — the first player who is unable to make a move loses. Determine who wins with optimal play.
$$$^{\text{∗}}$$$We define that $$$x\equiv y\pmod m$$$ whenever $$$x-y$$$ is an integer multiple of $$$m$$$.

## Input
The first line contains an integer $$$t$$$ ($$$1 \leq t \leq 100$$$)  — the number of test cases.
The only line of each test case contains an integer $$$n$$$ ($$$1\leq n \leq 100$$$) — the number of integers written on the blackboard.

## Output
For each test case, output on a single line "Alice" if Alice wins with optimal play, and "Bob" if Bob wins with optimal play.
You can output the answer in any case (upper or lower). For example, the strings "aLiCe", "alice", "ALICE", and "alICE" will be recognized as "Alice".