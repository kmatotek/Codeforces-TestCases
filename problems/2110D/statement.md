# Problem Description

In 2077, when robots took over the world, they decided to compete in the following game.
There arencheckpoints, and thei-th checkpoint containsbibatteries. Initially, the Robot starts at the1-st checkpoint with no batteries and must reach then-th checkpoint.
There are a total ofmone-way passages between the checkpoints. Thei-th passage allows movement from pointsito pointti(si<ti), but not the other way. Additionally, thei-th passage can only be used if the robot has at leastwicharged batteries; otherwise, it will run out of power on the way.
When the robot arrives at pointv, it can additionally take any number of batteries from0tobv, inclusive. Moreover, it always carries all previously collected batteries, and at each checkpoint, it recharges all previously collected batteries.
Find the minimum number of batteries that the robot can have at the end of the journey, or report that it is impossible to reach from the first checkpoint to the last.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains two integersn,m(2≤n≤2⋅105,0≤m≤3⋅105) — the number of checkpoints and the number of passages, respectively.
The second line containsnnumbersbi(0≤bi≤109) — the number of batteries at thei-th checkpoint.
The nextmlines contain three integerssi,ti,wi(1≤si<ti≤n,1≤wi≤109) — the endpoints of the passage and the minimum number of batteries required to pass through it.
It is guaranteed that the sum ofndoes not exceed2⋅105.
It is guaranteed that the sum ofmdoes not exceed3⋅105.

## Output
For each test case, output the minimum number of batteries that you can have at the end of the journey, or−1if it is impossible to reach pointn.