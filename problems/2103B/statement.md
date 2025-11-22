# Problem Description


You are given a binary stringsof lengthnand a typewriter with two buttons:0and1. Initially, your finger is on the button0. You can do the following two operations:
Thecostof a binary string is defined as the minimum number of operations needed to type the entire string.
Before typing, you may reverse at most one substring∗ofs. More formally, you can choose two indices1≤l≤r≤n, and reverse the substringsl…r, resulting in the new strings1s2…sl−1srsr−1…slsr+1…sn.
Your task is to find the minimum possible cost among all strings obtainable by performing at most one substring reversal ons.
∗A stringais a substring of a stringbifacan be obtained frombby the deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤2⋅105) — the length of the binary strings.
The second line of each test case contains a binary strings1s2…sn(si=0orsi=1) — the characters of the binary strings.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output the minimum cost of stringsafter performing at most one substring reversal.