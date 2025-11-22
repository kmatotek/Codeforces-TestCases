# Problem Description

You are the proud owner of an infinitely large grid of lightbulbs, represented by aCartesian coordinate system. Initially, all of the lightbulbs are turned off, except for one lightbulb, where you buried your proudest treasure.
In order to hide your treasure's position, you perform the following operation an arbitrary number of times (possibly zero):
In the end, there arenlightbulbs turned on at coordinates(x1,y1),(x2,y2),…,(xn,yn). Unfortunately, you have already forgotten where you buried your treasure, so now you have to figure out one possible position of the treasure. Good luck!

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤2⋅105) — the number of lightbulbs that are on.
Thei-th of the nextnlines contains two integersxiandyi(−108≤xi,yi≤108) — the coordinates of thei-th lightbulb. It is guaranteed that all coordinates are distinct.
Additional constraint: There exists at least one position(s,t)(−109≤s,t≤109), such that if the lightbulb at position(s,t)is initially turned on, then after performing an arbitrary number of operations (possibly zero), we will get the given configuration of lightbulbs.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output two integerssandt(−109≤s,t≤109) — one possible position of the buried treasure. If there are multiple solutions, print any of them.
For this problem, hacks are disabled.