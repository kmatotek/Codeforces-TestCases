# Problem Description

Programmer Gleb frequently visits the IT Campus "NEIMARK" to participate in programming training sessions.
Not only is Gleb a programmer, but he is also a renowned rower, so he covers part of his journey from home to the campus by kayaking along a river. Assume that Gleb starts at point0and must reach points(i.e., travelsmeters along a straight line). To make the challenge tougher, Gleb has decided not to go outside the segment[0,s]. The dimensions of the kayak can be neglected.
Gleb is a strong programmer! Initially, his power isk. Gleb's power directly affects the movement of his kayak. If his current power isx, then with one paddle stroke the kayak movesxmeters in the current direction. Gleb can turn around and continue moving in the opposite direction, but such a maneuver is quite challenging, and after each turn, his power decreases by1. The power can never become0— if his current power is1, then even after turning it remains1. Moreover, Gleb cannot make two turns in a row — after each turn, he must move at least once before making another turn. Similarly, Gleb cannot make a turn immediately after the start — he must first perform a paddle stroke.
Gleb wants to reach pointsfrom point0without leaving the segment[0,s]and while preserving as much power as possible. Help him — given the valuesand his initial powerk, determine the maximum possible power he can have upon reaching points.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤100). The description of the test cases follows.
A single line of each test case contains two integerssandk(1≤s≤109,1≤k≤1000,k≤s).
It is guaranteed that the sum ofkover all test cases does not exceed2000.

## Output
For each test case, output the maximum possible power Gleb can have at the end of his journey.