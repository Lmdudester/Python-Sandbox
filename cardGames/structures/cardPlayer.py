from structures.card import Card

# class CardPlayer
#   Object: CardPlayer - represents a player in a card game
# Shared class data:
#   N/A
# Attributes:
#   hand - A list containing all the cards the playe currently
#           has in hand
#   name - A string holding the name of the given player
#   maxHandSize - The maximum number of cards the player can have
#                   in hand at any point in time
#   startMoney - The amount of money the player should start with
class CardPlayer:

    # **__init()__**
    # Creates a CardPlayer object
    # Args:
    #   name - a string holding the name of the given player
    #   maxHandSize - the maximum number of cards the player can have
    #                   in hand at any point in time
    #   startMoney - the amount of money the player should start with
    # Return:
    #   N/A
    def __init__(self, name, maxHandSize, startMoney):
        self.hand = []
        self.name = name
        self.maxHandSize = maxHandSize
        self.bank = startMoney

    # ~~~Hand Methods~~~ #

    # **giveCard()**
    # Places a card into the players hand
    # Args:
    #   cardD - the card to be put into the player's hand
    # Return:
    #   None if the card was successfully placed
    #   cardD if it would not fit in the hand
    def giveCard(self, cardD):
        if(len(self.hand) + 1 > self.maxHandSize):
            return cardD
        self.hand.append(cardD)
        return None

    # **discardOne()**
    # Discards a specific card from the player's hand (by index)
    # Args:
    #   index - the index of the card being discarded
    # Return:
    #   None if the given index was out of range
    #   The card that was discarded if one was discarded
    def discardOne(self, index):
        if(0 > index or index >= len(self.hand)):
            return None
        return self.hand.pop(index)

    # **discardHand()**
    # Discards a players whole hand
    # Args:
    #   index - the index of the card being discarded
    # Return:
    #   None if the given index was out of range
    #   The card that was discarded if one was discarded
    def discardHand(self):
        self.hand = []

    # ~~~Balance Methods~~~ #

    # **alterBalance()**
    # Change the value of the players bank
    # Args:
    #   value - the value to add to the balance
    #           (use negative value to subtract)
    # Return:
    #   N/A
    def alterBalance(self, value):
        self.bank = self.bank + value

    # ~~~String Methods~~~ #

    # **toString()**
    # Returns a string representing the player's data
    # Args:
    #   N/A
    # Return:
    #   A string of the format --> 
    #       "Name: <name>\nBank: <bank>\nHand: \n<card>\n<card>..."
    def toString(self):
        ret = "Name: " + self.name + "\nBank: $" + str(self.bank) + "\nHand:"
        for i in self.hand:
            ret = ret + "\n" + i.toString()
        return ret
