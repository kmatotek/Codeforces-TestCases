# Problem Description

There is a robot on the coordinate line. Initially, the robot is located at the point $$$x$$$ ($$$x \ne 0$$$). The robot has a sequence of commands of length $$$n$$$ consisting of characters, whereLrepresents a move to the left by one unit (from point $$$p$$$ to point $$$(p-1)$$$) andRrepresents a move to the right by one unit (from point $$$p$$$ to point $$$(p+1)$$$).
The robot starts executing this sequence of commands (one command per second, in the order they are presented). However, whenever the robot reaches the point $$$0$$$, the counter of executed commands is reset (i. e. it starts executing the entire sequence of commands from the very beginning). If the robot has completed all commands and is not at $$$0$$$, it stops.
Your task is to calculate how many times the robot will enter the point $$$0$$$ during the next $$$k$$$ seconds.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first line of a test case contains three integers $$$n$$$, $$$x$$$ and $$$k$$$ ($$$1 \le n \le 2 \cdot 10^5$$$; $$$-n \le x \le n$$$; $$$n \le k \le 10^{18}$$$).
The second line of a test case contains a string $$$s$$$ consisting of $$$n$$$ charactersLand/orR.
Additional constraint on the input: the sum of $$$n$$$ over all test cases doesn't exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, print a single integer — the number of times the robot will enter the point $$$0$$$ during the next $$$k$$$ seconds.