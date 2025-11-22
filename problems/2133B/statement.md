# Problem Description


Steve lives in a village with $$$n$$$ other villagers. Unfortunately, due to disputes over the distribution of emeralds, none of those villagers are friends with any other villager. Furthermore, villager $$$i$$$ initially has agrumpinessof $$$g_i$$$.
Steve can perform the following operation any number of times:
Steve wishes to make every villager friends with every other villager (possibly through some intermediate friendships); that is, from any villager, you can follow a path of friendships to reach any other villager. Since he does not want to inflate the village economy too much, calculate the minimum number of emeralds he must give away to accomplish this.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$2 \le n \le 2 \cdot 10^5$$$) — the number of villagers.
The second line of each test case contains $$$n$$$ integers $$$g_1, g_2,\ldots, g_n$$$ ($$$1 \le g_i \le 10^9$$$) — the initial grumpiness of each villager.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.

## Output
For each test case, output a single integer — the minimum number of emeralds Steve must give away to make everyone friends.