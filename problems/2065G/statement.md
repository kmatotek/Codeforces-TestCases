# Problem Description

Skibidus was abducted by aliens of Amog! Skibidus tries to talk his way out, but the Amog aliens don't believe him. To prove that he is not totally capping, the Amog aliens asked him to solve this task:
An integerxis considered asemi-primeif it can be written asp⋅qwherepandqare (not necessarily distinct)prime numbers. For example,9is asemi-primesince it can be written as3⋅3, and3is a prime number.
Skibidus was given an arrayacontainingnintegers. He must report the number of pairs(i,j)such thati≤jandlcm(ai,aj)∗issemi-prime.
∗Given two integersxandy,lcm(x,y)denotes theleast common multipleofxandy.

## Input
The first line contains an integert(1≤t≤104) — the number of test cases.
The first line of each test case contains an integern(2≤n≤2⋅105).
The following line containsnintegersa1,a2,…,an(2≤ai≤n).
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output the number of ordered pairs of indices on a new line.