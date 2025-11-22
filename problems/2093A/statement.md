# Problem Description

We call an arraya, consisting ofkpositive integers, palindromic if[a1,a2,…,ak]=[ak,ak−1,…,a1]. For example, the arrays[1,2,1]and[5,1,1,5]are palindromic, while the arrays[1,2,3]and[21,12]are not.
We call a numberkan ideal generator if any integern(n≥k) can be represented as the sum of the elements of a palindromic array of length exactlyk. Each element of the array must be greater than0.
For example, the number1is an ideal generator because any natural numberncan be generated using the array[n]. However, the number2is not an ideal generator — there is no palindromic array of length2that sums to3.
Determine whether the given numberkis an ideal generator.

## Input
The first line of the input contains one integert(1≤t≤1000) — the number of test cases.
The first and only line of each test case contains one integerk(1≤k≤1000).

## Output
For each numberk, you need to output the word"YES"if it is an ideal generator, or"NO"otherwise.
You may output"Yes"and"No"in any case (for example, the strings"yES","yes", and"Yes"will be recognized as a positive answer).