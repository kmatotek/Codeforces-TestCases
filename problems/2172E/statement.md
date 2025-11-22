# Problem Description

At the "Number Maze," a mysterious code master stands guard. He blocks the path and smiles, saying: "Brave adventurer, passing through this gate will not be easy! An ancient numeric code, capable of being rearranged into numerous combinations, is in the code master's possession. The traveler must choose two numeric codes from these combinations and show theirxAyBresult, or the gate will trap the traveler here forever!"
The rules ofxAyBare as follows:
For example:
You are given a base numeric coden, which can be one of{12,123,1234}. Consider all possible permutations of the digits ofn, sorted in ascending order. Let thej-th andk-th permutations (1-indexed) be the two numeric codes chosen by the traveler.
Your task is to compare these two permutations and determine theirxAyBresult, according to the rules above.

## Input
Each test contains multiple test cases. The first line contains a single integert, representing the number of tests the code master will conduct. The description of the test cases follows.
The only line of each test case contains three integersn,j, andk, representing the base numeric code and the indices of the two permutations to be compared, respectively.

## Output
For each test case, output the result in the formatxAyB, wherexandyare integers.