# Problem Description


This is an interactive problem. Refer to the Interaction section below for better understanding.
There are $$$n$$$ ($$$2 \le n \le 40$$$) batteries numbered $$$1, 2, \ldots, n$$$. Some of them work while the others don't. Let $$$a$$$ be the number of batteries that work. It is guaranteed that $$$\mathbf{a \geq 2}$$$.
You are given $$$n$$$ butnot$$$a$$$.
There is a flashlight which can hold two batteries and it only turns on when both batteries work. The batteries have been shuffled and you don't know which ones work and which ones don't. You can choose two batteries and try them in the flashlight.
You want to find a pair of batteries that work. However, you are worried about breaking the flashlight, so you want to limit the amount of trials you attempt.
Therefore, you should find a pair of working batteries using at most $$$\left \lfloor \frac{n^2}{a} \right \rfloor$$$ trials.
The interactor isadaptive. This means that whether battery $$$i$$$ ($$$1 \le i \le n$$$) works is not fixed and may change during the interaction. However, it is guaranteed that there exists a configuration of $$$a$$$ working batteries that is consistent with the information that you have received so far.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 50$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$2 \le n \le 40$$$) — the number of batteries.
It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$200$$$.
