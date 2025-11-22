# Problem Description

You are given a ropenunits long, where each unit is painted either red or black. The rope can be represented as a string of lengthnconsisting of charactersR(red) andB(black). You are also given two integersmandk.
You may perform the following operationat mostmtimes (possibly, zero times):
For example, consider the ropeRRRRBRRRwithk=4. If you choose the3-rd to6-th characters (RRRRBRRR), then after flipping, the rope becomesRRBBRBRR.
Define thenumber of color segmentsas the smallest number of contiguous segments into which the rope can be divided so that each segment consists of units of a single color. For instance, the ropeRRBRRRBBhas4color segments:RR,B,RRR, andBB.
Your task is to determine the maximum possible number of color segments after performingat mostmoperations.
∗A stringtis a substring of a stringsiftcan be obtained fromsby the deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

## Input
The first line contains three integersn,m, andk, representing the length of the rope, the maximum number of operations allowed, and the length of each operation's flip window, respectively.
The second line contains a string of lengthnconsisting only of the charactersRandB, representing the initial content of the rope.

## Output
Output an integer in a single line, representing the maximum possible number of color segments after performing at mostmoperations.