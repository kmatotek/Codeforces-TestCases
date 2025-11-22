# Problem Description

You are given three integers $$$a,b,c$$$.
Let $$$F(n)$$$ be the polynomial of degree $$$2n$$$ defined as follows.
$$$$$$F(n)=\left ({a x^2+b x+c}\right) ^n$$$$$$
You are asked to solve $$$q$$$ queries of the following kind.
However, it might be too easy for you if this problem ends here. So here is a twist$$$^{\text{†}}$$$: You are asked to solve the queriesonline.
$$$^{\text{∗}}$$$Here, $$$[x^a]F(n)$$$ denotes the coefficient of $$$x^a$$$ of the polynomial $$$F(n)$$$.
$$$^{\text{†}}$$$I hope it isn't too hard for you after the twist. Even a toddler knows one way to solve it. You just have to optimize that method by a factor of $$$8\,000\,000$$$.

## Input
The first line contains three integers $$$a$$$, $$$b$$$, $$$c$$$ ($$$1 \le a,b,c \le 10^9+6$$$).
The second line contains the number of queries $$$q$$$ ($$$1 \le q \le 3 \cdot 10^5$$$).
Each of the $$$q$$$ following lines contains two integers $$$n_i'$$$ and $$$k_i'$$$ denoting the query in encrypted format.
You must decrypt the queries as follows.
Do note thatboththe sum of $$$n_i$$$andthe sum of $$$k_i$$$ over all queriesare not bounded.

## Output
For each query, print the answer modulo $$$10^9+7$$$ on a new line.