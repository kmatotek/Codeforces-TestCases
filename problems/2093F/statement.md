# Problem Description

Hackers are once again trying to create entertaining phrases using the output of neural networks. This time, they want to obtain an array of stringsaof lengthn.
Initially, they have an arraycof lengthn, filled with blanks, which are denoted by the symbol∗. Thus, ifn=4, then initiallyc=[∗,∗,∗,∗].
The hackers have access tomneural networks, each of which has its own version of the answer to their request – an array of stringsbiof lengthn.
The hackers are trying to obtain the arrayafrom the arraycusing the following operations:
For example, if the first neural network is chosen andc=[∗,«like»,∗], andb1=[«I»,«love»,«apples»], then after the operation with the first neural network,cmay become either[«I»,«like»,∗]or[∗,«like»,«apples»].
Unfortunately, because of the way hackers access neural networks, they will only be able to see the modified arraycafter all operations are completed, so they will have to specify the entire sequence of operations in advance.
However, the random behavior of the neural networks may lead to the situation where the desired array is never obtained, or obtaining it requires an excessive number of operations.
Therefore, the hackers are counting on your help in choosing a sequence of operations that will guarantee the acquisition of arrayain the minimum number of operations.
More formally, if there exists a sequence of operations that canguaranteeobtaining arrayafrom arrayc, then among all such sequences, find the one with theminimumnumber of operations, and output the number of operations in it.
If there is no sequence of operations that transforms arraycinto arraya, then output−1.

## Input
The first line contains a single integert(1≤t≤1000) — the number of test cases.
The first line of each test case contains two integersnandm(1≤n,m≤500) — the length of the original arrayaand the number of neural networks, respectively.
The second line of each test case contains the arraya, consisting ofnstringsai(1≤|ai|≤10), separated by spaces.
The nextmlines of each test case contain the arraysbi— one in each line, consisting ofnstringsbi,j(1≤|bi,j|≤10), separated by spaces.
It is guaranteed that the sum of|ai|and|bi,j|across all test cases does not exceed2⋅105, and that the sum ofn⋅macross all test cases also does not exceed2⋅105.
It is guaranteed that the input strings consist only of characters from the Latin alphabet in both lowercase and uppercase.
Note that the length of each individual input string does not exceed10.

## Output
Outputtnumbers — one number for each test case, each on a separate line.
If there exists a sequence of operations that guarantees obtaining arrayafrom thei-th test case, then thei-th number is the number of operations in the minimum such sequence.
Otherwise, for thei-th number, output−1.