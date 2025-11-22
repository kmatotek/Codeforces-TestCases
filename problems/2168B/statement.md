# Problem Description


This is a run-twice (communication) interactive problem.
There are two players: Player A and Player B. The jury (otherwise known as the interactor of this problem) will first interact with player A. After player A ends their interaction, the jury will interact with player B. Note that player A and player B may not directly pass information to each other; both players are only able to send information to or receive information from the jury.
Before the interaction, the jury determines an integer $$$n$$$ and a permutation $$$p$$$$$$^{\text{∗}}$$$ of the integers from $$$1$$$ to $$$n$$$ exactly once. These values are consistent across both players.
Player A receives the value of $$$n$$$ and all elements of $$$p$$$ from the jury. Then, Player A must send a binary integer $$$x$$$ (that is, $$$x$$$ must equal $$$0$$$ or $$$1$$$) back to the jury.
Player B receives the value of $$$n$$$ and the integer $$$x$$$ (the same integer that player A sent) from the jury. However, the permutation $$$p$$$ is not given to player B. Player B's task is to determine the position of integer $$$n$$$ in $$$p$$$. To do so, Player B can ask the jury at most $$$30$$$ queries in the following form:
Player A wants to ensure that player B can determine the position of $$$n$$$. Your task is to act as both players and determine an optimal interaction strategy for both players so that player B determines the position of $$$n$$$ correctly.
First Run
Your code will run exactly twice on each test. On the first run, you will be Player A.
Input
The first line of the input contains the stringfirst. The purpose of this is so your program recognizes that this is its first run, and it should act as Player A.
The second line of the input contains exactly one integer $$$t$$$ — the number of test cases ($$$1 \le t \le 100$$$).
The first line of the $$$i$$$-th test case contains an integer $$$n$$$ — the length of $$$p$$$ for the $$$i$$$-th test case ($$$2 \le n \le 10^4$$$).
The second line of the $$$i$$$-th test case contains $$$n$$$ space-separated integers $$$p_1, p_2, \ldots, p_n$$$. It is guaranteed this sequence forms a permutation.
It is guaranteed the sum of $$$n$$$ over all test cases does not exceed $$$10^4$$$.
Output
For each test case, print an integer $$$x$$$, either $$$0$$$ or $$$1$$$, on a new line. This is the integer that will be sent to you in the second run.
After this, proceed to the next test case, or you terminate your program if it was the last test case.
Second Run
On the second run, you are Player B.
Input
The first line of the input contains the stringsecond. The purpose of this is so your program recognizes that this is its second run, and it should act as Player B.
The second line of the input contains exactly one integer $$$t$$$ — the number of test cases ($$$1 \le t \le 100$$$). Note that this number is equal to $$$t$$$ from the first run input.
The first line of each test case contains two integers $$$n$$$ and $$$x$$$ ($$$2 \leq n \leq 10^4$$$, $$$0 \leq x \leq 1$$$). This denotes the length of $$$p$$$ and the binary integer $$$x$$$ that was sent by Player A from the last run.
Note that the test cases in the second run may be shuffled. Please see the example test case for further illustration.
Interaction
For the $$$i$$$-th test case, recall you will first receive $$$n$$$ and $$$x$$$ in the input from the jury according to the input format above. After receiving those inputs, you will be able to make at most $$$30$$$ queries of the following form (ignore quotes):
After each query, the jury will respond with $$$\max(p_{l}, p_{l+1}, \ldots, p_{r}) - \min(p_{l}, p_{l+1}, \ldots, p_{r})$$$, in which you should read through the input stream.
If your program makes more than $$$30$$$ queries, your program should immediately terminate to receive the verdictWrong Answer. Otherwise, you can get an arbitrary verdict because your solution will continue to read from a closed stream.
Once you are ready to report the position of $$$n$$$, you may do so in the following format:
Then, you will either proceed to the next test case, or your program must terminate if you have processed every test case.
The interactor isnotadaptive. That is, the permutation will not change during the interaction, and will always be the same permutation as shown to you in the first run.
After printing each query do not forget to output the end of line and flush$$$^{\text{†}}$$$ the output. Otherwise, you will getIdleness limit exceededverdict.
If, at any interaction step, you read $$$-1$$$ instead of valid data, your solution must exit immediately. This means that your solution will receiveWrong answerbecause of an invalid query or any other mistake. Failing to exit can result in an arbitrary verdict because your solution will continue to read from a closed stream.
$$$^{\text{∗}}$$$A permutation of length $$$n$$$ is an array consisting of $$$n$$$ distinct integers from $$$1$$$ to $$$n$$$ in arbitrary order. For example, $$$[2,3,1,5,4]$$$ is a permutation, but $$$[1,2,2]$$$ is not a permutation ($$$2$$$ appears twice in the array), and $$$[1,3,4]$$$ is also not a permutation ($$$n=3$$$ but there is $$$4$$$ in the array).
$$$^{\text{†}}$$$To flush, use:

