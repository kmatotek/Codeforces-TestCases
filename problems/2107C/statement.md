# Problem Description

You are given an arraya1,a2,…,anof lengthnand a positive integerk, but some parts of the arrayaare missing. Your task is to fill the missing part so that themaximum subarray sum∗ofais exactlyk, or report that no solution exists.
Formally, you are given a binary stringsand a partially filled arraya, where:
All the values that you remember satisfy|ai|≤106. However, you may use values up to1018to fill in the values that you do not remember. It can be proven that if a solution exists, a solution also exists satisfying|ai|≤1018.
∗Themaximum subarray sumof an arrayaof lengthn, i.e.a1,a2,…anis defined asmax1≤i≤j≤nS(i,j)whereS(i,j)=ai+ai+1+…+aj.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
The first line of each test case contains two numbersn,k(1≤n≤2⋅105,1≤k≤1012).
The second line of each test case contains a binary (01) stringsof lengthn.
The third line of each test case containsnnumbersa1,a2,…,an(|ai|≤106). Ifsi=0, then it's guaranteed thatai=0.
It is guaranteed that the sum ofnover all test cases does not exceed2⋅105.

## Output
For each test case, first outputYesif a solution exists orNoif no solution exists. You may print each character in either case, for exampleYESandyEswill also be accepted.
If there's at least one solution, printnnumbersa1,a2,…,anon the second line.|ai|≤1018must hold.