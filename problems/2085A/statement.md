# Problem Description


A stringrconsisting only of lowercase Latin letters is calleduniversalif and only ifris lexicographically smaller∗than the reversal†ofr.
You are given a stringsconsisting ofnlowercase Latin letters. You are required to makesuniversal. To achieve this, you can perform the following operation onsat mostktimes:
Determine whether you can makesuniversalby performing the above operation at mostktimes.
∗A stringais lexicographically smaller than a stringbof the same length, if and only if the following holds:
†The reversal of a stringris the string obtained by writingrfrom right to left. For example, the reversal of the stringabcadisdacba.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤500). The description of the test cases follows.
The first line of each test case contains two integersnandk(1≤n≤100,0≤k≤104) — the length of the strings, and the maximum number of operations you can perform.
The second line contains a stringsconsisting ofnlowercase Latin letters.

## Output
For each test case, print "YES" if it is possible to makesuniversalby performing the operation at mostktimes. Otherwise, print "NO".
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.