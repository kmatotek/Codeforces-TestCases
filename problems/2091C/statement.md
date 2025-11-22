# Problem Description

At the IT Campus "NEIMARK", there are several top-secret rooms where problems for major programming competitions are developed. To enter one of these rooms, you must unlock a circular lock by selecting the correct code. This code is updated every day.
Today's code is a permutation∗of the numbers from1ton, with the property that in every cyclic shift†of it, there is exactly one fixed point. That is, in every cyclic shift, there exists exactly one element whose value is equal to its position in the permutation.
Output any valid permutation that satisfies this condition. Keep in mind that a valid permutation might not exist, then output−1.
∗A permutation is defined as a sequence of lengthnconsisting of integers from1ton, where each number appears exactly once. For example, (2 1 3), (1), (4 3 1 2) are permutations; (1 2 2), (3), (1 3 2 5) are not.
†A cyclic shift of an array is obtained by moving the last element to the beginning of the array. A permutation of lengthnhas exactlyncyclic shifts.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤500). The description of the test cases follows.
A single line of each test case contains a single integern(1≤n≤2⋅105).
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output the desired permutation. If multiple solutions exist, output any one of them. If no suitable permutations exist, output−1.