# Problem Description

You are given a permutation$$$^{\text{∗}}$$$ $$$p$$$ of every integer from $$$1$$$ to $$$n$$$. You also own a binary$$$^{\text{†}}$$$ string $$$s$$$ of size $$$n$$$ where $$$s_i = \mathtt{0}$$$ for all $$$1 \le i \le n$$$. You may do the following operation at most $$$5$$$ times:
You are also given a binary string $$$x$$$ of size $$$n$$$. After performing operations, it must hold for every $$$1 \le i \le n$$$ that if $$$x_i = \mathtt{1}$$$, then $$$s_i = \mathtt{1}$$$. Note that if $$$x_i = \mathtt{0}$$$, then $$$s_i$$$ can haveanyvalue.
Figure out any sequence ofat most $$$5$$$operations such that the aforementioned condition is satisfied, or report that it is impossible to do so. Note that youdo nothave to minimize the number of operations you make.
$$$^{\text{∗}}$$$A permutation $$$p$$$ of every integer from $$$1$$$ to $$$n$$$ is a sequence of elements from $$$1$$$ to $$$n$$$ such that every element appears exactly once.
$$$^{\text{†}}$$$A string $$$b$$$ of size $$$m$$$ is considered binary if and only if $$$b_i = \mathtt{0}$$$ or $$$b_i = \mathtt{1}$$$ for all $$$1 \le i \le m$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$3 \le n \le 2 \cdot 10^5$$$) — the size of the array.
The second line contains exactly $$$n$$$ integers $$$p_1, p_2, \ldots, p_n$$$ ($$$1 \le p_i \le n$$$, the elements of $$$p$$$ are pairwise distinct) — where $$$p_i$$$ is the $$$i$$$-th element of the permutation.
The third line contains a single binary string $$$x$$$ of size $$$n$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, if it is impossible to perform operations such that the constraint is satisfied, output $$$-1$$$.
Otherwise, output an integer $$$0 \le k \le 5$$$, the number of operations. On the $$$i$$$-th of the next $$$k$$$ lines, output two integers $$$1 \le l_i \le r_i \le n$$$, the bounds of the $$$i$$$-th operation that is performed. If there are multiple correct solutions, output any of them.