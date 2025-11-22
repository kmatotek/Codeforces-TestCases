# Problem Description

Natsume Akito has just woken up in a new world and immediately received his first quest! The system provided him with an arrayaofnzeros, an integerk, and an integerp.
In one operation, Akito chooses two integersiandxsuch that1≤i≤nand−p≤x≤p, and performs the assignmentai=x.
Akito is still not fully accustomed to controlling his new body, so help him calculate the minimum number of operations required to make the sum of all elements in the array equal tok, or tell him that it is impossible.

## Input
The first line of input contains one integert(1≤t≤1000) — the number of test cases.
The only line of each test case contains three integersn,k,p(1≤n≤50,−2500≤k≤2500,1≤p≤50) — the length of the array, the required sum, and the boundary of the segment from which numbers can be replaced.

## Output
For each test case, output the minimum number of operations to achieve the final sumkin the array, or−1if it is impossible to achieve the sumk.