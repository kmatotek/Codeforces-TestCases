# Problem Description

Isamatdin has $$$n$$$ toys arranged in a row. The $$$i$$$-th toy has an integer $$$a_i$$$. He wanted to sort them because otherwise, his mother would scold him.
However, Isamatdin never liked arranging toys in order, so his friend JahonaliX gave him a magic wand to help. Unfortunately, JahonaliX made a small mistake while creating the wand.
But Isamatdin couldn't wait any longer and decided to use the broken wand anyway. The wand can only swap two toys if their integers havedifferent parity(one is even, the other is odd). In other words, you can swap toys in positions $$$(i, j)$$$ only if $$$a_i \bmod 2 \neq a_j \bmod 2$$$, where $$$\bmod$$$ — is the remainder of integer division.
Now he wants to know thelexicographically smallest$$$^{\text{∗}}$$$ arrangement he can achieve using this broken wand.
$$$^{\text{∗}}$$$A sequence $$$p$$$ islexicographically smallerthan a sequence $$$q$$$ if there exists an index $$$i$$$ such that $$$p_j = q_j$$$ for all $$$j < i$$$, and $$$p_i < q_i$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 2 \cdot 10^5$$$) — the number of toys.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^9$$$) — the integers of the toys.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output $$$n$$$ integers — the lexicographically smallest sequence that can be obtained using the described operation.