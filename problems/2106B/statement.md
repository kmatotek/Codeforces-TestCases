# Problem Description

Given a permutation∗pof lengthnthat contains every integer from0ton−1and a strip ofncells, St. Chroma will paint thei-th cell of the strip in the colorMEX(p1,p2,...,pi)†.
For example, supposep=[1,0,3,2]. Then, St. Chroma will paint the cells of the strip in the following way:[0,2,2,4].
You have been given two integersnandx. Because St. Chroma loves colorx, construct a permutationpsuch that the number of cells in the strip that are painted colorxismaximized.
∗A permutation of lengthnis a sequence ofnelements that contains every integer from0ton−1exactly once. For example,[0,3,1,2]is a permutation, but[1,2,0,1]isn't since1appears twice, and[1,3,2]isn't since0does not appear at all.
†TheMEXof a sequence is defined as the first non-negative integer that does not appear in it. For example,MEX(1,3,0,2)=4, andMEX(3,1,2)=0.

## Input
The first line of the input contains a single integert(1≤t≤4000) — the number of test cases.
The only line of each test case contains two integersnandx(1≤n≤2⋅105,0≤x≤n) — the number of cells and the color you want to maximize.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
Output a permutationpof lengthnsuch that the number of cells in the strip that are painted colorxismaximized. If there exist multiple such permutations, output any of them.