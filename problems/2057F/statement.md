# Problem Description

One day, the teachers of "T-generation" decided to instill discipline in the pupils, so they lined them up and made them calculate in order. There are a total ofnpupils, the height of thei-th pupil in line isai.
The line iscomfortable, if for eachifrom1ton−1, the following condition holds:ai⋅2≥ai+1. Initially, the line is comfortable.
The teachers do not like that the maximum height in the line is too small, so they want to feed the pupils pizza. You know that when a pupil eats one pizza, their height increases by1. One pizza can only be eaten by only one pupil, but each pupil can eat an unlimited number of pizzas. It is important that after all the pupils have eaten their pizzas, the line is comfortable.
The teachers haveqoptions for how many pizzas they will order. For each optionki, answer the question: what is the maximum heightmax(a1,a2,…,an)that can be achieved if the pupils eat at mostkipizzas.

## Input
Each test contains multiple test cases. The first line contains a single integert(1≤t≤104) — the number of test cases. The description of the test cases follows.
The first line of each set of test case contains two integersnandq(1≤n,q≤5⋅104) — the number of pupils and the number of options for how many pizzas the teachers will order.
The second line of each set of test case containsnintegersa1,a2,…,an(1≤ai≤109) — the heights of the pupils.It is guaranteed that initially, the line is comfortable.
Each of the followingqlines of each set of input data contains one integerki(1≤ki≤109) — the next limit for how many pizzas the pupils can eat.
It is guaranteed that the sum of the values ofnacross all sets of input data does not exceed5⋅104.
It is guaranteed that the sum of the values ofqacross all sets of input data does not exceed5⋅104.

## Output
For each test case, for each limit for how many pizzas the pupils can eat, output the maximum valuemax(a1,a2,…,an)that can be achieved while ensuring that the line is comfortable.