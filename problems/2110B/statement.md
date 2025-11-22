# Problem Description

In 2077, robots decided to get rid of balanced bracket sequences once and for all!
A bracket sequence is calledbalancedif it can be constructed by the following formal grammar.
You are the head of the department for combating balanced bracket sequences, and your main task is to determine which brackets you can destroy and which you cannot.
You are given a balanced bracket sequence represented by a strings, consisting of the characters(and). Since the robots' capabilities are not limitless, they can removeexactlyone opening bracket andexactlyone closing bracket from the string.
Your task is to determine whether the robots can delete such two brackets so that the stringsis no longer a balanced bracket sequence.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
Each test case consists of a single strings(2≤|s|≤2⋅105) — a sequence of the characters(and).
It is guaranteed thatsis a balanced bracket sequence.
It is also guaranteed that the sum of|s|across all test cases does not exceed2⋅105.

## Output
For each test case, output "YES" if the robots can make the string stop being a balanced bracket sequence, and "NO" otherwise.
You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.