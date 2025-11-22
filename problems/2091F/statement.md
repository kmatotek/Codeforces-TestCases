# Problem Description

The visitors of the IT Campus "NEIMARK" are not only strong programmers but also physically robust individuals! Some practice swimming, some rowing, and some rock climbing!
Master Igor is a prominent figure in the local rock climbing community. One day, he went on a mountain hike to ascend one of the peaks. As an experienced climber, Igor decided not to follow the established trails but to use his skills to climb strictly vertically.
Igor found a rectangular vertical section of the mountain and mentally divided it intonhorizontal levels. He then split each level intomsegments using vertical partitions. Upon inspecting these segments, Igor discovered convenient protrusions that can be grasped (hereafter referred to asholds). Thus, the selected part of the mountain can be represented as ann×mrectangle, with some cells containing holds.
Being an experienced programmer, Igor decided to count the number of validroutes. A route is defined as a sequence ofdistinctholds. A route is considered valid if the following conditions are satisfied:
Igor's arm span isd, which means he can move from one hold to another if theEuclidean distancebetween the centers of the corresponding segments does not exceedd. The distance between sections (i1,j1) and (i2,j2) is given by√(i1−i2)2+(j1−j2)2.
Calculate the number of different valid routes. Two routes are considered different if they differ in the list of holds used or in the order in which these holds are visited.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤103). The description of the test cases follows.
The first line of each test case contains three integersn,m,d(2≤n≤2000,1≤m,d≤2000).
Each of the followingnlines containsmcharacters — the description of the corresponding level of the mountain. The symbol '#' represents an empty section, and the symbol 'X' represents a section with a hold. The levels are described from top to bottom.
It is guaranteed that the sum ofn⋅mover all test cases does not exceed4⋅106.

## Output
For each test case, output the number of different routes modulo998244353.