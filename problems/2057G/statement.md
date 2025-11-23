# Problem Description

Every Saturday, Alexander B., a teacher of parallel X, writes a secret message to Alexander G., a teacher of parallel B, in the evening. Since Alexander G. is giving a lecture at that time and the message is very important, Alexander B. has to write this message on an interactive online board.
The interactive online board is a grid consisting ofnrows andmcolumns, where each cell is1×1in size. Some cells of this board are already filled in, and it is impossible to write a message in them; such cells are marked with the symbol ".", while the remaining cells are calledfreeand are marked with the symbol "#".
Let us introduce two characteristics of the online board:
LetAbe the set of free cells. Your goal is to find a set of cellsS⊆Athat satisfies the following properties:
We can show that at least one setSsatisfying these properties exists; you are required to findany suitableone.

## Input
The first line contains the numbert(1≤t≤80000) — the number of test cases.
In the first line of each test case, the numbersnandm(1≤n,m≤2⋅106) — the dimensions of the grid are given.
The followingnlines contain the description of the grid.
It is guaranteed that the sum ofn⋅macross all test cases does not exceed2⋅106.

## Output
For each test case, outputnlines consisting ofmsymbols, where each symbol encodes the state of the cell: