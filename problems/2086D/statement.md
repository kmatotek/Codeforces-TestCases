# Problem Description

You would like to construct a string𝑠s, consisting of lowercase Latin letters, such that the following condition holds:
Constructing any string is too easy, so you will be given an array𝑐cof2626numbers — the required number of occurrences of each individual letter in the string𝑠s. So, for every𝑖∈[1,26]i∈[1,26], the𝑖i-th letter of the Latin alphabet should occur exactly𝑐𝑖citimes.
Your task is to count the number of distinct strings𝑠sthat satisfy all these conditions. Since the answer can be huge, output it modulo998244353998244353.

## Input
Each test consists of several test cases. The first line contains a single integer𝑡t(1≤𝑡≤1041≤t≤104)— the number of test cases. The description of test cases follows.
Each test case contains2626integers𝑐𝑖ci(0≤𝑐𝑖≤5⋅1050≤ci≤5⋅105)— the elements of the array𝑐c.
Additional constraints on the input data:

## Output
For each test case, print one integer — the number of suitable strings𝑠s, taken modulo998244353998244353.