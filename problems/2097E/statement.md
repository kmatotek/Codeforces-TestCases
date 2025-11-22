# Problem Description

Boy Vasya loves to travel very much. In particular, flying in airplanes brings him extraordinary pleasure. He was about to fly to another city, but the runway was heavily covered with snow and needed to be cleared.
The runway can be represented asnconsecutive sections numbered from1ton. The snowstorm was quite strong, but it has already stopped, so Vasya managed to calculate that thei-th section is covered withaimeters of snow. For such situations, the airport has a snowplow that works in a rather unusual way. In one minute, the snowplow can do the following:
Formally, one can choose1≤l≤r≤n(r−l+1≤d). After that,c=max{al,al+1,…,ar}is calculated, and ifc>0, then for alli:l≤i≤rsuch thatai=c, the value ofaiis decreased by one.
Vasya has been preparing for the flight for a long time and wants to understand how much time he has left to wait until all sections are completely cleared of snow. In other words, it is required to calculate the minimum number of minutes that the snowplow will need to achieveai=0for allifrom1ton.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤2⋅105). The description of the test cases follows.
The first line of each test case contains two integersnandd(1≤n≤5⋅105,1≤d≤n) — the number of sections on the runway and the maximum length of the segment that the snowplow can choose.
The second line of each test case containsnintegersa1,a2,…,an(1≤ai≤109), whereaiis the number of meters of snow on thei-th section.
It is guaranteed that the sum ofnover all test cases does not exceed5⋅105.

## Output
For each test case, output a single integer — the minimum number of minutes required for the snowplow to achieveai=0for allifrom1ton.