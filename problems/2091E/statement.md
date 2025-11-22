# Problem Description

Recently, Misha at the IT Campus "NEIMARK" camp learned a new topic — the Euclidean algorithm.
He was somewhat surprised when he realized thata⋅b=lcm(a,b)⋅gcd(a,b), wheregcd(a,b)— isthe greatest common divisor (GCD)of the numbersaandbandlcm(a,b)— isthe least common multiple (LCM). Misha thought that since the product of LCM and GCD exists, it might be interesting to consider their quotient:F(a,b)=lcm(a,b)gcd(a,b).
For example, he tooka=2andb=4, computedF(2,4)=42=2and obtained a prime number (a number is prime if it has exactly two divisors)! Now he considersF(a,b)to be an interesting ratio ifa<bandF(a,b)is a prime number.
Since Misha has just started studying number theory, he needs your help to calculate — how many different pairs of numbersaandbare there such thatF(a,b)is an interesting ratio and1≤a<b≤n?

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤103). The description of the test cases follows.
A single line of each test case contains a single integern(2≤n≤107).
It is guaranteed that the sum ofnover all test cases does not exceed107.

## Output
For each test case, output the number of interesting ratiosF(a,b)for pairs satisfying1≤a<b≤n.