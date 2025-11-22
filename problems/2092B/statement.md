# Problem Description

As soon as Dasha Purova crossed the border of France, the villain Markaron kidnapped her and placed her in a prison under his large castle. Fortunately, the wonderful Lady Bug, upon hearing the news about Dasha, immediately ran to save her in Markaron's castle. However, to get there, she needs to crack a complex password.
The password consists of two bit stringsaandb, each of which has a length ofn. In one operation, Lady Bug can choose any index2≤i≤nand perform one of the following actions:
Lady Bug can perform any number of operations. The password is considered cracked if she can ensure that the first string consists only of zeros. Help her understand whether or not she will be able to save the unfortunate Dasha.

## Input
Each test consists of several test cases. The first line of the input data contains one integert(1≤t≤104) — the number of test cases. The description of the test cases follows.
The first line of each test case contains one integern(2≤n≤2⋅105) — the length of the bit strings of the password.
The next two lines contain the bit strings of lengthn,aandb, which represent the password. Each of the strings contains only the characters0and'1'.
It is guaranteed that the sum ofnacross all test cases does not exceed2⋅105.

## Output
For each test case, output "YES" if Lady Bug can crack the password after any number of operations; otherwise, output "NO".
You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.