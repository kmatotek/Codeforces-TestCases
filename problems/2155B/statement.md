# Problem Description


Abraham is a brave explorer who goes where no other programmer has gone before. For his next expedition, he plans to investigate a peculiar maze. He knows that the maze is an $$$n \times n$$$ grid with an arrow in each cell that points in one of four directions: up, down, left and right. Abraham also knows that if he stands on an arrow, he will be forced to follow the arrows starting from that cell. Each arrow moves Abraham exactly $$$1$$$ cell in the direction that it is pointing. If he reaches an arrow that points towards the outside of the maze, Abraham will escape the maze.
Abraham doesn't know how the arrows are arranged, so he wants to plan for multiple scenarios. He tasks you with finding an arrangement of arrows in the grid such that there are exactly $$$k$$$ starting cells from which he can escape the maze.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 1000$$$). The description of the test cases follows.
The only line of each test case contains two integers $$$n$$$, $$$k$$$ ($$$2 \le n \le 100$$$, $$$0 \le k \le n^2$$$) — the size of the grid and the number of cells from which Abraham should be able to escape.
It is guaranteed that the sum of $$$n^2$$$ over all test cases does not exceed $$$10^5$$$.

## Output
For each test case, do one of the following:
If there are multiple solutions, print any of them.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.