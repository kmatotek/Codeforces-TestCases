# Problem Description

Ivan, Dmitrii, and Pjotr are celebrating Ivan's birthday at an amusement park with $$$n$$$ attractions. The $$$i$$$-th attraction operates at minutes $$$a_i, 2a_i, 3a_i, \dots$$$ (i.e., every $$$a_i$$$ minutes).
Each minute, the friends can either ride exactly one available attractiontogetheror wait. Since the rides are very short, they can board another attraction the next minute. They may ride the attractions in any order.
They want to experience each ride exactly once before heading off to enjoy the birthday cake. What is the earliest time by which they can finish all $$$n$$$ attractions?

## Input
Each test contains multiple test cases. The first line contains an integer $$$t$$$ ($$$1\le t\le 2000$$$) — the number of test cases. The descriptions of the $$$t$$$ test cases follow.
The first line contains an integer $$$n$$$ ($$$1\le n \le 2000$$$) — the number of attractions.
The second line contains $$$n$$$ integers $$$a_1,\, a_2,\,\ldots,\, a_n$$$ ($$$1 \le a_i \le 10^9$$$) — the values determining when the various attractions operate.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2000$$$.

## Output
For each test case, print the earliest time the three friends can finish all $$$n$$$ attractions.