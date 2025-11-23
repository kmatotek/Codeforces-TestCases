# Problem Description

Rumors of the excellence of Gabriella's wine tasting events have toured the world and made it to the headlines of prestigious wine magazines. Now, she has been asked to organize an event at the EUC 2025!
This time she selected2nbottles of wine, of which exactlynare of white wine, and exactlynof red wine. She arranged them in a line as usual, in a predetermined order described by a stringsof length2n: for1≤i≤2n, thei-th bottle from the left is white wine ifsi=Wand red wine ifsi=R.
To spice things up for the attendees (which include EUC contestants), Gabriella came up with the following wine-themed problem:
Consider a way of dividing the2nbottles into two disjoint subsets, each containingnbottles. Then, for every1≤i≤n, swap thei-th bottle in the first subset (from the left) and thei-th bottle of the second subset (also from the left). Is it possible to choose the subsets so that, after this operation is done exactly once, the white wines occupy the firstnpositions?

## Input
The first line contains an integert(1≤t≤500) — the number of test cases. The descriptions of thettest cases follow.
The first line of each test case contains an integern(1≤n≤100) — where2nis the total number of bottles.
The second line of each test case contains a stringsof length2n, describing the bottle arrangement — thei-th character ofs(1≤i≤2n) isWfor a white wine andRfor a red wine.
It is guaranteed thatscontains exactlynW's andnR's.

## Output
For each test case, printYESif it is possible to divide the bottles as explained in the statement. Otherwise, printNO.