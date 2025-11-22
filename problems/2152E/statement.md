# Problem Description


This is an interactive problem.
Faker is being naughty again. You asked him to create a nice query problem, but he created an interactive problem where he is answering a query instead! Faker hid a permutation from you, and you have to infer some interesting information by interacting with him.
You are given an integer $$$n$$$. Faker hid a hidden permutation$$$^{\text{∗}}$$$ $$$p_1, p_2, \ldots, p_{n^2+1}$$$ of length $$$n^2+1$$$. Your goal is to find a monotone subsequence (either increasing or decreasing) of the hidden permutation, with length exactly $$$n+1$$$. It can be proved that every permutation of length $$$n^2 + 1$$$ contains a monotone subsequence of length $$$n+1$$$. For more information about the proof, you can check outthis Wikipedia page.
To find it, you can make at most $$$n$$$skyscraper queriesto the interactor, which is defined as follows:
After making at most $$$n$$$ queries, you must report a valid monotone subsequence of lengthexactly$$$n+1$$$.
Note that the permutation $$$p$$$ is fixedbeforeany queries are made and does not depend on the queries.
$$$^{\text{∗}}$$$A permutation of length $$$m$$$ is an array consisting of $$$m$$$ distinct integers from $$$1$$$ to $$$m$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$m=3$$$ but there is $$$4$$$ in the array).

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 5000$$$). The description of the test cases follows.
The first and only line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 100$$$).
It is guaranteed that the sum of $$$n^2+1$$$ over all test cases does not exceed $$$10\,001$$$.
