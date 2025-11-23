# Problem Description

You're given integerskandn. For each integerxfrom1tok, count the number of integer arraysasuch that all of the following are satisfied:
Note that two arraysbandcare different if either their lengths are different, or if there exists an index1≤i≤|b|such thatbi≠ci.
Output the answer modulo998244353.

## Input
The first line contains an integert(1≤t≤103) — the number of independent test cases.
The only line of each test case contains two integerskandn(1≤k≤105,1≤n≤9⋅108).
It is guaranteed that the sum ofkover all test cases does not exceed105.

## Output
For each test case, outputkspace-separated integers on a new line: the number of arrays forx=1,2,…,k, modulo998244353.