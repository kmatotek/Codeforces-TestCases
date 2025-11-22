# Problem Description

Consider the following game.
In this game, a level consists ofnpairs of gates. Each pair contains one left gate and one right gate. Each gate performs one of two operations:
The additional people gained from each operation can be assigned to either lane. However, people already in a lanecannotbe moved to the other lane.
Initially, there is one person in each lane. Your task is to determine the maximum total number of people that can be achieved by the end of the level.

## Input
The first line contains an integert(1≤t≤104) — the number of test cases.
The first line of each test case contains one integern(1≤n≤30) — the number of pairs of gates.
The nextnlines of each test case provide the information for the left gate followed by the right gate of each gate pair. The information for each gate is given in the form+a(1≤a≤1000) orxa(2≤a≤3) for some integera.

## Output
For each test case, output a single integer — the maximum total number of people at the end of the level.