# Problem Description

A new semester is about to begin, and it is necessary to create a schedule for the first day. There are a total ofngroups andmclassrooms in the faculty. It is also known that each group has exactly6classes on the first day, and thek-th class of each group takes place at the same time. Each class must be held in a classroom, and at the same time, there cannot be classes for more than one group in the same classroom.
Each classroom has its own index (at least three digits), and all digits of this index, except for the last two, indicate the floor on which the classroom is located. For example, classroom479is located on the4-th floor, while classroom31415is on the314-th floor. Between floors, one can move by stairs; for any floorx>1, one can either go down to floorx−1or go up to floorx+1; from the first floor, one can only go up to the second; from the floor107(which is the last one), it is possible to go only to the floor9999999.
The faculty's dean's office has decided to create the schedule in such a way that students move as much as possible between floors, meaning thatthe total number of movements between floors across all groups should be maximized. When the students move from one floor to another floor, they take the shortest path.
For example, if there aren=2groups andm=4classrooms[479,290,478,293], the schedule can be arranged as follows:
In such a schedule, the groups will move between the2nd and4th floors each time, resulting in a total of20movements between floors.
Help the dean's office create any suitable schedule!

## Input
Each test consists of several test cases. The first line contains a single integert(1≤t≤103) — the number of test cases. The description of the test cases follows.
The first line of each test case contains two integersnandm(1≤n≤m≤105) — the number of groups and the number of available classrooms.
The second line of each test case containsmintegersai(100≤ai<109) — the indices of the available classrooms.
Additional constraints on the input:

## Output
For each test case, outputnlines, where thei-th line should contain6integers — the indices of the classrooms where the classes for thei-th group will be held.
Each classroom must be occupied by at most one group during thek-th class.