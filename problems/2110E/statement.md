# Problem Description

In 2077, the robots that took over the world realized that human music wasn't that great, so they started composing their own.
To write music, the robots have a special musical instrument capable of producingndifferent sounds. Each sound is characterized by its volume and pitch. A sequence of sounds is called music. Music is consideredbeautifulif any two consecutive sounds differ either only in volume or only in pitch. Music is consideredboringif the volume or pitch of any three consecutive sounds is the same.
You want to composebeautiful,non-boringmusic that contains each sound produced by your musical instrument exactly once.

## Input
Each test contains multiple test cases. The first line contains the number of test casest(1≤t≤104). The description of the test cases follows.
In the first line of each test case, there is a numbern(1≤n≤2⋅105) — the number of sounds that the musical instrument can produce.
Next, there arenlines, where thei-th line contains a pair of numbersvi,pi(1≤vi,pi≤109) — the volume and pitch of thei-th sound, respectively. It is guaranteed that among allnsounds, there are no duplicates, meaning for anyi≠j, at least one of the conditionsvi≠vjorpi≠pjholds.
The sum ofnacross all test cases does not exceed2⋅105.

## Output
For each test case, if it is possible to compose such music, output "YES", and on the next line, outputnnumbers — the indices of the sounds in the order that forms beautiful non-boring music. Otherwise, output "NO".
You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.