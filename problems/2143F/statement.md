# Problem Description


You have been gifted a magic sequence of integers: $$$a_1, a_2, \ldots, a_n$$$. However, this is no ordinary sequence — it can modify itself in a specific way!
After observing it carefully, you discovered the rule it follows:
Being afraid of strictly increasing sequences, you start asking yourself questions:
You are given $$$q$$$ queries. Each query consists of two integers $$$l$$$ and $$$r$$$, and you must determine whether the subarray $$$a_l, a_{l+1}, \ldots, a_r$$$ can be transformed into a strictly increasing sequence by applying any number of the described operations only within the range $$$l$$$ to $$$r$$$, that is,only using indices $$$l \le i \le j \le r$$$.
$$$^{\text{∗}}$$$$$$\oplus$$$ denotes thebitwise XOR operation.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line contains two integers $$$n$$$ and $$$q$$$ ($$$1 \leq n, q \leq 2 \cdot 10^5$$$) — the length of the sequence and the number of queries.
The second line contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \leq a_i < 2^{20}$$$) — the contents of the sequence.
Each of the next $$$q$$$ lines contains two integers $$$l$$$ and $$$r$$$ ($$$1 \leq l \leq r \leq n$$$), representing a query. For each query, you must determine whether the subarray $$$a_l, a_{l+1}, \ldots, a_r$$$ can be transformed into a strictly increasing sequence using the allowed operations.
It is guaranteed that the total sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$, and the total sum of $$$q$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each query, outputYESif the subarray $$$a_l, a_{l+1}, \ldots, a_r$$$ can be transformed into a strictly increasing sequence using the allowed operations; otherwise, outputNO.
You may print each letter ofYESorNOin any case. For example,YES,yES,YeSwill all be recognized as a positive answer.