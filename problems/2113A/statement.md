# Problem Description

You are the owner of a popular shashlik restaurant, and your grill is the heart of your kitchen. However, the grill has a peculiarity: after cooking each shashlik, its temperature drops.
You need to cook as many portions of shashlik as possible, and you have an unlimited number of portions of two types available for cooking:
Initially, the grill's temperature is $$$k$$$ degrees. Determine the maximum total number of portions of shashlik that can be cooked.
Note that the grill's temperature can be negative.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The only line of each test case contains five integers $$$k$$$, $$$a$$$, $$$b$$$, $$$x$$$, and $$$y$$$ ($$$1 \le k, a, b, x, y \le 10^9$$$) — the initial temperature of the grill, the required temperature for cooking the first and second types of shashlik, respectively, as well as the temperature drop after cooking the first and second types of shashlik, respectively.

## Output
For each test case, output a single integer — the maximum number of portions of shashlik that you can cook.