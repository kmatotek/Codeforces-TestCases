# Problem Description

Nikyr has started working as a queue manager at the company "Black Contour." He needs to choose the order of servicing customers. There are a total ofnqueues, each initially containing0people. In each of the nextnmoments of time, there aretwo sequentialevents:
Let the number of people in thei-th queue after all events bexi. Nikyr wants MEX†of the collectionx1,x2,…,xnto be as large as possible. Help him determine the maximum value he can achieve with an optimal order of servicing the queues.
†The minimum excluded (MEX) of a collection of integersc1,c2,…,ckis defined as the smallest non-negative integerywhich does not occur in the collectionc.
For example:

## Input
Each test consists of multiple test cases. The first line contains a single integert(1≤t≤2⋅104) — the number of test cases. The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤300) — the number of queues and moments of time.
Thei-th of the nextnlines containsnintegersai,1,ai,2,…,ai,n(1≤ai,j≤109) — the number of new customers in thei-th queue at each moment of time.
It is guaranteed that the sum ofn2over all test cases does not exceed2⋅105.

## Output
For each test case, output a single integer — the maximum value ofMEX([x1,x2,…,xn])that can be achieved.