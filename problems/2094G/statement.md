# Problem Description

Chimpanzini Bananini stands on the brink of a momentous battle—one destined to bring finality.
For an arbitrary arraybof lengthm, let's denote therizzinessof the array to be∑mi=1bi⋅i=b1⋅1+b2⋅2+b3⋅3+…+bm⋅m.
Chimpanzini Bananini gifts you an empty array. There are three types of operations you can perform on it.
After each operation, you are interested in calculating therizzinessof your array.
Note that all operations arepersistent. This means that each operation modifies the array, and subsequent operations should be applied to the current state of the array after the previous operations.

## Input
The first line contains an integert(1≤t≤104) — the number of test cases.
The first line of each test case contains an integerq(1≤q≤2⋅105) — the number of operations you perform on your array.
The followingqlines first contain a single integers(1≤s≤3) — the operation type.
It is guaranteed that the sum ofqwill not exceed2⋅105over all test cases. Additionally, it is guaranteed that the first operation on each test case will be one withs=3.

## Output
For each test case, outputqlines, outputting therizzinessof your array after each operation.