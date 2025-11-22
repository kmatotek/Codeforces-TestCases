# Problem Description

Let's call an arraybbeautifulif it consists of at least two elements and there exists a positionisuch that|bi−bi+1|≤1(where|x|is the absolute value ofx).
You are given an arraya, and as long as it consists of at least two elements, you can perform the following operation:
Calculate the minimum number of operations required to make the array beautiful, or report that it is impossible.

## Input
The first line contains one integert(1≤t≤200) — the number of test cases.
The first line of each test case contains one integern(2≤n≤1000) — the size of the arraya.
The second line containsnintegersa1,a2,…,an(1≤ai≤106) — the arrayaitself.

## Output
For each test case, output one integer — the minimum number of operations needed to make the arrayabeautiful, or−1if it is impossible to make it beautiful.