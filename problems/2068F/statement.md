# Problem Description

When organizing a big event, organizers often handle side tasks outside their expertise. For example, the chief judge of EUC 2025 must find a name for the event's official mascot while satisfying certain constraints:
*A stringxis asubsequenceof a stringyifxcan be obtained fromyby erasing some characters (at any positions) while keeping the remaining characters in the same order. For example,abcis a subsequence ofaxbyczbut not ofacbxyz.

## Input
The first line contains an integern(1≤n≤200000) — the number of words that shall appear as subsequences.
Thei-th of the followingnlines contains the stringsi(1≤|si|≤200000,siconsists of lowercase English letters) — thei-th word in the list of words that shall appear as subsequences. The total length of thesenwords is at most200000, i.e.,|s1|+|s2|+⋯+|sn|≤200000.
The last line contains the stringt(1≤|t|≤200000,tconsists of lowercase English letters) — the name of last year's mascot.

## Output
PrintYESif there is a valid name for the mascot. Otherwise, printNO.
If there is a valid name, on the next line print a valid name. The string you print must have length at most1000000and must consist of lowercase English letters. One can prove that if a valid name for the mascot exists, then there is one satisfying these additional constraints.
If there are multiple solutions, print any of them.