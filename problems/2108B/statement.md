# Problem Description


On a recent birthday, your best friend Maurice gave you a pair of numbersnandx, and asked you to construct an array ofpositivenumbersaof lengthnsuch thata1⊕a2⊕⋯⊕an=x∗.
This task seemed too simple to you, and therefore you decided to give Maurice a return gift by constructing an array among all such arrays that has the smallest sum of its elements. You immediately thought of a suitable array; however, since writing it down turned out to be too time-consuming, Maurice will have to settle for just the sum of its elements.
∗⊕denotes thebitwise XOR operation.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
Each test case consists of a single line containing a pair of numbersnandx(1≤n≤109,0≤x≤109) — the numbers given to you by Maurice.

## Output
For each test case, output your gift to Maurice — the sum of the elements of the array that satisfies all the described properties. If a suitable array does not exist, output−1.