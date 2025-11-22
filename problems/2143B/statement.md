# Problem Description

You want to buy $$$n$$$ products with prices $$$a_1, a_2, \ldots, a_n$$$. You can either:
You have $$$k$$$ discount vouchers with values $$$b_1, b_2, \ldots, b_k$$$. A voucher of value $$$x$$$ allows you to select exactly $$$x$$$ products and pay only for the $$$x - 1$$$ most expensive ones, as such, you can consider that the cheapest product in the group is free. Each product can be included inat most onediscount group, even if it is not the free one. Also, any single voucher can be used at most one single time.
What is theminimum total costrequired to purchase all $$$n$$$ products?

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le n, k \le 2 \cdot 10^5$$$) —the number of products and the number of available discount vouchers.
The second line contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \le a_i \le 10^9$$$) — the prices of the products.
The third line contains $$$k$$$ integers $$$b_1, b_2, \ldots, b_k$$$ ($$$1 \le b_i \le n$$$) — the values of the discount vouchers.
It is guaranteed that the sum of $$$n$$$ across all test cases does not exceed $$$2 \cdot 10^5$$$, and the sum of $$$k$$$ across all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
Print $$$t$$$ lines. The $$$i$$$-th line should contain the answer for the $$$i$$$-th test case — the minimum total cost required to purchase all products in that test case.