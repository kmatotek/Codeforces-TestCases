# Problem Description

A segment of positive integers[l,r]is calledcoprimeiflandrare coprime∗.
A coprime segment[l,r]is calledminimal coprimeif it does not contain†any coprime segment not equal to itself. To better understand this statement, you can refer to the notes.
Given[l,r], a segment of positive integers, find the number of minimal coprime segments contained in[l,r].
∗Two integersaandbare coprime if they share only one positive common divisor. For example, the numbers2and4are not coprime because they are both divided by2and1, but the numbers7and9are coprime because their only positive common divisor is1.
†A segment[l′,r′]is contained in the segment[l,r]if and only ifl≤l′≤r′≤r.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤100). The description of the test cases follows.
The only line of each test case consists of two integerslandr(1≤l≤r≤109).

## Output
For each test case, output the number of minimal coprime segments contained in[l,r], on a separate line.