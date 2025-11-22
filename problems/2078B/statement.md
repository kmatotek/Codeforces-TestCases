# Problem Description

There arencells in a labyrinth, and celli(1≤i≤n) isn−ikilometers away from the exit. In particular, cellnis the exit. Note also that each cell is connected to the exit but is not accessible from any other cell in any way.
In each cell, there is initially exactly one person stuck in it. You want to help everyone get as close to the exit as possible by installing a teleporter in each celli(1≤i≤n), which translocates the person in that cell to another cellai.
The labyrinth owner caught you in the act. Amused, she let you continue, but under some conditions:
You must find a teleporter configuration that minimizes the sum of distances of all individuals from the exit after using the teleporter exactlyktimes while still satisfying the restrictions of the labyrinth owner.
If there are many possible configurations, you can output any of them.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first and only line of each test case contains two integersnandk(2≤n≤2⋅105,1≤k≤109) — the number of cells in the labyrinth and the valuek.
It is guaranteed that the total sum ofnacross all test cases does not exceed2⋅105.

## Output
For each test case, outputnintegers — the destinations of the teleportersa1,a2,…,anin order, satisfying the given conditions (1≤ai≤n,ai≠i).