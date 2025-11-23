# Problem Description

Today, Alice has given Bob arrays for him to sort in increasing order again! At this point, no one really knows how many times she has done this.
Bob is given two sequencesaandb, both of lengthn. All integers in the range from1to2nappear exactly once in eitheraorb. In other words, the concatenated∗sequencea+bis a permutation†of length2n.
Bob must sortboth sequencesin increasing orderat the same timeusing Alice'sswapfunction. Alice'sswapfunction is implemented as follows:
Given sequencesaandb, please determine if both sequences can be sorted in increasing order simultaneously after using Alice'sswapfunction any number of times.
∗The concatenated sequencea+bdenotes the sequence[a1,a2,a3,…,b1,b2,b3,…].
†A permutation of lengthmcontains all integers from1tomin some order.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(3≤n≤2⋅105).
The second line of each test case containsa1,a2,…,an(1≤ai≤2n).
The third line of each test case containsb1,b2,…,bn(1≤bi≤2n).
It is guaranteed that all integers in the range[1,2n]appear exactly once in eitheraorb.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
If it is possible to sort both sequences simultaneously, print "YES" on a new line. Otherwise, print "NO" on a new line.
You can output the answer in any case. For example, the strings "yEs", "yes", and "Yes" will also be recognized as positive responses.