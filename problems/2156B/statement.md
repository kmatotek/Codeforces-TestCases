# Problem Description


You are given $$$n$$$ machines arranged in a circle, where $$$n$$$ is at most $$$20$$$. Each machine is either of typeAor typeB. The machines are numbered clockwise from $$$1$$$ to $$$n$$$, and the type of the $$$i$$$-th machine is denoted by $$$s_i$$$. Each machine takes an integer $$$x$$$ and updates it according to its type:
You are given $$$q$$$ queries, each consisting of a single integer $$$a$$$. In each query, you start at machine $$$1$$$ holding an integer $$$a$$$. Each second, the following two actions occur in order:
This process continues until your integer $$$a$$$ becomes $$$0$$$. For each query, determine the number of seconds required for $$$a$$$ to reach $$$0$$$.
Note that all queries are independent of each other.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$q$$$ ($$$1\le n\le 20$$$, $$$1\le q\le 10^4$$$) — the number of machines, and the number of queries, respectively.
The second line of each test case contains a string $$$s$$$ ($$$|s| = n$$$ and $$$s_i = \mathtt{A} \text{ or }\mathtt{B}$$$) — the types of the machines.
The third line of each test case contains $$$q$$$ integers $$$a_1, a_2, \ldots, a_q$$$ ($$$1\le a_i\le 10^9$$$) — the initial integer of each query.
Note that there are no constraints on the sum of $$$n$$$ over all test cases.
It is guaranteed that the sum of $$$q$$$ over all test cases does not exceed $$$10^4$$$.

## Output
For each test case, output $$$q$$$ integers representing the answers to each query.