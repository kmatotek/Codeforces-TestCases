# Problem Description


Call an arraybof sizemgoodif the following conditions hold:
For example, the array[1,1,3,3,5]isgood(where the permutationp=[2,1,5,3,4]satisfies the second requirement), but the array[1,1,2]isn't.
Note the empty array is considered to begood.
You are given an arrayaof sizen. Find the length of the longestgoodsubsequence^{\text{†}}ofa.
^{\text{∗}}A permutation of lengthmis an array consisting ofmdistinct integers from1tomin arbitrary order. For example,[2,3,1,5,4]is a permutation, but[1,2,2]is not a permutation (2appears twice in the array), and[1,3,4]is also not a permutation (m=3but there is4in the array).
^{\text{†}}A sequencecis a subsequence of a sequencedifccan be obtained fromdby the deletion of several (possibly, zero or all) element from arbitrary positions.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1 \le t \le 10^4). The description of the test cases follows.
The first line of each test case contains an integern(1 \leq n \leq 15\,000) – the length ofa.
The second line of each test case containsnintegersa_1,a_2,\ldots,a_n(1 \leq a_i \leq n) — denoting the arraya.
It is guaranteed that the sum ofn^2does not exceed15\,000^2over all test cases.

## Output
For each test case, output the length of the longest good subsequence ofaon a new line.