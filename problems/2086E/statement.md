# Problem Description

We call a positive integerzebra-likeif its binary representation has alternating bits up to the most significant bit, and the least significant bit is equal to1. For example, the numbers1,5, and21arezebra-like, as their binary representations1,101, and10101meet the requirements, while the number10is notzebra-like, as the least significant bit of its binary representation1010is0.
We define thezebra valueof a positive integer𝑒as the minimum integer𝑝such that𝑒can be expressed as the sum of𝑝zebra-likenumbers (possibly the same, possibly different)
Given three integers𝑙,𝑟, and𝑘, calculate the number of integers𝑥such that𝑙≤𝑥≤𝑟and thezebra valueof𝑥equals𝑘.

## Input
Each test consists of several test cases. The first line contains a single integer𝑡(1≤𝑡≤100) — the number of test cases. The description of test cases follows.
The only line of each test case contains three integers𝑙,𝑟(1≤𝑙≤𝑟≤1018) and𝑘(1≤𝑘≤1018).

## Output
For each test case, output a single integer — the number of integers in[𝑙,𝑟]withzebra value𝑘.