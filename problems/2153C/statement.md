# Problem Description


You are given $$$n$$$ sticks, where the $$$i$$$-th stick has a length of $$$a_i$$$. You want to choose a non-empty subset of these sticks and use them as the sides of a polygon. Each selected stick must be used entirely as a single side of the polygon. It isnotallowed for two or more sticks to be joined end-to-end in parallel to form a longer side.
Your goal is to form a polygon that is symmetrical, strictly convex, and non-degenerate:
Among all such polygons that you can form with the sticks, find the maximum possible perimeter$$$^{\text{∗}}$$$. If no valid polygon exists, output $$$0$$$.
$$$^{\text{∗}}$$$Theperimeterof a polygon is equal to the sum of the lengths of its sides.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$3\le n\le 2\cdot 10^5$$$) — the number of sticks.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1\le a_i\le 10^9$$$) — the lengths of the sticks.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2\cdot 10^5$$$.

## Output
For each test case, output a single integer representing the maximum possible perimeter of a non-degenerate, symmetrical and strictly convex polygon that you can form from a non-empty subset of the sticks. If it is not possible, output $$$0$$$.