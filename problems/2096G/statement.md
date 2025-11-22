# Problem Description

This is an interactive problem.
You are a proud teacher at the Millennium Science School. Today, a student named Alice challenges you to a guessing game.
Alice is thinking of an integer from1ton, and you must guess it by asking her some queries.
To make things harder, she says you mustask all the queries first, and she willignoreexactly1query.
For each query, you choose an array ofkdistinctintegers from1ton, wherekis even. Then, Alice will respond with one of the following:
Alice is impatient, so you must find a strategy thatminimizesthe number of queries. Can you do it?
Formally, letf(n)be the minimum number of queries required to determine Alice's number. Then you must find a strategy that usesexactlyf(n)queries.
Note that the interactor isadaptive, which means Alice's number is not fixed at the beginning and may depend on your queries. However, it is guaranteed that there exists at least one number that is consistent with Alice's responses.
We can show thatf(n)≤20for allnsuch that2≤n≤2⋅105.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The only line of each test case contains a single integern(2≤n≤2⋅105) — the maximum possible value of Alice's number.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.
