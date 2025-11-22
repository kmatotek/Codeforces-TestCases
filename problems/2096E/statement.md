# Problem Description

You are the proud owner ofnteddy bears, which are arranged in a row on a shelf. Each teddy bear is colored either black or pink.
An arrangement of teddy bears isbeautifulif all the black teddy bears are to the left of all the pink teddy bears. In other words, theredoes notexist a pair of indices(i,j)(1≤i<j≤n) such that thei-th teddy bear is pink, and thej-th teddy bear is black.
You want to reorder the teddy bears into a beautiful arrangement. You are too short to reach the shelf, but luckily, you can send instructions to a robot to move the teddy bears around. In a single instruction, the robot can:
What is the minimum number of instructions needed to reorder the teddy bears?

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(3≤n≤2⋅105) — the number of teddy bears.
The second line of each test case contains a single stringsof lengthnconsisting of charactersBandP— the colors of the teddy bears. For eachifrom1ton, thei-th teddy bear is colored black ifsi=Band pink ifsi=P.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output a single integer — the minimum number of instructions needed to reorder the teddy bears.