# Problem Description

You are given two permutationsp1,p2,…,pnandq1,q2,…,qnof lengthn. In one operation, you can select two integers1≤i,j≤n,i≠jand swappiandpj. The cost of the operation ismin(|i−j|,|pi−pj|).
Find the minimum cost to makepi=qihold for all1≤i≤nand output a sequence of operations to achieve the minimum cost.
A permutation of lengthnis an array consisting ofndistinct integers from1tonin arbitrary order. For example,[2,3,1,5,4]is a permutation, but[1,2,2]is not a permutation (2appears twice in the array), and[1,3,4]is also not a permutation (n=3but there is4in the array).

## Input
The first line of input contains a single integert(1≤t≤104) — the number of input test cases.
The first line of each test case contains one integern(2≤n≤100) — the length of permutationspandq.
The second line containsnintegersp1,p2,…,pn(1≤pi≤n) — the permutationp. It is guaranteed thatp1,p2,…,pnis a permutation of1,2,…,n.
The third line containsnintegersq1,q2,…,qn(1≤qi≤n) — the permutationq. It is guaranteed thatq1,q2,…,qnis a permutation of1,2,…,n.
It is guaranteed that the sum ofn3over all test cases does not exceed106.

## Output
For each test case, output the total number of operationsk(0≤k≤n2) on the first line. Then outputklines, each containing two integersi,j(1≤i,j≤n,i≠j) representing an operation to swappiandpjin order.
It can be shown that no optimal operation sequence has a length greater thann2.