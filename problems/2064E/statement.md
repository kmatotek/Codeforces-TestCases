# Problem Description

Steve has a permutation∗pand an arrayc, both of lengthn. Steve wishes to sort the permutationp.
Steve has an infinite supply of coloured sand blocks, and using them he discovered a physics-based way to sort an array of numbers called gravity sort. Namely, to perform gravity sort onp, Steve will do the following:
Alex looks at Steve's sand blocks after performing gravity sort and wonders how many pairs of arrays(p′,c′)wherep′is a permutation would have resulted in the same layout of sand. Note that the original pair of arrays(p,c)will always be counted.
Please calculate this for Alex. As this number could be large, output it modulo998244353.
∗A permutation of lengthnis an array consisting ofndistinct integers from1tonin arbitrary order. For example,[2,3,1,5,4]is a permutation, but[1,2,2]is not a permutation (2appears twice in the array), and[1,3,4]is also not a permutation (n=3but there is a4in the array).

## Input
The first line contains an integert(1≤t≤104) — the number of test cases.
The first line of each testcase contains an integern(1≤n≤2⋅105) — the lengths of the arrays.
The second line of each testcase containsndistinctintegersp1,p2,…,pn(1≤pi≤n) — the elements ofp.
The following line containsnintegersc1,c2,…,cn(1≤ci≤n) — the elements ofc.
The sum ofnacross all testcases does not exceed2⋅105.

## Output
For each testcase, output the number of pairs of arrays(p′,c′)Steve could have started with, modulo998244353.