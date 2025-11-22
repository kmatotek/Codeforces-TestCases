# Problem Description


You are given an arrayaconsisting ofn≥4non-negative integers.
You need to perform the following operation onauntil its length becomes1:
Serval wants the final element inato be0. Help him!
More formally, you have to find a sequence of operations, such that after performing these operations in order, the length ofabecomes1, and the final element inais0.
It can be shown that at least one valid operation sequence exists under the constraints of the problem, and the length of any valid operation sequence does not exceedn.
Note that you donotneed to minimize the number of operations.
∗The minimum excluded (MEX) of a collection of integersb1,b2,…,bkis defined as the smallest non-negative integerxwhich does not occur in the collectionb.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤1000). The description of the test cases follows.
The first line of each test case contains a single integern(4≤n≤5000) — the length of the arraya.
The second line containsnintegersa1,a2,…,an(0≤ai≤n) — the elements of the arraya.
It is guaranteed that the sum ofnover all test cases does not exceed5000.

## Output
For each test case, output a single integerk(0≤k≤n) in the first line of output — the length of the operation sequence.
Then, outputklines, thei-th line containing two integersliandri(1≤li<ri≤|a|) — the two indices you choose in thei-th operation, where|a|denotes the length of the array before this operation.
If there are multiple answers, you may print any of them.