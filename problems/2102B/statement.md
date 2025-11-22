# Problem Description


You are given an array of integersa1,a2,…,an. You are allowed to do the following operation any number of times (possibly zero):
Your task is to determine whether it is possible to make the element at index1become the median of the array after doing the above operation any number of times. Note that operations can be applied to index1as well, meaning the median can be either the original value ofa1or its negation.
The median of an arrayb1,b2,…,bmis defined as the⌈m2⌉-th∗smallest element of arrayb. For example, the median of the array[3,1,2]is2, while the median of the array[10,1,8,3]is3.
It is guaranteed that the absolute value of the elements ofaare distinct. Formally, there are no pairs of indices1≤i<j≤nwhere|ai|=|aj|.
∗⌈x⌉is the ceiling function which returns the least integer greater than or equal tox.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤105) — the length of the arraya.
The second line of each test case containsnintegersa1,a2,…,an(|ai|≤106,|ai|≠|aj|) — the elements of the arraya.
It is guaranteed that the sum ofnover all test cases does not exceed105.

## Output
For each testcase, output "YES" if it is possible to make the element at index1become the median of the array, and "NO" otherwise.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.