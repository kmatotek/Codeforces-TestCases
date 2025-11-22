# Problem Description

The final of the first Olympiad by IT Campus "NEIMARK" is scheduled for March 1, 2025. A nameless intern was tasked with forming the date of the Olympiad using digits — 01.03.2025.
To accomplish this, the intern took a large bag of digits and began drawing them one by one. In total, he drewndigits — the digitaiwas drawn in thei-th turn.
You suspect that the intern did extra work. Determine at which step the intern could have first assembled the digits to form the date of the Olympiad (the separating dots can be ignored), or report that it is impossible to form this date from the drawn digits. Note that leading zerosmust be displayed.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤20).
The second line of each test case containsnintegersai(0≤ai≤9) — the numbers that the intern pulled out in chronological order.

## Output
For each test case, output the minimum number of digits that the intern could pull out. If all the digits cannot be used to make a date, output the number0.