# Problem Description

In anticipation of a duel with his old friend Fernan, Edmond is preparing an energy drink called "Mishkin Energizer". The drink consists of a stringsof lengthn, made up only of the charactersL,I, andT, which correspond to the content of three different substances in the drink.
We call the drinkbalancedif it contains an equal number of all substances. To boost his aura and ensure victory in the duel, Edmond must make the initial string balanced by applying the following operation:
Help Edmond make the drink balanced and win the duel by performingno more than2noperations. If there are multiple solutions, any one of them can be output. If it is impossible, you must report this.

## Input
Each test consists of several test cases. The first line of the input data contains one integert(1≤t≤100) — the number of test cases. The description of the test cases follows.
The first line of each test case contains one integern(1≤n≤100) — the length of the strings.
The second line of each test case contains a stringsof lengthn, consisting only of the charactersL,I, andT.

## Output
For each test case, output−1if there is no solution. Otherwise, in the first line, output a single integerm(0≤m≤2n) — the number of operations you performed.
Then thel-th of the followingmlines should contain a single integeri(1≤i<n+l−1), indicating the operation of inserting a character betweensiandsi+1. It must hold thatsi≠si+1.
If there are multiple solutions, any one of them can be output. Note that you do not need to minimize the number of operations in this problem.