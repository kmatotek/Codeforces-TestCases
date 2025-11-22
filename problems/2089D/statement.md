# Problem Description

In C++, the conditional operator?:is used as the value ofx?y:zisyifxis true; otherwise, the value isz.x,y, andzmay also be expressions. It is right-associated; that is,a?b:c?d:eis equivalent toa?b:(c?d:e).0means false and1means true.
Given a binary string with length2n+1, you need to show whether the value of the expression can be1after insertingnconditional operators into the string. You can use parentheses. For example, the string10101can be transformed into(1?0:1)?0:1, whose value is1.

## Input
The first line contains a single integert(1≤t≤10000), the number of test cases. The description of the test cases follows.
In the first line of each test case, there is a single integern(1≤n≤1.5⋅105).
In the second line of each test case, there is a binary string of length2n+1.
It is guaranteed that the sum ofnacross all test cases does not exceed1.5⋅105.

## Output
For each test case, on the first line, outputYesif the string can be transformed into an expression of value1; otherwise, outputNo.
If the answer isYes, output the expression on the second line. You can use parentheses, but the order of the characters in the original string must remain the same. The length of your expression must be no more than10n+1000.