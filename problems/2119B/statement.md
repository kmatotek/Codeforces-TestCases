# Problem Description

You are given two points $$$(p_x,p_y)$$$ and $$$(q_x,q_y)$$$ on a Euclidean plane.
You start at the starting point $$$(p_x,p_y)$$$ and will perform $$$n$$$ operations. In the $$$i$$$-th operation, youmustchoose any point such that the Euclidean distance$$$^{\text{∗}}$$$ between your current position and the point isexactly$$$a_i$$$, and then move to that point.
Determine whether it is possible to reach the terminal point $$$(q_x,q_y)$$$ after performing all operations.
$$$^{\text{∗}}$$$The Euclidean distance between $$$(x_1, y_1)$$$ and $$$(x_2, y_2)$$$ is $$$\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$$

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$1\leq n \leq 10^3$$$) — the length of the sequence $$$a$$$.
The second line of each test case contains four integers $$$p_x,p_y,q_x,q_y$$$ ($$$1\leq p_x,p_y,q_x,q_y\leq 10^7$$$) — the coordinates of the starting point and terminal point.
The third line of each test case contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$1 \le a_i \le 10^4$$$) — the distance to move in each operation.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2\cdot 10^5$$$.

## Output
For each test case, output "Yes" if it is possible to reach the terminal point $$$(q_x,q_y)$$$ after all operations; otherwise, output "No".
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.