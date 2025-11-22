# Problem Description

Kenny is a kindergarten teacher who is teaching his students about math. To help them learn, he wants to give them homework in an enjoyable and non-annoying format – Number Search.
A Number Search puzzle is similar to a Word Search puzzle, but instead of words, it's about finding math expressions. An instance of the puzzle consists of two parts: a grid withnrows andmcolumns, and a lista1,a2,…,aqofqtarget numbers to search for. Each cell in the grid contains a digit from1to9, a plus sign+, or a multiplication sign*.
An expression can be formed by joining one or more consecutive characters along the same row, column, or diagonal, in a straight line (in either direction). Each expression can be defined by its starting cell and ending cell. Two expressions are considered different if they start or end at different cells, even if they contain the exact same characters.
A valid expression must be of the formnumopnumop…opnumwhere eachnumis a sequence of one or more digits, and eachopis either+or*. For example, "123" and "1+2*3+45" are valid expressions, while "+123" and "2**5" are not. The value of an expression is the result of evaluating it following typical arithmetic rules.
The goal of the puzzle is to count, for each numberai, how many different valid expressions in the grid evaluate toai.
To demonstrate the rules, consider the following completed Number Search puzzle:
Let's denote the cell at rowrand columncas(r,c).
Kenny can't wait to see children enjoy solving interesting Number Search puzzles. But before giving them a puzzle, he needs to have the answers ready. Please help him calculate the answers for each puzzle he has prepared.

## Input
The first line contains three integersn,m, andq, representing the number of rows, the number of columns, and the number of target numbers, respectively.
Each of the followingnlines contains a string ofmcharacters, representing the grid.
Thei-th of the followingqlines contains an integerai, representing thei-th target number.

## Output
Printqlines. Thei-th line contains an integer, representing the answer forai.