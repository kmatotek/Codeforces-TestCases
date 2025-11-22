# Problem Description

There are some coins arranged in a line, numbered from1from left to right. There are three types of coins: gold, silver, and bronze.
Two players play a game; players take turns, and the first player makes the first turn. In one turn, the player chooses one of the three types of coins, and then collects all coins of that type which are still not taken by the other player. The game continues until all the coins are collected. Both players play optimally, and each player wants to maximize the number of coins he/she gets.
Your task is to answerqindependent queries of the following form: how many coins can the first player collect if the game is played using only coins with indices fromltorinclusive.

## Input
The first line contains a strings(1≤|s|≤105), consisting of the charactersG,S, and/orB.Gmeans that the coin is gold.Smeans that the coin is silver.Bmeans that the coin is bronze.
The second line contains a single integerq(1≤q≤105) — the number of queries.
Thenqlines follow; each of them contains two integerslandr(1≤l≤r≤|s|).

## Output
For each query, print a single integer — the number of coins the first player can collect if the game is played using only coins with indices fromltorinclusive.