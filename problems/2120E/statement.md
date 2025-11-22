# Problem Description

Harshith is the president of TollClub. He tasks his subordinate Aryan to oversee a toll plaza withnlanes. Initially, thei-th lane hasaicars waiting in a queue. Exactly one car from the front of each lane passes through the toll every second.
The angriness of a car is defined as the number of seconds it had to wait before passing through the toll. Consider it takes 1 sec for each car to pass the toll, i.e., the first car in a lane has angriness1, the second car has angriness2, and so on.
To reduce congestion and frustration, cars are allowed to switch lanes. A car can instantly move to the back of any other lane at any time. However, changing lanes increases its angriness by an additionalkunits due to the confusion caused by the lane change.
Harshith, being the awesome person he is, wants to help the drivers by minimising the total angriness of all cars. He asks Aryan to do so or get fired. Aryan is allowed to change lanes of any car anytime (possibly zero), but his goal is to find the minimum possible total angriness if the lane changes are done optimally. Help Aryan retain his job by determining the minimum angriness he can achieve.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains two integersnandk(1≤n≤2⋅105,1≤k≤106) — the number of lanes and the increment in angriness on a lane change.
The second line of each test case containsnspace-separated integers, denoting arraya— thei-th number representing the number of cars in thei-th lane (1≤ai≤106).
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.
Note that the sum ofmaxaiover all test cases isnotbounded.

## Output
For each test case, output a single integer in a new line, denoting the minimum total angriness.