# Problem Description

There aren+mdistinct points(a1,0),(a2,0),…,(an,0),(b1,2),(b2,2),…,(bm,2)on the plane. Initially, your score is0. To increase your score, you can perform the following operation:
Letkmaxbe the maximum number of operations that can be performed. For example, if it is impossible to perform any operation,kmaxis0. Additionally, definef(k)as the maximum possible score achievable by performing the operationexactlyktimes. Here,f(k)is defined for all integersksuch that0≤k≤kmax.
Find the value ofkmax, and find the values off(x)for all integersx=1,2,…,kmaxindependently.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤3⋅104). The description of the test cases follows.
The first line of each test case contains two integersnandm(1≤n,m≤2⋅105).
The second line of each test case containsnpairwise distinct integersa1,a2,…,an— the points ony=0(−109≤ai≤109).
The third line of each test case containsmpairwise distinct integersb1,b2,…,bm— the points ony=2(−109≤bi≤109).
It is guaranteed that both the sum ofnand the sum ofmover all test cases do not exceed2⋅105.

## Output
For each test case, given that the maximum number of operations iskmax, you must output at most two lines:
Note that under the constraints of this problem, it can be shown that all values off(x)are integers no greater than1016.