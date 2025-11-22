# Problem Description


There is an arrayaconsisting ofnnon-negative integers and amagic numberk(k≥1,kis an integer). Serval has constructed another arraybof lengthn, wherebi=aimodkholds∗for all1≤i≤n. Then, heshuffledb.
You are given the two arraysaandb. Find a possiblemagic numberk. However, there is a small possibility that Serval fooled you, and such an integer does not exist. In this case, output−1.
It can be shown that, under the constraints of the problem, if such an integerkexists, then there exists a valid answer no more than109. And you need to guarantee thatk≤109in your output.
∗aimodkdenotes the remainder from dividingaibyk.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains an integern(1≤n≤104) — the length of the arraya.
The second line containsnintegersa1,a2,…,an(0≤ai≤106) — the elements of the arraya.
The third line containsnintegersb1,b2,…,bn(0≤bi≤106) — the elements of the arrayb.
It is guaranteed that the sum ofnover all test cases does not exceed104.

## Output
For each test case, output a single integerk(1≤k≤109) — themagic numberyou found. Print−1if it is impossible to find such an integer.
If there are multiple answers, you may print any of them.