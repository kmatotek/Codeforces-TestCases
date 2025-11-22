# Problem Description

Some teachers work at the educational center "Sirius" while simultaneously studying at the university. In this case, the trip does not exempt them from completing their homework, so they do their homework right on the plane. Artem is one of those teachers, and he was assigned the following homework at the university.
With an arbitrary stringaofevenlengthm, he can perform the following operation. Artem splits the stringainto two halvesxandyof equal length, after which he performsexactly oneof three actions:
Unfortunately, Artem fell asleep on the plane, so you will have to complete his homework. Artem has two binary stringssandtof lengthn, each consisting ofncharacters0or1. Determine whether it is possible to make stringsequal to stringtwithan arbitrarynumber of operations.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤105). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤106) — the length of the stringssandt.
The second line of each test case contains the stringsof lengthn, consisting only of characters0and1.
The third line of each test case contains the stringtof lengthn, consisting only of characters0and1.
It is guaranteed that the sum ofnover all test cases does not exceed106.

## Output
For each test case, output "Yes" (without quotes) if it is possible to make stringsequal to stringt, and "No" otherwise.
You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.