# Problem Description


Serval has just found a Kaitenzushi buffet restaurant. Kaitenzushi means that there is a conveyor belt in the restaurant, delivering plates of sushi in front of the customer, Serval.
In this restaurant, each plate contains exactlykpieces of sushi and thei-th plate has adeliciousnessdi. Serval will have a meal in this restaurant fornminutes, and within thenminutes, he must eat upallthe pieces of sushi he took from the belt.
Denote the counter for uneaten taken pieces of sushi asr. Initially,r=0. In thei-th minute (1≤i≤n), only thei-th plate of sushi will be delivered in front of Serval, and he can dooneof the following:
Note that after thenminutes, the value ofrmustbe0.
Serval wants to maximize the sum of thedeliciousnessesof all the plates he took. Help him find it out!

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains two integersnandk(1≤k<n≤2⋅105) — the number of minutes of the meal and the number of sushi pieces in each plate.
The second line containsnintegersd1,d2,…,dn(1≤di≤109) — thedeliciousnessof each plate.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, print a single integer — the maximum possible sum of thedeliciousnessesof all the plates Serval took.