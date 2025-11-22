# Problem Description


Steve stumbled upon a collection of $$$n$$$ gears, where gear $$$i$$$ has $$$a_i$$$ teeth, and he wants to arrange them into a row.
After he arranges them, Steve will spin the leftmost gear at a speed of $$$1$$$ revolution per second. For each of the other gears, let $$$x$$$ be the number of teeth it has, $$$y$$$ be the number of teeth of the gear to its left, and $$$z$$$ be the speed the gear to its left spins at. Then, its speed will be $$$\frac{y}{x} \cdot z$$$ revolutions per second.
Steve considers the contraptionsatisfactoryif the rightmost gear spins at a speed of $$$1$$$ revolution per second. Determine whether Steve can rearrange the gears into a satisfactory contraption.

## Input
Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 1000$$$). The description of the test cases follows.
The first line of each test case contains a single integer $$$n$$$ ($$$2 \le n \le 100$$$) — the number of gears Steve has.
The second line of each test case contains $$$n$$$ integers $$$a_1,a_2,\ldots,a_n$$$ ($$$2 \le a_i \le 100$$$) — the number of teeth of each gear.

## Output
For each test case, print "YES" if Steve can rearrange the gears in a satisfactory way, and "NO" otherwise.
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.