# Problem Description

In 2077, a sport called hobby-droning is gaining popularity among robots.
You already have a drone, and you want to win. For this, your drone needs to fly through a course withnobstacles.
Thei-th obstacle is defined by two numbersli,ri. Let the height of your drone at thei-th obstacle behi. Then the drone passes through this obstacle ifli≤hi≤ri. Initially, the drone is on the ground, meaningh0=0.
The flight program for the drone is represented by an arrayd1,d2,…,dn, wherehi−hi−1=di, and0≤di≤1. This means that your drone either does not change height between obstacles or rises by1. You already have a flight program, but somediin it are unknown and marked as−1. Replace the unknowndiwith numbers0and1to create a flight program that passes through the entire obstacle course, or report that it is impossible.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
In the first line of each test case, an integern(1≤n≤2⋅105)is given — the size of the arrayd.
In the second line of each test case, there arenintegersd1,d2,…,dn(−1≤di≤1) — the elements of the arrayd.di=−1means that thisdiis unknown to you.
Next, there arenlines containing2integersli,ri(0≤li≤ri≤n) — descriptions of the obstacles.
It is guaranteed that the sum ofnacross all test cases does not exceed2⋅105.

## Output
For each test case, outputnintegersd1,d2,…,dn, if it is possible to correctly restore the arrayd, or−1if it is not possible.