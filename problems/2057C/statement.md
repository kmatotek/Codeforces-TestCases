# Problem Description

In the upcoming year, there will be many team olympiads, so the teachers of "T-generation" need to assemble a team of three pupils to participate in them. Any three pupils will show a worthy result in any team olympiad. But winning the olympiad is only half the battle; first, you need to get there...
Each pupil has an independence level, expressed as an integer. In "T-generation", there is exactly one student with each independence levels fromltor, inclusive. For a team of three pupils with independence levelsa,b, andc, the value of their team independence is equal to(a⊕b)+(b⊕c)+(a⊕c), where⊕denotes thebitwise XOR operation.
Your task is to choose any trio of students with the maximum possible team independence.

## Input
Each test contains multiple test cases. The first line contains a single integert(1≤t≤104) — the number of test cases. The description of the test cases follows.
The first line of each test case set contains two integerslandr(0≤l,r<230,r−l>1) — the minimum and maximum independence levels of the students.

## Output
For each test case set, output three pairwise distinct integersa,b, andc, such thatl≤a,b,c≤rand the value of the expression(a⊕b)+(b⊕c)+(a⊕c)is maximized. If there are multiple triples with the maximum value, any of them can be output.