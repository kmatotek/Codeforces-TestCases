# Problem Description

You are given an arrayaof lengthnand anevenintegerk(2≤k≤n). You need to split the arrayainto exactlyknon-empty subarrays†such that each element of the arrayabelongs to exactly one subarray.
Next, all subarrays with even indices (second, fourth,…,k-th) are concatenated into a single arrayb. After that,0isaddedto the end of the arrayb.
Thecostof the arraybis defined as the minimum indexisuch thatbi≠i. For example, the cost of the arrayb=[1,2,4,5,0]is3, sinceb1=1,b2=2, andb3≠3. Determinethe minimumcost of the arraybthat can be obtained with an optimal partitioning of the arrayainto subarrays.
†An arrayxis a subarray of an arrayyifxcan be obtained fromyby the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

## Input
Each test consists of multiple test cases. The first line contains a single integert(1≤t≤104) — the number of test cases. The description of the test cases follows.
The first line of each test case contains two integersnandk(2≤k≤n≤2⋅105,kis even) — the length of the arrayaand the number of subarrays.
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤109) — the elements of the arraya.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output a single integer — the minimum cost of the arraybthat can be obtained.