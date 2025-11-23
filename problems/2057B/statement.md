# Problem Description

Due to a shortage of teachers in the senior class of the "T-generation", it was decided to have a huge male gorilla conduct exams for the students. However, it is not that simple; to prove his competence, he needs to solve the following problem.
For an arrayb, we define the functionf(b)as the smallest number of the following operations required to make the arraybempty:
You are given an arrayaof lengthnand an integerk. No more thanktimes, you can choose any indexi(1≤i≤n) and any integerp, and replaceaiwithp.
Help the gorilla to determine the smallest value off(a)that can be achieved after such replacements.

## Input
Each test contains multiple test cases. The first line contains a single integert(1≤t≤104) — the number of test cases. The description of the test cases follows.
The first line of each set of input data contains two integersnandk(1≤n≤105,0≤k≤n) — the length of the arrayaand the maximum number of changes, respectively.
The second line of each set of input data containsnintegersa1,a2,…,an(1≤ai≤109) — the arrayaitself.
It is guaranteed that the sum of the values ofnacross all sets of input data does not exceed105.

## Output
For each set of input data, output a single integer on a separate line — the smallest possible value off(a).