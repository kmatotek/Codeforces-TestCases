# Problem Description

Akito got tired of being a simple locksmith at a bank, so he decided to enroll in the Magical Academy and become the best wizard in the world! However, to enroll, he needed to solve a single problem on the exam, which the ambitious hero could not manage.
In the problem, he was given an arrayaof lengthn. He needed to minimize the number of inversions∗in the array after applying the spellexactly once. The spell was simple; to apply it, Akito had to choose two numberslandrsuch that1≤l≤r≤nand perform a cyclic shift of the subarray fromltorone position to the left.
More formally, Akito selects the subarray[l,r]and modifies the array as follows:
Akito is eager to start his studies, but he still hasn't passed the exam. Help him enroll and solve the problem!
∗An inversion in an arraybof lengthmis defined as a pair of indices(i,j)such that1≤i<j≤mandbi>bj. For example, in the arrayb=[3,1,4,1,5], the inversions are the pairs of indices(1,2),(1,4),(3,4).

## Input
The first line of input contains a numbert(1≤t≤104) — the number of test cases.
In the first line of each test case, there is a numbern(1≤n≤2000) — the length of the arraya.
In the second line of each test case, there arennumbersai(1≤ai≤2000) — the elements of the arraya.
It is guaranteed that the sum ofn2across all test cases does not exceed4⋅106.

## Output
For each test case, output two numberslandr(1≤l≤r≤n) — the boundaries of the subarray that should be chosen so that after applying the spell, the number of inversions in the array is minimized.
If there are multiple suitable pairs of boundaries, you may output any of them.