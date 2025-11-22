# Problem Description

There arenarrows drawn in a row on a strip of paper, numbered from1ton. Each arrow points either to the left or to the right. Initially, all arrows are painted blue.
In one operation, you can repaint abluearrow intored. For the first operation, you can choose any arrow. For each subsequent operation, you are only allowed to choose such an arrow that the arrow repainted on the previous operation points in its direction. That is, if the arrow repainted in the previous operation is a left arrow, then, for the current operation, you have to choose an arrow at a smaller index than the previous one. Similarly, if the previous arrow was a right arrow, the current one has to be at a greater index than it. Note that the arrows don't have to be adjacent.
Each arrow has an integer reward for repainting it into red (which can be negative, positive, or zero).
The final score is the sum of the rewards for the repainted arrows. What is the maximum score that can be achieved if you are allowed to perform any number of operations (including zero)?

## Input
The first line contains a single integert(1≤t≤104) — the number of test cases.
In the first line of each test case, there is a single integern(1≤n≤3⋅105) — the number of arrows.
In the second line, there is a string consisting ofncharacters '<' and/or '>' (ASCII codes 60 and 62, respectively).
In the third line, there arenintegersc1,c2,…,cn(−109≤ci≤109) — the reward for repainting each arrow.
An additional constraint on the input: the sum ofnover all test cases does not exceed3⋅105.

## Output
For each test case, print a single integer — the maximum score that can be achieved if you are allowed to perform any number of operations (including zero).