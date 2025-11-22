# Problem Description

In Bobritto Bandito's home town of residence, there are an infinite number of houses on an infinite number line, with houses at…,−2,−1,0,1,2,…. On day0, he started a plague by giving an infection to the unfortunate residents of house0. Each succeeding day, the plague spreads toexactly onehealthy household that is next to an infected household. It can be shown that each day the infected houses form a continuous segment.
Let the segment starting at thel-th house and ending at ther-th house be denoted as[l,r]. You know that afterndays, the segment[l,r]became infected. Find any such segment[l′,r′]that could have been infected on them-th day (m≤n).

## Input
The first line contains an integert(1≤t≤100) – the number of independent test cases.
The only line of each test case contains four integersn,m,l, andr(1≤m≤n≤2000,−n≤l≤0≤r≤n,r−l=n).

## Output
For each test case, output two integersl′andr′on a new line. If there are multiple solutions, output any.