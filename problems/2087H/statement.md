# Problem Description

Let's recall the rules of the game "Nim". The game is played by two players who take turns. They have a certain number of piles of stones (the piles can be of the same size or different sizes; the size is defined as the number of stones in a pile). On their turn, a player must choose any non-empty pile of stones and remove any number of stones from it (at least one). The player who cannot make a move loses.
In this problem, a modified version of the game will be used. There is a special set of numbersSthat prohibits certain moves. For each numbersiin this set, if the current size of the pile of stones isstrictly greaterthansi, it cannot be madestrictly lessthansiin one move. In other words, if the current size of the pile isx, and the player tries to make a move that results in a size ofy, andx>si>yfor some numbersi∈S, such a move is not allowed.
Your task is as follows. Initially, the setSis empty. You need to process queries of three types:

## Input
The first line contains a single integerq(1≤q≤3⋅105) — the number of queries.
Each query is given in one line in one of the following formats:

## Output
For each query of type2, outputFirstif the player making the first move will win, orSecondif they will lose.