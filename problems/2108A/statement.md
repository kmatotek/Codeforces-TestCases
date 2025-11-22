# Problem Description


For a permutationpof lengthn∗, we define the function:
f(p)=n∑i=1|pi−i|
You are given a numbern. You need to compute how manydistinctvalues the functionf(p)can take when consideringall possiblepermutations of the numbers from1ton.
∗A permutation of lengthnis an array consisting ofndistinct integers from1tonin arbitrary order. For example,[2,3,1,5,4]is a permutation, but[1,2,2]is not a permutation (2appears twice in the array), and[1,3,4]is also not a permutation (n=3but there is4in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤100). The description of the test cases follows.
The first line of each test case contains an integern(1≤n≤500) — the number of numbers in the permutations.

## Output
For each test case, output a single integer — the number of distinct values of the functionf(p)for the given length of permutations.