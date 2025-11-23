# Problem Description

There are very long classes in the T-Generation. In one day, you need to have time to analyze the training and thematic contests, give a lecture with new material, and, if possible, also hold a mini-seminar. Therefore, there is a break where students can go to drink coffee and chat with each other.
There are a total ofn+2coffee machines located in sequentially arranged rooms along a long corridor. The coffee machines are numbered from0ton+1, and immediately after the break starts, there areaistudents gathered around thei-th coffee machine.
The students are talking too loudly among themselves, and the teachers need to make a very important announcement. Therefore, they want to gather the maximum number of students around some single coffee machine. The teachers are too lazy to run around the corridors and gather the students, so they came up with a more sophisticated way to manipulate them:
The teachers have not yet decided where they will gather the students, so for eachifrom1ton, you should determine what is the maximum number of students that can be gathered around thei-th coffee machine.
The teachers can turn off the lights in any rooms at their discretion, in any order, possibly turning off the lights in the same room multiple times.
Note that the values ofa0andan+1do not affect the answer to the problem, so their values will not be given to you.

## Input
The first line contains a single integert(1≤t≤10000) — the number of test cases.
In the first line of each test case, there is an integern(1≤n≤106).
In the second line of each test case, there are integersa1,…,an(0≤ai≤109) — the number of students around coffee machines numbered1,2,…,n.
It is guaranteed that the sum ofnacross all test cases does not exceed106.

## Output
For each test case, outputnintegersb1,…,bn, wherebiis the maximum number of students that can be around coffee machines numberi.