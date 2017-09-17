from structures.card import Card
from random import randint

# class Deck
#   Object: Deck - Represents a 52 Card Deck
# Shared class data:
#   N/A
# Attributes:
#   deckList - the list of all 52 of the cards in the deck
#   index - the index in the current deckList that represents the top card
class Deck:

    # **__init()__**
    # Creates a Deck object and shuffles it
    # Args:
    #   N/A
    # Return:
    #   N/A
    def __init__(self):
        self.index = 0
        self.deckList = []
        for i in [2, 3, 4, 5, 6, 7, 8,
                    9, 10, 11, 12, 13, 14]:
            for j in [0, 1, 2, 3]:
                self.deckList.append(Card(i,j))
        self.shuffle()

    # **shuffle()**
    # Randomly shuffles the list of cards
    # Args:
    #   N/A
    # Return:
    #   N/A
    def shuffle(self):
        self.index = 0
        for x in range(0, 50):
            temp = self.deckList[x]
            num = randint((x + 1), 51)
            self.deckList[x] = self.deckList[num]
            self.deckList[num] = temp

    # ~~~Dealing Methods~~~ #

    # **peekCard()**
    # Gets a card object at a given index in the reamining deck without
    #   altering the top card of the deck
    # Args:
    #   subIndex - the index of the card in the remaining deck (0-maxIndex)
    # Return:
    #   The card at that sub-index
    def peekCard(self, subIndex):
        if(self.index + subIndex >= 52):
            return None
        else:
            return self.deckList[self.index + subIndex]

    # **dealCard()**
    # Gets the "top" card object of the deck and edits the deck to
    #   reflect that
    # Args:
    #   N/A
    # Return:
    #   The "top" card object of the deck or None if the deck is empty
    def dealCard(self):
        if(self.index == 52):
            return None
        self.index = self.index + 1
        return self.deckList[self.index - 1]

    # ~~~Object Data Methods~~~ #

    # **size()**
    # Gets the number of cards remaining in the deck
    # Args:
    #   N/A
    # Return:
    #   The number of cards remaining in the deck
    def size(self):
        return 52 - self.index

    # ~~~String Methods~~~ #

    # **toString()**
    # Gets a string representing the whole deck
    # Args:
    #   N/A
    # Return:
    #   A string of the format: "<face> of <suit>\n<face> of <suit>\n..."
    def toString(self):
        ret = ""
        for i in range(self.index, 52):
            ret = ret + self.deckList[i].toString() +"\n"
        return ret;
