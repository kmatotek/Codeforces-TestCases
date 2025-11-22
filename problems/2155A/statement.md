# Problem Description

Juan and his friends are going to split themselves into $$$n$$$ teams and play a modified double-elimination football tournament, consisting of awinners'group and alosers'group. Initially, all teams belong to the winners' group.
In each round of the tournament, the following happens as long as one of the groups hasat least twoteams:
Note that in the above process, when a team loses a match in the winners' group, it drops down to the losers' group in the next round. That means, it is not considered for the pairing process in the current round's losers' group.
After multiple iterations of the aforementioned process, both groups end up with a single team each. When this happens, both teams face off against each other in a match and a victor emerges.
Determine how many matches were played in total. It can be proved that no matter how the teams are paired up and which ones win and lose, the answer remains the same.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 100$$$). The description of the test cases follows.
The only line of each test case contains one positive integer $$$n$$$ ($$$2 \le n \le 500$$$) — the number of teams.

## Output
For each test case, print the total number of matches played during the tournament.