# Problem Description

Megumin is a wizard who can cast powerful magic spells that affect large areas. She is obsessed with the extremely devastating Explosion spell that can destroy everything around its target.
There are currentlynslimes in the wild. Each slime's location can be described in 2D Cartesian coordinates. Megumin wishes to kill at leastkslimes so she can earn more experience points to level up her Explosion. To do that, she can choose any circle on the plane and cast an Explosion spell which kills every slime inside or on the border of the circle.
However, the Explosion magic requires a large amount of mana to cast, and Megumin can only use it once per day. The amount of mana used is equal to the area inside the circle she chooses. What is the minimum amount of mana she needs to spend to killkslimes with a single Explosion?

## Input
The first line contains two integersnandk(1≤k≤n≤105) — the number of slimes and how many slimes Megumin needs to defeat.
Each of the nextnlines contains two integersxandy(−109≤x,y≤109), denoting the coordinates(x,y)of a slime's location. It is guaranteed that all locations are distinct and that no three slimes lie on the same circle.

## Output
Print one real number — the answer.
Your answer is considered correct if its absolute or relative error does not exceed10−6. Formally, let your answer bea, and the jury's answer beb. Your answer is accepted if and only if|a−b|max(1,|b|)≤10−6.