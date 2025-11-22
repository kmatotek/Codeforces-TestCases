# Problem Description

Given a stringsthat consists only of the first three letters of the Latin alphabet, meaning each character of the string is eithera,b, orc.
Also given areqoperations that need to be performed on the string. In each operation, two lettersxandyfrom the set of the first three letters of the Latin alphabet are provided, and for each operation, one of the following two actions must be taken:
The goal is to perform all operations in the given order in such a way that the stringsbecomes lexicographically minimal.
Recall that a stringais lexicographically less than a stringbif and only if one of the following conditions holds:

## Input
Each test consists of several test cases. The first line contains a single integert(1≤t≤103) — the number of test cases. The description of the test cases follows.
In the first line of each test case, there are two integersnandq(1≤n,q≤2⋅105) — the length of the stringsand the number of operations.
In the second line of each test case, the stringsis given — a string of exactlyncharacters, each of which isa,b, orc.
The nextqlines of each test case contain the description of the operations. Each line contains two charactersxandy, each of which isa,b, orc.
Additional constraints on the input:

## Output
For each test case, output the lexicographically minimal string that can be obtained fromsusing the given operations.