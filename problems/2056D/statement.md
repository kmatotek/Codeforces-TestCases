# Problem Description


An arraybofmintegers is calledgoodif,when it is sorted,b⌊m+12⌋=b⌈m+12⌉. In other words,bis good if both of its medians are equal. In particular,⌊m+12⌋=⌈m+12⌉whenmis odd, sobis guaranteed to be good if it has an odd length.
You are given an arrayaofnintegers. Calculate the number of good subarrays∗ina.
∗An arrayxis a subarray of an arrayyifxcan be obtained fromyby the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤105) — the length of the array.
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤10) — the given array.
It is guaranteed that the sum ofnover all test cases does not exceed105.

## Output
For each test case, output a single integer representing the number of good subarrays ina.