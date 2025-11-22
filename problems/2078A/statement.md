# Problem Description

You are given an arrayaof lengthn, and must perform the following operation until the length ofabecomes1.
Choose a positive integerk<|a|such that|a|kis an integer. Splitaintoksubsequences∗s1,s2,…,sksuch that:
After this, replacea=[avg(s1),avg(s2),…,avg(sk)], whereavg(s)=∑|s|i=1si|s|is the average of all the values in the subsequence. For example,avg([1,2,1,1])=54=1.25.
Your task is to determine whether there exists a sequence of operations such that after all operations,a=[x].
∗A sequencexis a subsequence of a sequenceyifxcan be obtained fromyby the deletion of several (possibly, zero or all) elements.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤500). The description of the test cases follows.
The first line of each test case contains two integersn,x(1≤n,x≤100) — the length of the arrayaand the final desired value.
The second line containsnintegersa1,a2,…,an(1≤ai≤100) — the arraya.

## Output
For each test case, output "YES'" (without quotes) if there exists such a sequence of operations, and "NO" (without quotes) otherwise.
You can output"YES"and"NO"in any case (for example, strings"yES","yes"and"Yes"will be recognized as a positive response).