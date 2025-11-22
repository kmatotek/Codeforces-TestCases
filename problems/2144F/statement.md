# Problem Description

A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic sequence. For example:
You are given $$$n$$$ bracket sequences $$$s_1, s_2, \dots, s_n$$$ (not necessarily regular) and an even integer $$$k$$$. Your task is to split all of them into groups in such a way that:
What is the smallest number of groups that this can be achieved for? If it's impossible to do for any number of groups, report so. Otherwise, print the groups and any valid regular bracket sequence for each group. If there are multiple answers with the smallest number of groups, print any of them.

## Input
The first line contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le n \le 50$$$; $$$2 \le k \le 50$$$; $$$k$$$ is even).
The $$$i$$$-th of the next $$$n$$$ lines contains a bracket sequence $$$s_i$$$ ($$$2 \le |s_i| \le k$$$). It consists only of characters '(' and ')'.

## Output
If it's impossible to split all bracket sequences into groups according to the rules, then print $$$-1$$$.
Otherwise, print the smallest possible number of groups $$$m$$$ in the first line. Then, $$$m$$$ blocks of data should follow:
None of these bracket sequences should be a substring of the chosen regular bracket sequence. Each index from $$$1$$$ to $$$n$$$ should belong to exactly one group.
If there are multiple answers with the smallest $$$m$$$, print any of them.