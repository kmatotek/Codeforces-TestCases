# Problem Description

This is an interactive problem.
In a certain database, there arenhandles stored in the form of a numbered list. You are interested in one specific handleh, or more precisely, in its position in this list.
You can ask the database for the positionifrom the list, and it will return the handle at thei-th position.
All handles are non-empty strings consisting of at most20lowercase Latin letters,except the first onethat can be either a lowercase or an uppercase Latin letter.
You know that all handles are sorted in lexicographical order, but the problem is that it is unknown whether uppercase letters are considered less than lowercase ones. In other words, you do not know if it is true that all handles starting with uppercase letters come first, followed by those starting with lowercase letters — or vice versa, that all handles starting with lowercase letters come first, followed by those starting with uppercase letters.
Lexicographical order is the order of standard string comparison, formally defined as follows:
Due to restricted access to the database, you can make no more than10queries to it. Determine the position of the handle you are interested in, knowing that it is definitely in the list.

## Input
The first line contains the numbernand the stringh(1≤n≤500) — the total number of handles in the list and the handle you are searching for.
It is guaranteed that all handles are non-empty strings of no more than20characters, consisting only of lowercase Latin letters, except the first letter that may be an uppercase letter.
It is also guaranteed that all handles are sorted, unique, and the given handle is in the list.
