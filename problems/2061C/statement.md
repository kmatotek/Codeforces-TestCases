# Problem Description


Kevin enjoys logic puzzles.
He played a game withnclassmates who stand in a line. Thei-th person from the left says that there areailiars to their left (not including themselves).
Each classmate is either honest or a liar, with the restriction thatno two liars can stand next to each other. Honest classmates always say the truth.Liars can say either the truth or lies, meaning their statements are considered unreliable.
Kevin wants to determine the number of distinct possible game configurations modulo998244353. Two configurations are considered different if at least one classmate is honest in one configuration and a liar in the other.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains an integern(1≤n≤2⋅105) — the number of classmates.
The second line containsnintegersa1,a2,…,an(0≤ai≤n) — the number of liars to the left of thei-th person they claimed.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output one integer — the number of distinct game configurations modulo998244353.