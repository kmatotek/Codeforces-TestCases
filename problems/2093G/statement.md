# Problem Description

The beauty of an arraybof lengthmis defined asmax(bi⊕bj)among all possible pairs1≤i≤j≤m, wherex⊕yis thebitwise XORof numbersxandy. We denote the beauty value of the arraybasf(b).
An arraybis called beautiful iff(b)≥k.
Recently, Kostya bought an arrayaof lengthnfrom the store. He considers this array too long, so he plans to cut out some beautiful subarray from it. That is, he wants to choose numberslandr(1≤l≤r≤n) such that the arrayal…ris beautiful. The length of such a subarray will be the numberr−l+1. The entire arrayais also considered a subarray (withl=1andr=n).
Your task is to find the length of the shortest beautiful subarray in the arraya. If no subarray is beautiful, you should output the number−1.

## Input
The first line contains the number of test casest(1≤t≤104).
Next, there aretblocks of two lines:
In the first line of the block, there are two integersnandk(1≤n≤2⋅105,0≤k≤109).
In the second line of the block, there is the arrayaconsisting ofnintegers (0≤ai≤109).
It is guaranteed that the sum ofnacross all tests does not exceed2⋅105.

## Output
For each test case, you need to output a single integer — the minimum length of the segment(l,r)for whichf(al…r)≥k. If such a segment is not found, you should output−1.