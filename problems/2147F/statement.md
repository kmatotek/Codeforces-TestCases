# Problem Description

You are at a marketplace and there are two traders who are willing to trade on $$$n$$$ different items. Each trader is represented by a permutation that signifies the relative value of the $$$n$$$ items for that trader. Let's denote those two permutations $$$p$$$ and $$$s$$$. If you have an item $$$i$$$, you can trade it for an item $$$j$$$ if either $$$p_i > p_j$$$ (using the first trader) or $$$s_i > s_j$$$ (using the second trader).
We say that an item $$$i$$$ isat least as valuable asan item $$$j$$$ if you can come to the marketplace with item $$$i$$$, make some (possibly none) trades, and get item $$$j$$$. Note that at any moment, you will have exactly one item on hand. Assume that the traders have infinite supplies of any item.
Due to the never-ending updates in the market, traders will often reevaluate their views on the item values. You will be given $$$q$$$ queries; each is a swap in one of the permutations. After every update, you should print the number of pairs $$$(i, j)$$$ ($$$1 \le i, j \le n$$$) such that item $$$i$$$ is at least as valuable as item $$$j$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains two integers $$$n$$$ and $$$q$$$ ($$$2 \le n \le 10^5$$$, $$$1 \le q \le 10^5$$$).
The next two lines contain the initial permutations $$$p$$$ and $$$s$$$.
The following $$$q$$$ lines each contain three integers $$$tp$$$, $$$i$$$, $$$j$$$ ($$$tp \in \{ 1, 2 \}$$$, $$$1 \le i, j \le n$$$, $$$i \ne j$$$). If $$$tp=1$$$, swap $$$p_i$$$ with $$$p_j$$$. If $$$tp=2$$$, swap $$$s_i$$$ with $$$s_j$$$.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$10^5$$$, and the sum of $$$q$$$ over all test cases does not exceed $$$10^5$$$.

## Output
For each test case, output $$$q$$$ lines, the $$$k$$$-th of them containing a single integer — the number of pairs $$$(i, j)$$$ such that item $$$i$$$ is at least as valuable as item $$$j$$$ after the first $$$k$$$ updates.