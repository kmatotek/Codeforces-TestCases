# Problem Description

You've been staring at your computer screen for too long; it is time to give it a break and go touch some grass.
Your screen is a line of lengtha, and there arentabs displayed on it. You want to close all of the tabs by clicking on the x's at their right endpoint.
Every tab is a segment of lengthlen=min, wheremis the number of remaining tabs. The tabs are always tightly arranged in sequence from the left endpoint of the screen; that is, the x's will be at\textrm{len},2\cdot \textrm{len},3\cdot \textrm{len},\ldots,m\cdot\textrm{len}units away from the left endpoint. Please note that the length of each tab will change as you are closing tabs.
Now your cursor is at the left endpoint of the screen. You wonder what the minimum number oftimesyou need to move the mouse to close all tabs is.
If you have difficulty understanding the statement, you may also refer to your browser tab for a visualization, or clickhere.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1 \le t \le 10^4). The description of the test cases follows.
Each test case is a line of three integersa,b, andn(1\le b\le a \le 10^9,1\le n \le 10^9).

## Output
For each test case, output a single integer — the minimum number of times you need to move the mouse to close all tabs.