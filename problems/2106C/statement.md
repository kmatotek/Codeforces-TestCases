# Problem Description

Two integer arraysaandbof sizenarecomplementaryif there exists an integerxsuch thatai+bi=xover all1≤i≤n. For example, the arraysa=[2,1,4]andb=[3,4,1]are complementary, sinceai+bi=5over all1≤i≤3. However, the arraysa=[1,3]andb=[2,1]are not complementary.
Cow the Nerd thinks everybody is interested in math, so he gave Cherry Bomb two integer arraysaandb. It is known thataandbboth containnnon-negativeintegers not greater thank.
Unfortunately, Cherry Bomb has lost some elements inb. Lost elements inbare denoted with−1. Help Cherry Bomb count the number of possible arraysbsuch that:

## Input
The first line of the input contains a single integert(1≤t≤104) — the number of test cases.
The first line of each test case contains two integersnandk(1≤n≤2⋅105,0≤k≤109) — the size of the arrays and the maximum possible value of their elements.
The second line containsnintegersa1,a2,...,an(0≤ai≤k).
The third line containsnintegersb1,b2,...,bn(−1≤bi≤k). Ifbi=−1, then this element is missing.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
Output exactly one integer, the number of ways Cherry Bomb can fill in the missing elements frombsuch thataandbare complementary.