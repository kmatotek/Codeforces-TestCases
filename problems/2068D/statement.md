# Problem Description

Morse code is a classical way to communicate over long distances, but there are some drawbacks that increase the transmission time of long messages.
In Morse code, each character in the alphabet is assigned a sequence of dots and dashes such thatno sequence is a prefix of another. To transmit a string of characters, the sequences corresponding to each character are sent in order.A dash takes twice as long to transmit as a dot.
Your alphabet has $$$n$$$ characters, where the $$$i$$$-th character appears with frequency $$$f_i$$$ in your language. Your task is to design a Morse code encoding scheme, assigning a sequence of dots and dashes to each character, that minimizes the expected transmission time for a single character. In other words, you want to minimize $$$f_1t_1 + f_2t_2 + \cdots + f_nt_n$$$, where $$$t_i$$$ is the time required to transmit the sequence of dots and dashes assigned to the $$$i$$$-th character.

## Input
The first line contains an integer $$$n$$$ ($$$2\le n\le 200$$$) — the number of characters in the alphabet.
The second line contains $$$n$$$ real numbers $$$f_1$$$, $$$f_2$$$, $$$\ldots$$$, $$$f_n$$$ ($$$0 < f_i < 1$$$) — $$$f_i$$$ is the frequency of the $$$i$$$-th character. All values $$$f_1$$$, $$$f_2$$$, $$$\ldots$$$, $$$f_n$$$ are given with exactly four digits after the decimal point. The sum of all frequencies is exactly 1.

## Output
Print $$$n$$$ lines, each containing one string consisting of dots $$$\texttt{.}$$$ and dashes $$$\texttt{-}$$$. The $$$i$$$-th line corresponds to the sequence of dots and dashes that you assign to the $$$i$$$-th character.
If there are multiple valid assignments with the minimum possible expected transmission time, any of them is considered correct.