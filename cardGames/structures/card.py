class Card:
    #Has attributes "suit" and "face"
    faceDict = {2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight",
                9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King", 14:"Ace"}

    suitList = ["Diamonds", "Hearts", "Spades", "Clubs"]

    def __init__(self, face, suit):
        if(suit < 0 or suit > 3):
            raise ValueError("Invalid Suit Number: %i", suit)
        self.suit = suit #0(D), 1(H), 2(S), 3(C)

        if(face < 2 or face > 14):
            raise ValueError("Invalid Face Number: %i", face)
        self.face = face #2-14

    def toStr(self):
        return Card.faceDict[self.face] + " of " + Card.suitList[self.suit]
