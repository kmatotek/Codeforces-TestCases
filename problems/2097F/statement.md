# Problem Description

As is known, the airline "Trouble" often loses luggage, and concerned journalists decided to calculate the maximum number of luggage pieces that may not return to travelers.
The airline "Trouble" operates flights betweennairports, numbered from1ton. The journalists' experiment will last formdays. It is known that at midnight before the first day of the experiment, there weresjlost pieces of luggage in thej-th airport. On thei-th day, the following occurs:
For eachkfrom1tom, the journalists want to know the maximum number of lost pieces of luggage that may beunfoundduring the checks over the firstkdays. Note that for eachk, these values are calculated independently.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤100). The description of the test cases follows.
The first line of each test case contains two integersnandm(3≤n≤12,1≤m≤2000) — the number of airports and the number of days of the experiment.
The second line of each test case containsnintegerss1,s2,…,sn(0≤si≤108) — the initial number of lost pieces of luggage in each airport.
Next, the descriptions for each of themdays follow in order.
The first line of the description of thei-th day containsnintegersai,1,ai,2,…,ai,n(0≤ai,j≤108) — the maximum number of lost pieces of luggage that can be transported to the previous airport for each airport.
The second line of the description of thei-th day containsnintegersbi,1,…,bi,n(0≤bi,j≤108) — the minimum number of lost pieces of luggage that will be found on thei-th day in each airport.
The third line of the description of thei-th day containsnintegersci,1,…,ci,n(0≤ci,j≤108) — the maximum number of lost pieces of luggage that can be transported to the next airport for each airport.
It is guaranteed that the sum ofmover all test cases does not exceed2000.

## Output
For each test case, outputmintegers — the maximum number of unfound pieces of luggage for each number of days from1tom.