# Problem Description

Let us define thebeautyof a binary stringzas the number of indicesisuch that1≤i<|z|andzi≠zi+1.
While waiting for his friends from the CCB, Andryusha baked a pie, represented by a binary stringsof lengthn. To avoid offending anyone, he wants to divide this string intoksubstrings such that each digit belongs to exactly one substring, and the beauties of all substrings are the same.
Andryusha does not know the exact number of friends from the CCB who will come to his house, so he wants to find the number of values ofkfor which it is possible to split the pie into exactlykparts with equal beauties.
However, Andryusha's brother, Tristan, decided that this formulation of the problem is too simple. Therefore, he wants you to find the number of such values ofkfor each prefix of the string. In other words, for eachifrom1ton, you need to find the number of values ofkfor which it is possible to split the prefixs1s2…siinto exactlykparts with equal beauties.

## Input
Each test consists of several test cases. The first line of the input data contains one integert(1≤t≤105) — the number of test cases. The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤106) — the length of the binary string.
The second line of each test case contains a binary string of lengthn, consisting only of digits0and1.
It is guaranteed that the sum ofnacross all test cases does not exceed106.

## Output
For each test case, output a single line containingnintegersci(0≤ci≤n) — the number of values ofkfor which it is possible to split the prefixs1s2…siinto exactlykparts with equal beauties.