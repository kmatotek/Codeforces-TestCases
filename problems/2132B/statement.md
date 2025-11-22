# Problem Description

Vadim has thought of a number $$$x$$$. To ensure that no one can guess it, he appended a positive number of zeros to the right of it, thus obtaining a new number $$$y$$$. However, as a precaution, Vadim decided to spread the number $$$n = x + y$$$. Find all suitable $$$x$$$ that Vadim could have thought of for the given $$$n$$$.

## Input
Each test consists of several test cases. The first line contains a single integer $$$t$$$ $$$(1 \le t \le 10^4)$$$ — the number of test cases. The following lines describe the test cases.
In a single line of each test case, there is an integer $$$n$$$ — the number spread by Vadim $$$(11 \le n \le 10^{18})$$$.

## Output
For each number $$$n$$$, output $$$0$$$ if there are no suitable $$$x$$$. Otherwise, output the number of suitable $$$x$$$, followed by all suitable $$$x$$$in ascending order.