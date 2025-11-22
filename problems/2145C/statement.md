# Problem Description

Monocarp has a stringsof lengthn, consisting of the letters 'a' and 'b'. He wants to remove some (possibly zero) number ofconsecutiveletters from his string in such a way that the number of letters 'a' and 'b' in the resulting string becomes equal. Monocarp can start removing letters from any position in the strings.
Monocarp really likes his strings, so he wants to remove as few consecutive letters from it as possible.
Your task is to determine the minimum number of consecutive letters from the stringsthat need to be removed so that the number of letters 'a' and 'b' in the resulting string becomes equal. If it is necessary to remove all letters from the strings(i.e., make it empty), report this.

## Input
The first line contains one integert(1≤t≤104) — the number of test cases.
Each test case consists of two lines:
Additional constraint on the input: the sum of values ofnover all test cases does not exceed2⋅105.

## Output
For each test case, print the answer as follows:
If in order to make the number of letters 'a' and 'b' equal, it is necessary to remove all letters from the strings, output−1.
Otherwise, output the minimum number of consecutive letters that Monocarp needs to remove from his stringsso that the number of letters 'a' and 'b' becomes equal.