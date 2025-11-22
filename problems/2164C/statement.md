# Problem Description

You are now in a dungeon withnswords, facingmmonsters.
The damage of thei-th sword isai, and the life value of thei-th monster isbi. A sword with damagexcan kill a monster with life valueyif and only ifx≥y.
After killing thei-th monster with a sword of damagex, this sword disappears. Then, ifci>0, you will obtain a new sword with damagemax(x,ci); otherwise, you gain nothing.
Now you want to know the maximum number of monsters you can kill. Note that you can kill each monster at most once.

## Input
Each test contains multiple test cases. The first line contains the number of test casesT(1≤T≤104). The description of the test cases follows.
The first line of each test case contains two integersnandm(1≤n,m≤2⋅105).
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤109).
The third line of each test case containsmintegersb1,b2,…,bm(1≤bi≤109).
The fourth line of each test case containsmintegersc1,c2,…,cm(0≤ci≤109).
It is guaranteed that the sum ofnandmover all test cases does not exceed2⋅105, respectively.

## Output
For each test case output one integer — the maximum number of monsters you can kill.