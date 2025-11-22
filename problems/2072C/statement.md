# Problem Description

Akito still has nowhere to live, and the price for a small room is everywhere. For this reason, Akito decided to get a job at a bank as a key creator for storages.
In this magical world, everything is different. For example, the key for a storage with the code(n,x)is an arrayaof lengthnsuch that:
Akito diligently performed his job for several hours, but suddenly he got a headache. Substitute for him for an hour; for the givennandx, create any key for the storage with the code(n,x).
∗MEX(S)is the minimum non-negative integerzsuch thatzis not contained in the setSand all0≤y<zare contained inS.

## Input
The first line contains the numbert(1≤t≤104) — the number of test cases.
In the only line of each test case, two numbersnandx(1≤n≤2⋅105,0≤x<230) are given — the length of the array and the desired value of the bitwise "OR".
It is guaranteed that the sum ofnacross all test cases does not exceed2⋅105.

## Output
For each test case, outputnintegersai(0≤ai<230) — the elements of the key array that satisfy all the conditions.
If there are multiple suitable arrays, output any of them.