# Problem Description

Monocarp has $$$n$$$ pizzas, the $$$i$$$-th pizza consists of $$$a_i$$$ slices. Pizzas are denoted by uppercase Latin letters fromAto the $$$n$$$-th letter of the Latin alphabet.
Monocarp also has $$$m$$$ friends, and he wants to inviteexactly twoof them to eat pizza. For each friend, Monocarp knows which pizzas that friend likes.
After the friends arrive at Monocarp's house, for each pizza, the following happens:
For each $$$k$$$ from $$$0$$$ to $$$\sum a_i$$$, calculate the number of ways to chooseexactly two friendsto invite so that the friends don't quarrel, and Monocarp eats exactly $$$k$$$ slices.

## Input
The first line contains two integers $$$n$$$ and $$$m$$$ ($$$1 \le n \le 20$$$; $$$2 \le m \le 5 \cdot 10^5$$$) — the number of pizzas and the number of friends, respectively.
The second line contains $$$m$$$ strings $$$s_1, s_2, \dots, s_m$$$ ($$$1 \le |s_i| \le n$$$), where $$$s_i$$$ is a string consisting ofdistinctcharacters fromAto the $$$n$$$-th letter of the Latin alphabet, denoting which pizzas the $$$i$$$-th friend likes. In every string $$$s_i$$$, the characters are sorted in lexicographical (alphabetic) order.
The third line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 2 \cdot 10^4$$$) — the sizes of the pizzas.

## Output
Print $$$\sum a_i + 1$$$ integers, where the $$$k$$$-th integer (starting from $$$0$$$) should be the number of ways to chooseexactly two friendsto invite so that the friends don't quarrel, and Monocarp eats exactly $$$k$$$ slices.