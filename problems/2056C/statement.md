# Problem Description


For an integer sequencea=[a1,a2,…,an], we definef(a)as the length of the longest subsequence∗ofathat is a palindrome†.
Letg(a)represent the number of subsequences of lengthf(a)that are palindromes. In other words,g(a)counts the number of palindromic subsequences inathat have the maximum length.
Given an integern, your task is to find any sequenceaofnintegers that satisfies the following conditions:
It can be proven that such a sequence always exists under the given constraints.
∗A sequencexis a subsequence of a sequenceyifxcan be obtained fromyby the deletion of several (possibly, zero or all) element from arbitrary positions.
†A palindrome is a sequence that reads the same from left to right as from right to left. For example,[1,2,1,3,1,2,1],[5,5,5,5], and[4,3,3,4]are palindromes, while[1,2]and[2,3,3,3,3]are not.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤100). The description of the test cases follows.
The first line of each test case contains a single integern(6≤n≤100) — the length of the sequence.
Note that there arenoconstraints on the sum ofnover all test cases.

## Output
For each test case, outputnintegersa1,a2,…,an, representing an array that satisfies the conditions.
If there are multiple solutions, you may output any of them.