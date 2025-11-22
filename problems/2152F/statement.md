# Problem Description


Zeus is analyzing a replay of the fight to understand his opponent's attack patterns. The opponent has a special ability: if they land three attacks on a target within a time frame of $$$z$$$, their third attack becomes a powerful, boosted attack.
To outplay his opponent, Zeus should not let his opponent trigger their boosted attack. Let $$$Y = \{y_1, y_2, \ldots, y_m\}$$$ be the multiset of $$$m$$$ timestamps, where each $$$y_i$$$ represents the time when the opponent's attack landed. We call $$$Y$$$ to besafeif for every three timestamps $$$\{y_i, y_j, y_k\}$$$ such that $$$1 \le i < j < k \le m$$$, it holds that $$$\max(y_i, y_j, y_k) - \min(y_i, y_j, y_k) > z$$$, where $$$z$$$ is the duration of the time frame that is given to you as an input.
Zeus has a log of $$$n$$$ timestamps, $$$x_1, x_2, \ldots, x_n$$$, representing when the opponent's attacks landed. The timestamps aresorted in nondecreasing orderof occurrence. In other words, $$$x_i \le x_{i+1}$$$ for all $$$1 \le i < n$$$.
Zeus has $$$q$$$ intervals of interest, denoted as two integers $$$1 \le l \le r \le n$$$. For each interval, Zeus wants to find the maximum number of attacks among $$$[x_l, x_{l+1}, \ldots, x_r]$$$ that he could have let through: In other words, Zeus wants to find a maximum size subset of the multiset $$$\{x_l, x_{l+1}, \ldots, x_r\}$$$ such that the subset issafe.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 20\,000$$$). The description of the test cases follows.
The first line contains two integers $$$n$$$ and $$$z$$$ ($$$1 \le n \le 250\,000$$$, $$$1 \le z \le 10^9$$$).
The second line contains $$$n$$$ integers $$$x_1, x_2, \ldots, x_n$$$ ($$$1 \le x_i \le 10^9$$$) — the timestamps of the opponent's attacks. It is guaranteed that the array $$$x$$$ is sorted, i.e., $$$x_i \le x_{i+1}$$$ for all $$$1 \le i < n$$$.
The third line contains a single integer $$$q$$$ ($$$1 \le q \le 250\,000$$$).
The next $$$q$$$ lines each contain two integers $$$l$$$ and $$$r$$$ ($$$1 \le l \le r \le n$$$) — the endpoints of the interval.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$250\,000$$$.
It is guaranteed that the sum of $$$q$$$ over all test cases does not exceed $$$250\,000$$$.

## Output
For each of the $$$q$$$ queries, print a single integer — the maximum size of a safe subset of attack timestamps in the given interval.