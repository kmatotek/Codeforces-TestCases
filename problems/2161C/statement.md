# Problem Description

You are a customer in a store and want to buy $$$n$$$ items. Each item $$$i$$$ has a price $$$a_i$$$ such that $$$1 \leq a_i \leq X$$$, where $$$X$$$ is aloyalty factor.
Yourloyalty levelin the store is defined as $$$\lfloor {S \over X} \rfloor$$$, where $$$S$$$ is the total cost of items purchased so far. Initially, $$$S = 0$$$.
If you buy an item with price $$$p$$$ and your loyalty level increases as a result of this purchase, you earn $$$p$$$ bonus points.
Your task is to find themaximum number of bonus pointsyou can earn by choosing an optimal order of purchase for the items.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 2 \cdot 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ ($$$1 \leq n \leq 10^5$$$) and $$$X$$$ ($$$1 \leq X \leq 10^9$$$) — the number of items and the loyalty factor.
The second line of each test case contains $$$n$$$ integers $$$a_1$$$, $$$a_2$$$, $$$\ldots$$$, $$$a_n$$$ ($$$1 \leq a_i \leq X$$$) — the prices of the items.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^5$$$.

## Output
For each test case, output two lines.
The first line should contain a single integer — the maximum number of bonus points that can be earned.
The second line should contain $$$n$$$ integers — the prices of the items in an order of purchase that maximizes the number of bonus points.
If there are several orders that maximize the number of bonus points, you can output any of them.