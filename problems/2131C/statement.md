# Problem Description

Given twomultisetsSandTof sizenand a positive integerk, you may perform the following operations any number (including zero) of times onS:
Determine if it is possible to makeSequal toT. Two multisetsSandTare equal if every element appears the same number of times inSandT.

## Input
Each test contains multiple test cases. The first line contains an integert(1≤t≤104) — the number of test cases. The description of the test cases follows.
The first line contains two integersnandk(1≤n≤2⋅105,1≤k≤109) — the size ofSand the constant, respectively.
The second line containsnintegersS1,S2,…,Sn(0≤Si≤109) — the elements inS.
The third line containsnintegersT1,T2,…,Tn(0≤Ti≤109) — the elements inT.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output "YES" if it is possible to makeSequal toT, and "NO" otherwise.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.