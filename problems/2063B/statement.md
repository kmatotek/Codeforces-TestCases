# Problem Description


But as they are a crucial part of home design, Little John decides to hide some in the most unreachable places — under the eco-friendly wood veneers.
You are given an integer sequencea1,a2,…,an, and a segment[l,r](1≤l≤r≤n).
You must perform the following operation on the sequenceexactly once.
Formally, choose any number of indicesi1,i2,…,iksuch that1≤i1<i2<…<ik≤n. Then, change theix-th element to the original value of theik−x+1-th element simultaneously for all1≤x≤k.
Find theminimum valueofal+al+1+…+ar−1+arafter performing the operation.
∗A sequencebis a subsequence of a sequenceaifbcan be obtained fromaby the deletion of several (possibly, zero or all) element from arbitrary positions.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains three integersn,l,r(1≤l≤r≤n≤105) — the length ofa, and the segment[l,r].
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤109).
It is guaranteed that the sum ofnover all test cases does not exceed105.

## Output
For each test case, output the minimum value ofal+al+1+…+ar−1+aron a separate line.