# Problem Description

There are three energy crystals numbered1,2, and3; let's denote the energy level of thei-th crystal asai. Initially, all of them are discharged, meaning their energy levels are equal to0. Each crystal needs to be charged to levelx(exactlyx, not greater).
In one action, you can increase the energy level of any one crystal by any positive amount; however, the energy crystals are synchronized with each other, so an action can only be performed if the following condition is met afterward:
What is the minimum number of actions required to charge all the crystals?

## Input
Each test consists of several test cases. The first line contains a single integert(1≤t≤104) — the number of test cases. The description of the test cases follows.
The only line of each test case contains a single integerx(1≤x≤109).

## Output
For each test case, output a single integer — the minimum number of actions required to charge all energy crystals to levelx.