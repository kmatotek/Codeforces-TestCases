# Problem Description

The boarding process for various flights can occur in different ways: either bybusor through atelescopic jet bridge. Every day, exactly one flight is made from St. Petersburg to Minsk, and Vadim decided to demonstrate to the students that he always knows in advance how the boarding will take place.
Vadim made a bet withnstudents, and with thei-th student, he made a bet on dayai. Vadim wins the bet if he correctly predicts the boarding process on both dayai+1and dayai+2.
Although Vadim does not know in advance how the boarding will occur, he really wants to win the betat leastwith one student and convince him of his predictive abilities. Check if there exists a strategy for Vadim that allows him toguaranteesuccess.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integern(1≤n≤105) — the number of students Vadim made bets with.
The second line of each test case containsnintegersa1,…,an(1≤ai≤109) — the days on which Vadim made bets with the students.
It is guaranteed that the sum ofnover all test cases does not exceed105.

## Output
For each test case, output "Yes" (without quotes) if Vadim canguaranteeconvincing at least one student, and "No" otherwise.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.