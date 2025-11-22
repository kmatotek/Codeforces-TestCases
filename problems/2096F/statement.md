# Problem Description

You are a proud live streamer known as Gigi Murin. Today, you will play a game withnviewers numbered1ton.
In the game, each player is either a crewmate or an impostor. You don't know the role of each viewer.
There aremstatements numbered1tom, which are eithertrue or false. For eachifrom1tom, statementiis one of two types:
Answerqquestions of the following form:
Note that it isnot guaranteedthat there is at least one impostor among all viewers, and it isnot guaranteedthat there is at least one crewmate among all viewers.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains two integersn,m(1≤n,m≤2⋅105) — the number of viewers, and the number of statements.
Thei-th of the nextmlines contains three integersxi,ai,bi(xi∈{0,1},1≤ai≤bi≤n) — describing statementi.
The next line contains a single integerq(1≤q≤2⋅105) — the number of questions.
Each of the nextqlines contains two integerslandr(1≤l≤r≤m) — describing a question.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105, the sum ofmover all test cases does not exceed2⋅105, and the sum ofqover all test cases does not exceed2⋅105.

## Output
For each question, output "YES" if it is possible that the requested statements are all true. Otherwise, output "NO".
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.