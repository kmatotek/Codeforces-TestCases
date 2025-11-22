# Problem Description

We call a phone number abeautifulif it is a string of10digits, where thei-th digit from the left is at least10−i. That is, the first digit must be at least9, the second at least8,…, with the last digit being at least0.
For example,9988776655is a beautiful phone number, while9099999999is not, since the second digit, which is0, is less than8.
Vadim has abeautifulphone number. He wants to rearrange its digits in such a way that the result is thesmallest possible beautifulphone number. Help Vadim solve this problem.
Please note that the phone numbers are compared as integers.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The only line of each test case contains a single stringsof length10, consisting of digits. It is guaranteed thatsis abeautifulphone number.

## Output
For each test case, output a single string of length10— the smallest possible beautiful phone number that Vadim can obtain.