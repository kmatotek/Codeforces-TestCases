# Problem Description

A permutation of integers from1tonis an array of sizenwhere each integer from1tonappears exactly once.
You are given a permutationpof integers from1ton. You have to processnqueries. During thei-th query, you replacepdiwith0. Each element is replaced with0exactly once. The changes made in the queries are saved, that is, after thei-th query, all integerspd1,pd2,…,pdiare zeroes.
After each query, you have to find the minimum number of operations required tofixthe array; in other words, to transform the current array into any permutation of integers from1ton(possibly into the original permutationp, possibly into some other permutation).
The operation you can perform to fix the array is the following one:
Note that the answer for each query is calculated independently, meaning you do not actually apply any operations, just calculate the minimum number of operations.

## Input
Each test consists of several test cases. The first line contains one integert(1≤t≤104) — the number of test cases. Then the test cases follow.
The first line of each test case contains a single integern(1≤n≤105).
The second line of each test case containsnintegersp1,p2,…,pn(1≤pi≤n) — the original permutation. Allpiare distinct.
The third line of each test case containsnintegersd1,d2,…,dn(1≤di≤n). Alldiare distinct.
Additional constraint on the input:

## Output
For each test case, output a line containingnintegers, where thei-th integer should be equal to the minimum number of operations required to fix the array which was obtained after thei-th query (i.e., the permutationpwhere all integerspd1,pd2,…,pdiare replaced by zeroes).