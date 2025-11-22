# Problem Description


You have an array $$$a$$$ of size $$$n$$$ — $$$a_1, a_2, \ldots a_n$$$.
You need to divide the $$$n$$$ elements into $$$2$$$ sequences $$$B$$$ and $$$C$$$, satisfying the following conditions:
$$$^{\text{∗}}$$$$$$\gcd(x, y)$$$ denotes thegreatest common divisor (GCD)of integers $$$x$$$ and $$$y$$$.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 500$$$). The description of the test cases follows.
The first line of each test case contains an integer $$$n$$$ ($$$2 \le n \le 100$$$).
The second line of each test case contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$1 \le a_i \le 10^4$$$).

## Output
For each test case, first output $$$\texttt{Yes}$$$ if a solution exists or $$$\texttt{No}$$$ if no solution exists. You may print each character in either case, for example $$$\texttt{YES}$$$ and $$$\texttt{yEs}$$$ will also be accepted.
Only when there is a solution, output $$$n$$$ integers on the second line. The $$$i$$$-th number should be either $$$1$$$ or $$$2$$$. $$$1$$$ represents that the element belongs to sequence $$$B$$$ and $$$2$$$ represents that the element belongs to sequence $$$C$$$.
You should guarantee that $$$1$$$ and $$$2$$$ both appear at least once.