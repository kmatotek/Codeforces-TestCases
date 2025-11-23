# Problem Description

You are given a string $$$s$$$ consisting of lowercase Latin letters.
You can perform the following operation with the string $$$s$$$: choose a contiguous substring (possibly empty) of $$$s$$$ and shuffle it (reorder the characters in the substring as you wish).
Recall that a palindrome is a string that reads the same way from the first character to the last and from the last character to the first. For example, the stringsa,bab,acca,bcabcbacbare palindromes, but the stringsab,abbbaa,cccbare not.
Your task is to determine the minimum possible length of the substring on which the aforementioned operation must be performed in order to convert the given string $$$s$$$ into a palindrome.

## Input
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The only line of each test case contains a string $$$s$$$ ($$$2 \le |s| \le 2 \cdot 10^5$$$), consisting of lowercase Latin letters.
Additional constraints on the input:

## Output
For each test case, print a single integer — the minimum possible length of the substring on which the aforementioned operation must be performed in order to convert the given string $$$s$$$ into a palindrome.