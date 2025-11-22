# Problem Description

You are given two integersnandk;kis an odd number not less than3. Your task is to turnninto0.
To do this, you can perform the following operation any number of times: choose a numberxfrom1tokand subtract it fromn. However, if thecurrentvalue ofnis even (divisible by2), thenxmust also be even, and if thecurrentvalue ofnis odd (not divisible by2), thenxmust be odd.
In different operations, you can choose the same values ofx, but you don't have to. So, there are no limitations on using the same value ofx.
Calculate the minimum number of operations required to turnninto0.

## Input
The first line contains one integert(1≤t≤10000) — the number of test cases.
Each test case consists of one line containing two integersnandk(3≤k≤n≤109,kis odd).

## Output
For each test case, output one integer — the minimum number of operations required to turnninto0.