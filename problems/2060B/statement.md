# Problem Description

Farmer John'sncows are playing a card game! Farmer John has a deck ofn⋅mcards numbered from0ton⋅m−1. He distributesmcards to each of hisncows.
Farmer John wants the game to be fair, so each cow should only be able to play1card per round. He decides to determine aturn order, determined by a permutation∗pof lengthn, such that thepi'th cow will be thei'th cow to place a card on top of the center pile in a round.
In other words, the following events happen in order in each round:
There is a catch. Initially, the center pile contains a card numbered−1. In order to place a card, the number of the card must be greater than the number of the card on top of the center pile. Then, the newly placed card becomes the top card of the center pile. If a cow cannot place any card in their deck, the game is considered to be lost.
Farmer John wonders: does there existpsuch that it is possible for all of his cows to empty their deck after playing allmrounds of the game? If so, output any validp. Otherwise, output−1.
∗A permutation of lengthncontains each integer from1tonexactly once

## Input
The first line contains an integert(1≤t≤400) — the number of test cases.
The first line of each test case contains two integersnandm(1≤n⋅m≤2000) — the number of cows and the number of cards each cow receives.
The followingnlines containmintegers each – the cards received by each cow. It is guaranteed all given numbers (across allnlines) are distinct and in the range from0ton⋅m−1, inclusive.
It is guaranteed the sum ofn⋅mover all test cases does not exceed2000.

## Output
For each test case, output the following on a new line: