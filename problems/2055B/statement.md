# Problem Description


There arendifferent types of magical materials, numbered from1ton. Initially, you haveaiunits of materialifor eachifrom1ton. You are allowed to perform the following operation:
You are trying to craft an artifact using these materials. To successfully craft the artifact, you must have at leastbiunits of materialifor eachifrom1ton. Determine if it is possible to craft the artifact by performing the operation any number of times (including zero).

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(2≤n≤2⋅105) — the number of types of materials.
The second line of each test case containsnintegersa1,a2,…,an(0≤ai≤109) — the amount of each materialithat you currently hold.
The third line of each test case containsnintegersb1,b2,…,bn(0≤bi≤109) — the amount of each materialineeded to produce the artifact.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, print a single line containing either "YES" or "NO", representing whether or not the artifact can be crafted.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.