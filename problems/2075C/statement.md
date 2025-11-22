# Problem Description

Monocarp has installed a new fence at his summer house. The fence consists ofnplanks of the same size arranged in a row.
Monocarp decided that he would paint his fence according to the following rules:
Monocarp hasmdifferent paints, and the paint of thei-th color is sufficient to paint no more thanaiplanks of the fence. Monocarp will not buy any additional paints.
Your task is to determine the number of different ways to paint the fence that satisfy all of Monocarp's described wishes. Two ways to paint are considered different if there exists a plank that is painted in different colors in these two ways.

## Input
The first line contains a single integert(1≤t≤104) — the number of test cases.
The first line of each test case contains two integersnandm(2≤n,m≤2⋅105) — the number of planks in the fence and the number of different colors of paint that Monocarp has.
The second line containsmintegersa1,a2,…,am(1≤ai≤n), whereaiis the maximum number of planks that can be painted with the paint of colori.
The sum ofnover all test cases does not exceed2⋅105. The sum ofmover all test cases does not exceed2⋅105.

## Output
For each test case, output the number of different ways to paint the fence that satisfy all of Monocarp's described wishes.