# Problem Description

At the IT Campus "NEIMARK", there are training sessions in competitive programming — both individual and team-based!
For the next team training session,nstudents will attend, and the skill of thei-th student is given by a positive integerai.
The coach considers a team strong if itsstrengthis at leastx. Thestrengthof a team is calculated as the number of team members multiplied by the minimum skill among the team members.
For example, if a team consists of4members with skills[5,3,6,8], then the team'sstrengthis4⋅min([5,3,6,8])=12.
Output the maximum possible number of strong teams, given that each team must have at least one participant and every participant must belong to exactly one team.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains two integersnandx(1≤n≤2⋅105,1≤x≤109) — the number of students in training and the minimumstrengthof a team to be considered strong.
The second line of each test case containsnintegersai(1≤ai≤109) — the skill of each student.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output the maximum possible number of teams withstrengthat leastx.