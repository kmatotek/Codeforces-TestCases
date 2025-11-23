# Problem Description

One day, the schoolboy Mark misbehaved, so the teacher Sasha called him to the whiteboard.
Sasha gave Mark a table withnrows andmcolumns. His task is to arrange the numbers0,1,…,n⋅m−1in the table (each number must be used exactly once) in such a way as to maximize the sum of MEX∗across all rows and columns. More formally, he needs to maximizen∑i=1mex({ai,1,ai,2,…,ai,m})+m∑j=1mex({a1,j,a2,j,…,an,j}),whereai,jis the number in thei-th row andj-th column.
Sasha is not interested in how Mark arranges the numbers, so he only asks him to state one number — the maximum sum of MEX across all rows and columns that can be achieved.
∗The minimum excluded (MEX) of a collection of integersc1,c2,…,ckis defined as the smallest non-negative integerxwhich does not occur in the collectionc.
For example:

## Input
Each test contains multiple test cases. The first line contains a single integert(1≤t≤1000) — the number of test cases. The description of the test cases follows.
The first line of each test case contains two integersnandm(1≤n,m≤109) — the number of rows and columns in the table, respectively.

## Output
For each test case, output the maximum possible sum ofmexacross all rows and columns.