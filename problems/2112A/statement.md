# Problem Description

Alice and Bob participate in a game TV show. When the game starts, the prize will be dropped to a certain point, and whoever gets to it first will get the prize.
Alice decided that she would start running from pointa. Bob, however, has not yet chosen his starting position.
Bob knows that the prize could drop either at pointxor at pointy. He also knows that he can reach the prize faster than Alice if the distance from his starting position to the prize isstrictly lessthan the distance from Alice's starting position to the prize. The distance between any two pointscanddis calculated as|c−d|.
Your task is to determine whether Bob can choose an integer point that is guarantee to get to the prize faster, regardless of where it appears (at pointxory). Bob can choose any integer point, except fora(in particular, he can choose to start in pointx, pointy, or any other point, but nota).

## Input
The first line contains a single integert(1≤t≤1000) — the number of test cases.
The only line of each test case contains three integersa,x,y(1≤a,x,y≤100). Pointsa,x, andyare pairwise distinct.

## Output
For each test case, print "YES" (case insensitive) if Bob can choose an integer point that is guarantee to get to the prize faster, regardless of where it appears. Otherwise, print "NO" (case insensitive).