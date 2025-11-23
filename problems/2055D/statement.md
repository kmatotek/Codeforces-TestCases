# Problem Description


A crow is sitting at position0of the number line. There arenscarecrows positioned at integer coordinatesa1,a2,…,analong the number line. These scarecrows have been enchanted, allowing them to move left and right at a speed of1unit per second.
The crow is afraid of scarecrows and wants to stay at least a distance ofkahead of the nearest scarecrow positionedat or beforeit. To do so, the crow uses its teleportation ability as follows:
This teleportation happens instantly and continuously. The crow will keep checking for scarecrows positioned at or to the left of him and teleport whenever one gets too close (which could happen at non-integral times). Note that besides this teleportation ability, the crow will not move on its own.
Your task is to determine the minimum time required to make the crow teleport to a position greater than or equal toℓ, assuming the scarecrows move optimally to allow the crow to reach its goal. For convenience, you are asked to outputtwice the minimum timeneeded for the crow to reach the target positionℓ. It can be proven that this value will always be an integer.
Note that the scarecrows can start, stop, or change direction at any time (possibly at non-integral times).

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains three integersn,k,ℓ(1≤n≤2⋅105,1≤k≤ℓ≤108) — the number of scarecrows, the teleportation distance, and the target position of the crow, respectively.
The second line of each test case containsnintegersa1,a2,…,an(0≤a1≤a2≤…≤an≤ℓ) — the initial positions of thenscarecrows.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, output a single integer representing thetwice the minimum timerequired for the crow to teleport to a position greater than or equal toℓ.