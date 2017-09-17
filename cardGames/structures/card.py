# class Card
#   Object: Card - Represents a single card (as in a deck of cards)
# Shared class data:
#   faceDict - A dictionary mapping the number representing
#               the face value to a string
#   suitList - A list mapping the number representing
#               the suit value to a string
# Attributes:
#   face - a number 2-14 representative of the face value of the card
#   suit - a number 0-3 representative of the suit of the card
class Card:
    faceDict = {2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight",
                9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King", 14:"Ace"}

    suitList = ["Diamonds", "Hearts", "Spades", "Clubs"]

    # **__init()__**
    # Creates a Card object and throws an error if it was given an invalid argument
    # Args:
    #   face - a number 2-14 representative of the face value of the card
    #   suit - a number 0-3 representative of the suit of the card
    # Return:
    #   N/A
    # RaiseError:
    #   If an invalid argument value was sent
    def __init__(self, face, suit):
        if(suit < 0 or suit > 3):
            raise ValueError("Invalid Suit Number: %i", suit)
        self.suit = suit #0(D), 1(H), 2(S), 3(C)

        if(face < 2 or face > 14):
            raise ValueError("Invalid Face Number: %i", face)
        self.face = face #2-14

    # ~~~String Methods~~~ #

    # **getFaceString()**
    # Returns a string representing the face value of the card
    # Args:
    #   N/A
    # Return:
    #   A string of the face value of the card object
    def getFaceString(self):
        return Card.faceDict[self.face]

    # **getSuitString()**
    # Returns a string representing the suit of the card
    # Args:
    #   N/A
    # Return:
    #   A string of the suit of the card object
    def getSuitString(self):
        return Card.suitList[self.suit]

    # **toString()**
    # Returns a string representing the face and suit of the card
    # Args:
    #   N/A
    # Return:
    #   A string of the suit of the format "<face> of <suit>"
    def toString(self):
        return Card.faceDict[self.face] + " of " + Card.suitList[self.suit]
