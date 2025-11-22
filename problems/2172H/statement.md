# Problem Description

Aru loves playing card games (Poker, Texas hold 'em, Balatro, etc.) and she has perfected the art of shuffling cards, especially theriffleshuffle. She is playing with Mutsuki now, and it's her turn to shuffle the cards!
However, Mutsuki knows that Aru is too perfect with her shuffling game. In fact, given a deck with anevennumber of cards, Aru always performs a perfect riffle: she cuts the deck evenly and interleaves the two halves. Formally, if the deck is represented by a stringsof lengthn, wheresiis thei-th card from the top, one riffle produces the decks′=s1+sn/2+1+s2+sn/2+2+…+sn/2+sn.Mutsuki also knows that when handed a deck of cards, Aru will riffle it exactlyttimes.
Mutsuki currently holds a deck of2kcards, represented by a stringd.Beforegiving the deck to Aru, Mutsuki can choose tocutthe deck, by moving some number of cards from the top to the bottom of the deck. Formally, she can choose anymfrom0to2k−1, and produce the deckd′=dm+1+dm+2+…+d2k+d1+d2+…+dm.
Among all2kpossible cuts, Mutsuki wants to choose the one that results in thelexicographically smallestdeck after Aru riffles itttimes. Can you figure this out for her?

## Input
The first line contains two integerskandt, representing the size parameter of the deck, and the number of times Aru will riffle the deck, respectively.
The second line contains a stringdof2klowercase characters, representing the original deck of cards that Mutsuki has.

## Output
Print a string in one line, representing the lexicographically smallest deck of cards that Mutsuki can produce, by first cutting the deck and letting Aru riffle itttimes.