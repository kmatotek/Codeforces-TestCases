# Problem Description

You are given an array $$$a$$$ containing $$$n$$$ integers.
In one operation, you can choose some elements from this array and remove them. However, the elements you choose must meet one of the following conditions:
Note that if you choose only $$$1$$$ element to remove, it automatically meets these conditions.
For example, if $$$a = \{1, 2, 1, 1, 3\}$$$, some of the possible elements you can remove in one operation are:
However, you cannot choose the $$$2$$$-nd, the $$$3$$$-rd and the $$$4$$$-th element because the $$$2$$$-nd element is not equal to the $$$4$$$-th, but the $$$3$$$-rd element is equal to the $$$4$$$-th.
For each $$$x$$$ from $$$0$$$ to $$$n - 1$$$, you have to calculate the minimum number of operations required to decrease the size of the array toexactly$$$x$$$.

## Input
The first line contains one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
Each test case consists of two lines:
Additional constraint on the input: the sum of $$$n$$$ over all test cases does not exceed $$$3 \cdot 10^5$$$.

## Output
For each test case, print $$$n$$$ integers $$$c_0, c_1, \dots, c_{n-1}$$$, where $$$c_i$$$ is the minimum number of operations required to reduce the size of the array to exactly $$$i$$$.