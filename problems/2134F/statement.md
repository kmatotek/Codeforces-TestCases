# Problem Description


You are given four positive integersc0,c1,c2, andc3.
Letn=c0+c1+c2+c3. Consider an arrayaofnintegers withx(0≤x≤3) appearingcxtimes. For anydistinct permutation∗bof the arraya, define itsoddnessas†‡:
n−1∑i=1lowbit(bi⊕bi+1)
Your task is to count, for each integerkfrom0to2⋅(n−1)(inclusive), the number of distinct permutations ofawith an oddness equal tok.
Since the numbers might be too large, you are only required to find them modulo109+7.
∗A permutation of the array is an arrangement of its elements into any order. For example,[1,2,2]is a permutation of[2,2,1], but[1,1,2]is not. Two permutations are considered distinct if they differ in at least one position.
†⊕denotes thebitwise XOR operation.
‡lowbit(x)is the value of the lowest binary bit ofx, e.g.lowbit(12)=4,lowbit(8)=8. Specifically, we definelowbit(0)=0.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤50). The description of the test cases follows.
The first and the only line of each test case contains four positive integersc0,c1,c2, andc3(1≤c0,c1,c2,c3<800,4≤c0+c1+c2+c3≤800).
Letn=c0+c1+c2+c3. It is guaranteed that the sum ofnover all test cases does not exceed800.

## Output
For each test case, output2⋅(n−1)+1integers in one line — the number of distinct permutations ofawith an oddness equal to0,1,…,2⋅(n−1)respectively. Output the answers modulo109+7.