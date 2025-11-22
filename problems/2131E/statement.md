# Problem Description


You're given an arrayaof lengthn. For each indexisuch that1≤i<n, you can perform the following operationat most once:
You can choose indices and perform the operations in any sequential order.
Given another arraybof lengthn, determine if it is possible to transformatob.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains one integern(2≤n≤2⋅105).
The second line of each test case containsnintegersa1,a2,…,an(0≤ai<230).
The third line of each test case containsnintegersb1,b2,…,bn(0≤bi<230).
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output "YES" (quotes excluded) ifacan be transformed tob; otherwise, output "NO". You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.