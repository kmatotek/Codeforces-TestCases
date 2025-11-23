# Problem Description

You have a sequence of $$$n$$$ time clocks arranged in a line, where the initial time on the $$$i$$$-th clock is $$$a_i$$$. In each second, the following happens in order:
Note that the above events happen in order. If the time of a clock reaches $$$0$$$ in a certain second, even if you can move to this clock and reset its time during that second, you will still lose.
You can start from any clock. Determine if it is possible to continue this process indefinitely without losing.

## Input
The first line of input contains a single integer $$$t$$$ ($$$1 \leq t \leq 10^4$$$) — the number of test cases.
For each test case, the first line contains a single integer $$$n$$$ ($$$2 \leq n \leq 5 \cdot 10^5$$$) — the number of time clocks.
The second line contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \leq a_i \leq 10^9$$$) — the initial times set on the clocks.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$5\cdot 10^5$$$.

## Output
For each test case, print "YES" (without quotes) if it is possible to continue this process indefinitely, or "NO" (without quotes) otherwise.
You can output "YES" and "NO" in any case (for example, strings "yEs", "yes" and "Yes" will be recognized as a positive response).