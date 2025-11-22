# Problem Description

In a showmatch for a computer game,2nesports players are set to participate; the rating of thei-th player isai. The ratings of all players are distinct.
For each player, the most exciting match will be with the player whose rating is the closest to theirs. Formally, for thei-th player, thebest opponentis another playerjsuch that the absolute difference in their ratings|ai−aj|is minimized among all ways to choose playerj. Note that some player can have more than one best opponent.
For example, if there are4esports players with ratings[3,7,5,12], then:
The organizers of the showmatch want to pair the participants so that each player is in exactly one pair, and in each pair, the players are best opponents for each other. Determine whether such a pairing exists.

## Input
The first line contains a single integert(1≤t≤100) — the number of test cases.
Each test case consists of two lines:

## Output
For each test case, if it is possible to pair the participants such that in each pair the participants are best opponents for each other, outputYES. Otherwise, outputNO.