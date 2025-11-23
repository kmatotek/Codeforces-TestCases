# Problem Description

You are playing a pinball-like game on ah×wgrid.
The game begins with a small ball located at the center of a specific cell marked asS. Each cell of the grid is either:
The goal is to make the ball escape the grid.
At the start, you can nudge the ball in one of four directions: up (U), down (D), left (L), or right (R). The ball traverses a free cell in one second, it enters and exits a cell containing a thin oblique wall in one second, and it bounces off a block-type wall in no time (the block-type wall occupies all of its cell).
Collisions between the ball and all walls, both block-type and oblique, are perfectly elastic, causing the ball to reflect upon contact.
For example, the ball takes two seconds to enter a free cell, traverse it, bounce off an adjacent block-type wall, and traverse back the free cell until it exits.
As the ball moves, you may destroy oblique walls at any time, permanently converting them into free cells. You may destroy multiple oblique walls throughout the game, at any given time.
Determine whether it is possible for the ball to escape, and if so, find theminimumnumber of oblique walls that need to be destroyed, along with the precise time each chosen wall should be destroyed.

## Input
The first line contains two integershandw(1≤h,w≤1000) — the size of the grid.
The nexthlines describe the grid at the beginning of the game.
Thei-th of these lines containswcharacters, describing the cells on thei-th row. A dot (.) denotes a free cell, a hash sign (#) denotes a block-type wall, a (\) or (/) denotes a thin oblique wall, and anSdenotes the starting position of the ball (the starting position is a free cell).
It is guaranteed that all theh⋅wcharacters describing the grid belong to the set{.,#,\,/,S}and the characterSappears exactly once.

## Output
PrintYESif it is possible to make the ball escape the grid. Otherwise, printNO.
If it is possible, print the following extra information.
On the second line, print a single characterd∈{U,D,L,R}— the direction of the starting nudge of the ball.
On the third line, printk— the minimum number of oblique walls to be destroyed.
On each of the followingklines, print three integersti,ri, andci— the oblique wall in the cell on theri-th row from the top and on theci-th column from the left is destroyedtiseconds after the ball starts moving. Note that the corresponding wall is destroyedjust beforetiseconds have elapsed, essentially meaning that the corresponding cell acts as a free cell if the ball would have hit that wall exactlytiseconds after the start.
The operations must be printed in chronological order(i.e.,ti≤ti+1for all1≤i≤k−1). The same wall cannot be destroyed multiple times (i.e.,(ri,ci)≠(rj,cj)ifi≠j). Initially, there must be an oblique wall at the cell identified by(ri,ci)for all1≤i≤k.
Alltimust satisfy0≤ti≤107. It can be proved that, if there exists a solution, there exists a solution where notiexceeds107.