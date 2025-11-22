# Problem Description

A popular reality showUnconventional Pairshas been launched in the city. According to the rules of the show, participants are paired in an unusual way: with an even number of people, all participants must be in pairs.
Petya has an array of $$$n$$$ integers $$$a_1,a_2,\dots ,a_n$$$. It is known that $$$n$$$ is even. Petya must divide the participants (numbers) into exactly $$$\large\frac{n}{2}$$$ pairs $$$(a_{p_1},a_{q_1}),\,(a_{p_2},a_{q_2}),\dots\,(a_{p_\frac{n}{2}},a_{q_\frac{n}{2}})$$$. Each index can be included in no more than one pair.
For a pair $$$(x,y)$$$, itsdifferenceis defined as $$$|x-y|$$$. Petya wants to formunconventional pairssuch that themaximumdifference among all pairs is minimized.
Determine the minimum possible value of this maximum difference.

## Input
Each test consists of several test cases.
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases. The description of the test cases follows.
The first line of each test case contains one even number $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$) — the length of the array $$$a$$$.
The second line contains $$$n$$$ integers $$$a_1,a_2,\dots ,a_n$$$ $$$(-10^{9} \le a_i \le 10^{9})$$$ — the elements of the array $$$a$$$.
It is guaranteed that the sum of the values of $$$n$$$ across all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output a single number — the minimum possible maximum difference between the elements in pairs.