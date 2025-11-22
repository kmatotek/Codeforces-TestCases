# Problem Description


There arenapple trees arranged in a circle. Each tree bears exactly one apple, and the beauty of the apple on thei-th tree is given bybifor all1≤i≤n. You start in front of tree1.
At each tree, you may choose to either eat the apple or skip it. After making your choice, you move to the next tree: from treei, you move to treei+1for1≤i≤n−1, and from treen, you move back to tree1. This process continues indefinitely as you move through the trees in a cycle.
However, you have a special condition: you may only eat an apple if its beauty is strictly greater than the beauty of the last apple you ate. For example, ifb=[2,1,2,3]and you eat the apple on tree1(beauty2), you cannot eat the apples on trees2and3because their beauties are not greater than2. However, you may eat the apple on tree4sinceb4=3>2.
Note that you are allowed to skip an apple when you first encounter it, and you can choose to eat it later on a subsequent cycle.
Your task is to determine the maximum number of apples you can eat if you make optimal decisions on when to eat or skip each apple.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤500). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤100) — the number of apple trees.
The second line of each test case containsnintegersb1,b2,…,bn(1≤bi≤n) — the beauty of the apples on the trees.
Note that there are no constraints on the sum ofnover all test cases.

## Output
For each test case, output a single integer representing the maximum number of apples you can eat.