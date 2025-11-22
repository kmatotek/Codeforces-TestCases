# Problem Description

A matrix is called quaternary if all its elements are0,1,2, or3.
Ecrade calls a quaternary matrixAgoodif the following two properties hold.
Ecrade has a quaternary matrix of sizen×m. He is interested in the minimum number of elements that need to be changed for the matrix to becomegood, and he also wants to find one of the possible resulting matrices.
However, it seems a little difficult, so please help him!

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤2⋅105). The description of the test cases follows.
The first line of each test case contains two integersnandm(1≤n,m≤103).
This is followed bynlines, each containing exactlymcharacters and consisting only of0,1,2, and3, describing the elements of Ecrade's matrix.
It is guaranteed that the sum ofn⋅mover all test cases does not exceed106.

## Output
For each test case, print the minimum number of elements that need to be changed for the matrix to becomegoodon the first line, then printnlines, each containing exactlymcharacters and consisting only of0,1,2, and3, describing one of the possible resulting matrices.
If there are multiple possible resulting matrices, output any of them.