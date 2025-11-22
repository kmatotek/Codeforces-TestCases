# Problem Description

After three hundred years of slime farming, Akito finally obtained the magical numbern. Upon reaching the merchant, he wanted to exchange the number for gold, but the merchant gave the hero a quest.
The merchant said that for the quest, the skillrev(n,p)would be required, which Akito, by happy coincidence, had recently learned.rev(n,p)represents the following procedure:
The merchant's quest was to calculate the sumx=k∑p=2rev(n,p). Since this number can be quite large, only the remainder ofxwhen divided by109+7is required. The merchant also mentioned that the previous traveler had been calculating this sum for three hundred years and had not finished it. But you will help Akito finish it faster, right?

## Input
The first line contains the numbert(1≤t≤5000) — the number of test cases.
In the only line of each test case, two numbersnandkare given (1≤n≤3⋅105,2≤k≤1018) — the magical number and the upper limit for summation.
Note thatthe sum ofnacross all test cases is not bounded.

## Output
For each test case, you need to output a single number — the remainder ofx=k∑p=2rev(n,p)when divided by109+7.