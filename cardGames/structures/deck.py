from structures.card import Card
from random import randint

class Deck:

    def __init__(self):
        self.index = 0
        self.deckList = []
        for i in [2, 3, 4, 5, 6, 7, 8,
                    9, 10, 11, 12, 13, 14]:
            for j in [0, 1, 2, 3]:
                self.deckList.append(Card(i,j))
        self.shuffle()

    def shuffle(self):
        self.index = 0
        for x in range(0, 50):
            temp = self.deckList[x]
            num = randint((x + 1), 51)
            self.deckList[x] = self.deckList[num]
            self.deckList[num] = temp

    def getTopCard(self):
        self.index = self.index + 1
        return self.deckList[self.index - 1]

    def toStr(self):
        ret = ""
        for i in range(self.index, 52):
            ret = ret + self.deckList[i].toStr() +"\n"
        return ret;
