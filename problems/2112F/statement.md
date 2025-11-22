# Problem Description

There are $$$n$$$ variables; let's denote the value of the $$$i$$$-th variable as $$$a_i$$$.
There are also $$$m$$$ operations which will be applied to these variables; the $$$i$$$-th operation is described by three integers $$$x_i, y_i, z_i$$$. When the $$$i$$$-th operation is applied, the variable $$$x_i$$$ gets assigned the following value: $$$\min(a_{x_i}, a_{y_i} + z_i)$$$.
Every operation will be appliedexactly once, but their order is not fixed; they can be applied in any order.
Let's call a sequence of initial variable values $$$a_1, a_2, \dots, a_n$$$stable, if no matter in which order we apply operations, the resulting values will be the same. If the resulting value of the $$$i$$$-th variable depends on the order of operations, then the sequence of initial variable values is called $$$i$$$-unstable.
You have to process $$$q$$$ queries. In each query, you will be given initial values $$$a_1, a_2, \dots, a_n$$$ and an integer $$$k$$$; before applying the operations, you can at most $$$k$$$ times choose a variable and decrease it by $$$1$$$. For every variable $$$i$$$, you have to independently determine if it is possible to transform the given values into an $$$i$$$-unstable sequence.

## Input
The first line contains two integers $$$n$$$ and $$$m$$$ ($$$2 \le n \le 500$$$; $$$1 \le m \le 4 \cdot 10^5$$$) — the number of variables and operations, respectively.
Then, $$$m$$$ lines follow. The $$$i$$$-th of them contains three integers $$$x_i, y_i, z_i$$$ ($$$1 \le x_i, y_i \le n$$$; $$$x_i \ne y_i$$$; $$$0 \le z_i \le 10^5$$$) — the description of the $$$i$$$-th operation.
The next line contains one integer $$$q$$$ ($$$1 \le q \le 1000$$$) — the number of queries.
Each query consists of two lines:

## Output
For each query, print a string of $$$n$$$ zeroes and/or ones. The $$$i$$$-th character should be1if it is possible to obtain an $$$i$$$-unstable sequence, or0otherwise.