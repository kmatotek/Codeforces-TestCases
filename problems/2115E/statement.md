# Problem Description

May, Gellyfish's friend, loves playing a game called "Inscryption" which is played on a directed acyclic graph with $$$n$$$ vertices and $$$m$$$ edges. All edges $$$ a \rightarrow b$$$ satisfy $$$a<b$$$.
You start in vertex $$$1$$$ with some coins. You need to move from vertex $$$1$$$ to the vertex where the boss is located along the directed edges, and then fight with the final boss.
Each of the $$$n$$$ vertices of the graph contains a Trader who will sell you a card with power $$$w_i$$$ for $$$c_i$$$ coins. You can buy as many cards as you want from each Trader. However, you can only trade with the trader on the $$$i$$$-th vertex if you are currently on the $$$i$$$-th vertex.
In order to defeat the boss, you want the sum of the power of your cards to be as large as possible.
You will have to answer the following $$$q$$$ queries:

## Input
The first line of input contains two integers $$$n$$$ and $$$m$$$ ($$$1 \leq n \leq 200$$$, $$$n - 1 \leq m \leq \min(\frac {n(n-1)} 2, 2000)$$$) — the number of vertices and the number of edges.
The $$$i$$$-th of the following $$$n$$$ lines of input each contains two integers $$$c_i$$$ and $$$w_i$$$ ($$$1 \leq c_i \leq 200$$$, $$$1 \leq w_i \leq 10^9$$$) — describing the cards of the Trader on the $$$i$$$-th vertex.
In the following $$$m$$$ lines of input, each line contains two integers $$$u$$$ and $$$v$$$ ($$$1 \leq u < v \leq n$$$), indicating a directed edge from vertex $$$u$$$ to vertex $$$v$$$. It is guaranteed that every edge $$$(u,v)$$$ appears at most once.
The next line of input contains one single integer $$$q$$$ ($$$1 \leq q \leq 2 \cdot 10^5$$$) — the number of queries.
In the following $$$q$$$ lines of input, each line contains two integers $$$p$$$ and $$$r$$$ ($$$1 \leq p \leq n$$$, $$$1 \leq r \leq 10^9$$$).
It is guaranteed that for all $$$i$$$, there exists a path from vertex $$$1$$$ to vertex $$$i$$$.

## Output
For each query, output the answer to the query.