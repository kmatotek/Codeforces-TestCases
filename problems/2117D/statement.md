# Problem Description

Yousef wants to explode an array $$$a_1, a_2, \dots, a_n$$$. An array gets exploded when all of its elements become equal to zero.
In one operation, Yousef can doexactlyone of the following:
Your task is to help Yousef determine if it is possible to explode the array using any number of operations.

## Input
The first line of the input contains an integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first line of each test case contains an integer $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$) — the size of the array.
The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^9$$$) — the elements of the array.
It is guaranteed that the sum of $$$n$$$ over all test cases doesn't exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, print "YES" if Yousef can explode the array, otherwise output "NO".
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.