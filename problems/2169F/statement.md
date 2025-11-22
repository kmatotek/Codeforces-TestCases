# Problem Description

Given three integersn,m,k, as well askarrays of integers of lengthsl1,l2,…,lkrespectively. We denote the element at positionjin array numberiasai,j. In each array, all elements are distinct (but may repeat in different arrays).
We call an arraybof lengthkbeautiful if for eachifrom1tok, the elementbiis equal to one of the elements of the arrayai.
We call an arraycperfect if every beautiful arraybcan be obtained from arraycby deleting several (possibly zero) elements without changing their order. In other words, arraycis perfect if every beautiful arraybis a subsequence of it.
Your task is to count the number of perfect arrayscof lengthncontaining only integers from1tom.

## Input
The first line contains three integersn,m,k(2≤n≤2⋅105;5≤m≤108;2≤k≤n).
The second line containskintegersl1,l2,…,lk(1≤li≤5).
The followingklines contain thei-th line withlidistinct integersai,1,ai,2,…,ai,li(1≤ai,j≤m).
Additional constraint on the input: the sum oflidoes not exceedn.

## Output
Print one integer — the number of perfect arrays of lengthnsuch that they contain only integers from1tom. Since the answer may be very large, output it modulo998244353.