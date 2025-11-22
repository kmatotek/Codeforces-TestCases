# Problem Description


An elementbi(1≤i≤m) in an arrayb1,b2,…,bmis a local minimum if at least one of the following holds:
Similarly, an elementbi(1≤i≤m) in an arrayb1,b2,…,bmis a local maximum if at least one of the following holds:
Note that local minima and maxima are not defined for arrays with only one element.
There is a hidden permutation∗pof lengthn. The following two operations are applied to permutationpalternately, starting from operation 1, until there is only one element left inp:
More specifically, operation 1 is applied during every odd iteration, and operation 2 is applied during every even iteration, until there is only one element left inp.
For each indexi(1≤i≤n), letaibe the iteration number that elementpiis removed, or−1if it was never removed.
It can be proven that there will be only one element left inpafter at most⌈log2n⌉iterations (in other words,ai≤⌈log2n⌉).
You are given the arraya1,a2,…,an. Your task is to construct any permutationpofnelements that satisfies arraya.
∗A permutation of lengthnis an array consisting ofndistinct integers from1tonin arbitrary order. For example,[2,3,1,5,4]is a permutation, but[1,2,2]is not a permutation (2appears twice in the array), and[1,3,4]is also not a permutation (n=3but there is4in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(2≤n≤2⋅105) — the number of elements in permutationp.
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤⌈log2n⌉orai=−1) — the iteration number that elementpiis removed.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.
It is guaranteed that there exists at least one permutationpthat satisfies arraya.

## Output
For each test case, outputnintegers representing the elements of the permutation satisfying arraya.
If there are multiple solutions, you may output any of them.