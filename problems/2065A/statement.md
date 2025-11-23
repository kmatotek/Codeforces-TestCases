# Problem Description

Skibidus lands on a foreign planet, where the local Amog tribe speaks the Amog'u language. InAmog'u, there are two forms of nouns, which aresingularandplural.
Given that the root of the noun is transcribed asS, the two forms are transcribed as:
Here,+denotesstring concatenation. For example,abc+def=abcdef.
For example, whenSis transcribed as "amog", then the singular form is transcribed as "amogus", and the plural form is transcribed as "amogi". Do note thatAmog'unouns can have anemptyroot — in specific, "us" is the singular form of "i" (which, on an unrelated note, means "imposter" and "imposters" respectively).
Given a transcribedAmog'unoun in singular form, please convert it to the transcription of the corresponding plural noun.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤100). The description of the test cases follows.
The only line of each test case contains a stringW, which is a transcribedAmog'unoun insingularform. It is guaranteed thatWconsists of only lowercase English letters, has a length of at most10, and ends with "us".

## Output
For each test case, output the transcription of the corresponding plural noun on a separate line.