# Problem Description

Vadim loves filling square tables with integers. But today he came up with a way to do it for fun! Let's take, for example, a table of size2×2, with rows numbered from top to bottom and columns numbered from left to right. We place1in the top left cell,2in the bottom right,3in the bottom left, and4in the top right. That's all he needs for fun!
Fortunately for Vadim, he has a table of size2n×2n. He plans to fill it with integers from1to22nin ascending order. To fill such a large table, Vadim will divide it into4equal square tables, filling the top left one first, then the bottom right one, followed by the bottom left one, and finally the top right one. Each smaller table will be divided into even smaller ones as he fills them until he reaches tables of size2×2, which he will fill in the order described above.
Now Vadim is eager to start filling the table, but he hasqquestions of two types:

## Input
Each test consists of several sets of input data. The first line contains a single integert(1≤t≤10)— the number of sets of input data. The following lines describe the input data sets.
In the first line of each data set, there is an integern, describing the size of the table(1≤n≤30).
In the second line of each data set, there is an integerq— the number of questions(1≤q≤20000).
In the followingqlines of each data set, the questions are described in the following formats:
It is guaranteed that the sum ofqover all test cases does not exceed20000.

## Output
Output the answers to each question on a separate line.