# Problem Description

Ecrade has ann×mgrid, originally empty, and he has pushed several (possibly, zero) balls in it.
Each time, he can push one ball into the grid either from the leftmost edge of a particular row or the topmost edge of a particular column of the grid.
When a ball moves towards a position:
Note that if a row or column is full (i.e., all positions in that row or column have balls), he cannot push a ball into that row or column.
Given the final state of whether there is a ball at each position of the grid, you need to determine whether it is possible for Ecrade to push the balls to reach the final state.

## Input
The first line contains an integert(1≤t≤10000) — the number of test cases. The description of the test cases follows.
The first line of each test case contains two integersnandm(1≤n,m≤50).
This is followed bynlines, each containing exactlymcharacters and consisting only of0and1, describing the final state of the grid. There is a ball at one position of the grid if and only if the corresponding position of the given input is1.
It is guaranteed that the sum ofn⋅mover all test cases does not exceed10000.

## Output
For each test case, output "Yes" (without quotes) if it is possible for Ecrade to push the balls to reach the final state, and "No" (without quotes) otherwise.
You can output "Yes" and "No" in any case (for example, strings "YES", "yEs" and "yes" will be recognized as a positive response).