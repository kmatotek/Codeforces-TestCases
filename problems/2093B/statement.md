# Problem Description

The cost of a positive integernis defined as the result of dividing the numbernby the sum of its digits.
For example, the cost of the number104is1041+0+4=20.8, and the cost of the number111is1111+1+1=37.
You are given a positive integernthat does not contain leading zeros. You can remove any number of digits from the numbern(including none) so that the remaining number contains at least one digit andis strictly greater than zero. The remaining digitscannotbe rearranged. As a result, youmayend up with a number that has leading zeros.
For example, you are given the number103554. If you decide to remove the digits1,4, and one digit5, you will end up with the number035, whose cost is0350+3+5=4.375.
What is the minimum number of digits you need to remove from the number so that its cost becomes the minimum possible?

## Input
The first line contains an integert(1≤t≤1000) — the number of test cases.
The only line of each test case contains a positive integern(1≤n<10100) without leading zeros.

## Output
For each test case, output one integer on a new line — the number of digits that need to be removed from the number so that its cost becomes minimal.