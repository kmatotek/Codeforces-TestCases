# Problem Description

Wolf has found $$$n$$$ sheep with tastiness values $$$p_1, p_2, ..., p_n$$$ where $$$p$$$ is a permutation$$$^{\text{∗}}$$$. Wolf wants to perform binary search on $$$p$$$ to find the sheep with tastiness of $$$k$$$, but $$$p$$$ may not necessarily be sorted. The success of binary search on the range $$$[l, r]$$$ for $$$k$$$ is represented as $$$f(l, r, k)$$$, which is defined as follows:
If $$$l > r$$$, then $$$f(l, r, k)$$$ fails. Otherwise, let $$$m = \lfloor\frac{l + r}{2}\rfloor$$$, and:
Cow the Nerd decides to help Wolf out. Cow the Nerd is given $$$q$$$ queries, each consisting of three integers $$$l$$$, $$$r$$$, and $$$k$$$. Before the search begins, Cow the Nerd may choose a non-negative integer $$$d$$$, and $$$d$$$ indices $$$1 \le i_1 < i_2 < \ldots < i_d \le n$$$ where $$$p_{i_j} \neq k$$$ over all $$$1 \leq j \leq d$$$. Then, he may re-order the elements $$$p_{i_1}, p_{i_2}, ..., p_{i_d}$$$ however he likes.
For each query, output theminimuminteger $$$d$$$ that Cow the Nerd must choose so that $$$f(l, r, k)$$$ can besuccessful, or report that it is impossible. Note that the queries are independent and the reordering is not actually performed.
$$$^{\text{∗}}$$$A permutation of length $$$n$$$ is an array that contains every integer from $$$1$$$ to $$$n$$$ exactly once.

## Input
The first line of the input contains a single integer $$$t$$$ $$$(1 \le t \le 10^4)$$$ — the number of test cases.
The first line of each test contains two integers $$$n$$$ and $$$q$$$ $$$(1 \le n, q \le 2 \cdot 10^5)$$$ — the length of $$$p$$$ and the number of queries respectively.
The second line contains $$$n$$$ integers $$$p_1, p_2, ..., p_n$$$ — the tastiness of the $$$i$$$-th sheep. It is guaranteed that every integer from $$$1$$$ to $$$n$$$ appears exactly once in $$$p$$$.
The following $$$q$$$ lines contain three integers $$$l$$$, $$$r$$$, and $$$k$$$ $$$(1 \le l \le r \le n, 1 \le k \le n)$$$ — the range that the binary search will be performed on and the integer being searched for each query.
It is guaranteed that the sum of $$$n$$$ and the sum of $$$q$$$ over all cases do not exceed $$$2 \cdot 10^5$$$.

## Output
For each query, output the minimum integer $$$d$$$ that Cow the Nerd must choose so that $$$f(l, r, k)$$$ is successful on a new line. If it is impossible, output $$$-1$$$.