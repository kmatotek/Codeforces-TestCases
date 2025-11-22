# Problem Description

This problem is a run-twice (communication) problem.
Alice has an integer $$$x$$$ where $$$1 \le x \le 2^{15}$$$, which she needs to send to Bob (an astronaut on the Moon) as it is an important parameter for their secret project on the Moon.
Fortunately, Alice has a secret storage device $$$S$$$, which contains anot necessarily non-emptysubset of the set $$$\{1, 2, \ldots, 20\}$$$. She plans to send $$$S$$$ to Bob. Bob's goal is to recover the value of $$$x$$$ using only $$$S$$$.
However, after Alice sends set $$$S$$$ on a spaceship and before Bob receives $$$S$$$, magical butterflies had intercepted the spaceship! When Bob finally receives $$$S$$$, one of the following had occurred:
Please devise a strategy for Alice and Bob so that Bob can determine the value of $$$x$$$ regardless of what happened to set $$$S$$$. Precisely, in this problem your code will be run exactly two times on each test. On the first run, you will act as Alice, and on the second Bob. No additional information other than the set $$$S$$$ can be transferred from Alice to Bob. To get anAcceptedverdict, your code on the second run should be able to exactly recover the integers that were received on the first run.
First Run
Input
The first line of the input contains the stringfirst. The purpose of this is so your program recognizes that this is its first run, and it should act as Alice.
The second line of the input contains exactly one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.
The first and only line of the $$$i$$$-th test case contains an integer $$$x$$$ ($$$1 \le x \le 2^{15}$$$).
Output
For each test case, send $$$S$$$ to Bob by printing two lines in the following manner.
Exceptionally, you may omit the second line if $$$n=0$$$. You may output elements of $$$S$$$ in any order. However, they must be pairwise distinct.
Then, you will either proceed to the next test case, or your program must terminate if you have processed every test case.
Second Run
Input
The first line of the input contains the stringsecond. The purpose of this is so your program recognizes that this is its second run, and it should act as Bob.
The second line of the input contains exactly one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases. Note that this number is equal to $$$t$$$ from the first run input.
The first line of each test case contains an integer $$$n'$$$ ($$$0 \leq n' \leq 20$$$) — the size of the set $$$S'$$$ that Bob receives, that is, possiblymodified$$$S$$$.
The second line of each test case contains $$$n$$$ integers $$$S'_1, S'_2, \ldots, S'_n$$$ ($$$1 \leq S'_i \leq 20$$$) — the elements of the $$$S'$$$ that Bob receives.The elements of $$$S'$$$ are sorted in increasing order, even if the original $$$S$$$ is not sorted in increasing order.
Note that the test cases in the second run may be shuffled. Please see the example input for more details.
Output
For each test case, print a single line with the value of $$$x$$$ ($$$1 \leq x \leq 2^{15}$$$).

