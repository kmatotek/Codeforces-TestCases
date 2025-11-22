# Problem Description

Flower gives Gellyfish two permutations∗of[0,1,…,n−1]:p0,p1,…,pn−1andq0,q1,…,qn−1.
Now Gellyfish wants to calculate an arrayr0,r1,…,rn−1through the following method:
But since Gellyfish is very lazy, you have to help her figure out the elements ofr.
Since the elements ofrare very large, you are only required to output the elements ofrmodulo998\,244\,353.
^{\text{∗}}An arraybis a permutation of an arrayaifbconsists of the elements ofain arbitrary order. For example,[4,2,3,4]is a permutation of[3,2,4,4]while[1,2,2]is not a permutation of[1,2,3].

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1 \le t \le 10^4). The description of the test cases follows.
The first line of each test case contains a single integern(1 \leq n \leq 10^5).
The second line of each test case containsnintegersp_0, p_1, \ldots,p_{n-1}(0 \leq p_i < n).
The third line of each test case containsnintegersq_0, q_1, \ldots,q_{n-1}(0 \leq q_i < n).
It is guaranteed that bothpandqare permutations of[0, 1, \ldots, n-1].
It is guaranteed that the sum ofnover all test cases does not exceed10^5.

## Output
For each test case, outputnintegersr_0, r_1, \ldots, r_{n-1}in a single line, modulo998\,244\,353.