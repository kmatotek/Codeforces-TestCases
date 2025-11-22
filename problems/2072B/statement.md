# Problem Description

After completing the first quest, Akito left the starting cave. After a while, he stumbled upon a goblin village.
Since Akito had nowhere to live, he wanted to find out the price of housing. It is well known that goblins write numbers as a string of characters '-' and '_', and the value represented by the stringsis the number of distinct subsequences∗of the stringsthat are equal to the string "-_-" (this is very similar to goblin faces).
For example, the strings="-_--_-" represents the number6, as it has6subsequences "-_-":
Initially, the goblins wrote a random string-numbersin response to Akito's question, but then they realized that they wanted to take as much gold as possible from the traveler. To do this, they ask you to rearrange the characters in the stringsso that the value of the number represented by the stringsis maximized.
∗A subsequence of a stringais a stringbthat can be obtained by deleting several (possibly0) characters froma. Subsequences are considered different if they are obtained by deleting different sets of indices.

## Input
The first line contains the numbert(1≤t≤104) — the number of test cases.
In the first line of each test case, there is one numbern(1≤n≤2⋅105) — the length of the string written by the goblins.
In the second line of each test case, there is a stringsof lengthn, consisting only of characters '-' and '_' — the string written by the goblins.
It is guaranteed that the sum ofnacross all test cases does not exceed2⋅105.

## Output
For each test case, you need to output one number — the maximum number of subsequences equal to the string "-_-", if the characters in the stringsare optimally rearranged.