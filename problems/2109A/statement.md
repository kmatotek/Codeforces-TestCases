# Problem Description

Something you may not know about Mouf is that he is a big fan of the Yu-Gi-Oh! card game. He loves to duel with anyone he meets. To gather all fans who love to play as well, he decided to organize a big Yu-Gi-Oh! tournament and invitednplayers.
Mouf arranged thenplayers in a line, numbered from1ton. They then heldn−1consecutive duels: for eachifrom1ton−1, playerifaced playeri+1, producing one winner and one loser per match. Afterward, each player reports a valueai(0≤ai≤1):
Since some may lie about their results (e.g., reporting a1instead of a0, or vice versa) to influence prize outcomes, Mouf will cancel the tournament if he can prove any report to be false.
Given the arraya, determine whether at least one player must be lying.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤100). The description of the test cases follows.
The first line of each test case contains one integern(2≤n≤100) — the number of players in the tournament.
The second line of each test case containsnintegersa1,a2,…,an(0≤ai≤1) — denoting the report of thei-th player.

## Output
For each test case, print"YES"(without quotes) if there is at least one liar among the players, and"NO"(without quotes) otherwise.
You can output the answer in any case (upper or lower). For example, the strings"yEs","yes","Yes", and"YES"will be recognized as positive responses.