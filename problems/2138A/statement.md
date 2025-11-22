# Problem Description

Chocola and Vanilla love cakes. Today, the manager of a cake shop gave them a total of2k+1cakes. The cakes were distributed evenly, so each of them initially received2kcakes.
However, Chocola and Vanilla now want to redistribute the cakes such that Chocola ends up with exactlyxcakes and Vanilla gets the remaining2k+1−xcakes.
In one step, they can perform exactly one of the following two operations:
Your task is to determine the minimum number of steps required to reach the target distribution and to output any valid sequence of operations achieving that minimum.
It can be proven that, under the given constraints, a valid solution always exists, and the minimum number of steps required is at most120.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤1000). The description of the test cases follows.
The first line of each test case contains two integerskandx(1≤k≤60,1≤x≤2k+1−1) — each person initially received2kcakes, andxis the number of cakes Chocola should have after redistribution.

## Output
For each test case, output a single integern(0≤n≤120) representing the minimum number of steps required for them to redistribute the cakes accordingly.
On the next line, outputnintegerso1,o2,…,on(oi=1oroi=2), whereoi=1means that in thei-th step, Chocola gave half of her cakes to Vanilla (operation 1), andoi=2means that Vanilla gave half of her cakes to Chocola (operation 2).