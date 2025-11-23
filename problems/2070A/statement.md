# Problem Description

FizzBuzz is one of the most well-known problems from coding interviews. In this problem, we will consider a remixed version of FizzBuzz:
Given an integer $$$n$$$, process all integers from $$$0$$$ to $$$n$$$. For every integer such that its remainders modulo $$$3$$$ and modulo $$$5$$$ are the same (so, for every integer $$$i$$$ such that $$$i \bmod 3 = i \bmod 5$$$), printFizzBuzz.
However, you don't have to solve it. Instead, given the integer $$$n$$$, you have to report how many times the correct solution to that problem will printFizzBuzz.

## Input
The first line contains one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
Each test case contains one line consisting of one integer $$$n$$$ ($$$0 \le n \le 10^9$$$).

## Output
For each test case, print one integer — the number of times the correct solution will printFizzBuzzwith the given value of $$$n$$$.