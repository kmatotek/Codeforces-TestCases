# Problem Description

Alice and Bob have a bag with $$$n$$$ marbles, with the integer $$$v_i$$$ written on the $$$i$$$-th marble. They play the following game: first, each player chooses an integer (let's denote the integer chosen by Alice as $$$a$$$, and the integer chosen by Bob as $$$b$$$). After that, they start drawing marbles from the bag in any order until the bag is empty. For each ball, the point goes to the one whose chosen integer is closer to the integer on the marble;in case of a tie, Alice gets the point.
For example, if $$$a = 10$$$, $$$b = 30$$$, then
Bob has managed to find out in advance which integer Alice will choose. Help him to choose his integer in such a way as to maximize the number of points he receives.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
Each test case consists of two lines:
Additional constraint on the input: the sum of $$$n$$$ across all test cases does not exceed $$$3 \cdot 10^5$$$.

## Output
For each test case, output a single integer $$$b$$$ ($$$0 \le b \le 2 \cdot 10^9$$$) that Bob should choose to maximize the number of points he receives. If there are multiple such numbers, you may output any of them.