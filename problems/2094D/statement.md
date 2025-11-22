# Problem Description

You have two drums in front of you: a left drum and a right drum. A hit on the left can be recorded as "L", and a hit on the right as "R".
The strange forces that rule this world are fickle: sometimes, a blow sounds once, and sometimes it sounds twice. Therefore, a hit on the left drum could have sounded as either "L" or "LL", and a hit on the right drum could have sounded as either "R" or "RR".
The sequence of hits made is recorded in the stringp, and the sounds heard are in the strings. Givenpands, determine whether it is true that the stringscould have been the result of the hits from the stringp.
For example, ifp="LR", then the result of the hits could be any of the strings "LR", "LRR", "LLR", and "LLRR", but the strings "LLLR" or "LRL" cannot.

## Input
The first line contains an integert(1≤t≤104) – the number of independent test cases.
The first line of each test case contains the stringp(1≤|p|≤2⋅105) consisting only of the characters "R" and "L", where|p|denotes the length of the stringp.
The second line of each test case contains the strings(1≤|p|≤|s|≤2⋅105) consisting only of the characters "R" and "L".
It is guaranteed that the sum of|s|does not exceed2⋅105across all test cases.

## Output
For each set of input data, output "YES" ifscan be the heard sound, and "NO" otherwise. You may output in any case.