# Problem Description

Anon and Soyo are good friends. To celebrate Anon's birthday, Soyo decides to buy a cake. After careful selection, she chooses a round strawberry cake to share with Anon at home.
The cake is modeled as a circle centered at the origin(0,0)with radiusr. There arenstrawberries on the cake, where thei-th strawberry is located at(xi,yi). The distance of any strawberry from the origin is at most0.9r.
Soyo wants to cut the cake into two pieces with a single straight line. Since Anon loves strawberries, Soyo wants Anon's piece contains all of them. If a strawberry lies on the cutting line, Soyo can assign it to either piece.
Soyo wants to make the smaller piece as large as possible. Please help Soyo determine the maximum possible area of the smaller piece, given that all strawberries lie on the same piece.

## Input
The first line contains two integersnandr, representing the number of strawberries on the cake and the radius of the cake, respectively.
Thei-th of the followingnlines contains two integersxiandyi, representing the coordinates of thei-th strawberry.

## Output
Print a single real number in one line, representing the maximum possible area of the smaller piece, given that all strawberries lie on the same piece.
Your answer will be accepted if the absolute or relative error does not exceed10−6. Formally, let your answer bea, and the jury's answer beb. Your answer is considered correct if|a−b|max(1,|b|)≤10−6.