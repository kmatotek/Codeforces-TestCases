# Problem Description


Steve's creeper farm has overflowed and there are creepers everywhere! There are $$$n$$$ creepers standing in a line, with the $$$i$$$-th creeper having explosive power $$$e_i$$$. Steve needs to kill all of them in order to get past.
To do this, he can use his trusty Flint and Steel todetonatecreepers. Detonating the creeper at position $$$i$$$ kills all creepers at positions $$$j$$$ such that $$$|i - j| < e_i$$$. Dead creepers cannot be detonated. Some creepers may be particularly weak and have explosive power $$$0$$$, meaning they cannot be detonated either.
With the Great Hog hot on his tail, there is no time to waste. Find a sequence of detonations that kills all the creepers with as few detonations as possible, or report it is impossible.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$2 \le n \le 5 \cdot 10^5$$$) — the number of creepers.
The second line of each test case contains $$$n$$$ integers $$$e_1, e_2,\ldots, e_n$$$ ($$$0 \le e_i \le n$$$) — the explosive power of each creeper.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$5 \cdot 10^5$$$.

## Output
For each test case, output $$$-1$$$ if it is impossible to kill all the creepers.
Otherwise, output two lines. On the first line, output a single integer $$$k$$$ ($$$1 \leq k \leq n$$$), the minimum number of detonations needed. Then output a line with $$$k$$$ integers $$$d_1, d_2, \ldots, d_k$$$ ($$$1 \leq d_i \leq n$$$), stating the sequence of creepers to detonate.
If there are multiple solutions, you can print any of them.