# Problem Description

You have a special sliding puzzle played on ann×ngrid. This puzzle is slightly different from standard sliding puzzles: between each pair of adjacent columns, there is a vertical bar of heighthi(for1≤i<n) positioned at the bottom of the grid. Eachhiindicates how many rows from the bottom this bar extends upwards, and it blocks tile movement between the two columns in those rows.
The grid contains several tiles, each occupying exactly one cell. These tiles can slide freely in the grid unless they are blocked by the grid boundaries, a vertical bar (depending on its height) or another tile.
The puzzle allows two types of tilt operations:
In both operations, all tiles move simultaneously and stop only when blocked by the grid's edge, a bar, or another tile.
Define a group operation as a sequence of: first tilt the grid to the right, then tilt it downward.
Initially, thei-th column hasaitiles stacked from the bottom of the column. You perform the group operation exactly once on the board. After the operation, determine the number of tiles in each column.

## Input
The first line contains an integern, representing the size of the board.
The second line containsnintegersa1,a2,…,an, whereaiis the number of tiles in thei-th column initially.
The third line containsn−1integersh1,h2,…,hn−1, wherehiis the height of the bar between columniand columni+1.

## Output
Printnnumbers in a new line, representing the number of tiles in each column after performing the group operation exactly once.