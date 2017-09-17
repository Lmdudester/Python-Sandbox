from structures.card import Card
from structures.deck import Deck
from structures.cardPlayer import CardPlayer

def getNumber(promptStr, failStr, lowB, upB):
    num = input(promptStr)

    while True:
        try:
            if(int(num) >= lowB and int(num) <= upB):
                break
            print(failStr + "\n")
            num = input(promptStr)
        except:
            print(failStr + "\n")
            num = input(promptStr)

    return int(num)

def getResp(promptStr, failStr, allowedResp):
    resp = input(promptStr)

    while True:
        for i in allowedResp:
            if(resp.lower() == i):
                return resp
        print(failStr + "\n")
        resp = input(promptStr)

def getHandValue(hand):
    num = 0
    aceCount = 0
    for i in hand:
        if(i.face < 11):
            num = num + i.face
        elif(i.face < 14):
            num = num + 10
        else:
            aceCount = aceCount + 1

    if(aceCount >= 1):
        while(num + 11 <= 21):
            aceCount = aceCount - 1
            num = num + 11
        num += aceCount

    return num

def takeTurn(player, deck, bet):
    print("\n%s's Turn:" % player.name)

    print("\n%s" % player.handString())
    print("\nCurrent Maximum Point Evaulation: %d\n" % getHandValue(player.hand))

    if(getHandValue(player.hand) == 21):
        print("\n%s HAS BLACKJACK!\n" % player.name.upper())
        return bet

    promptStr = "What would you like to do? (H - Hit, "
    options = ['s', 'h']

    if(player.bank - bet >= 0):
        options.append('d')
        promptStr = promptStr + "D - Double Down, "
    else:
        print("\nInsufficient funds to double down.\n")

    promptStr = promptStr + "S - Stand) "

    action = getResp(promptStr, "That is not an available option.", options)

    #Hit
    while(action == 'h'):
        player.giveCard(deck.dealCard())

        print("\n%s" % player.handString())
        print("\nCurrent Maximum Point Evaulation: %d\n" % getHandValue(player.hand))

        if(getHandValue(player.hand) > 21):
            print("%s Busted!" % player.name)
            return -1*bet

        action = getResp(promptStr, "That is not an available option.", options)

    #Double Down
    if(action == 'd'):
        player.giveCard(deck.dealCard())

        print("\n%s" % player.handString())
        print("\nCurrent Maximum Point Evaulation: %d\n" % getHandValue(player.hand))

        player.bank = player.bank - bet
        if(getHandValue(player.hand) > 21):
            print("%s Busted!" % player.name)
            return -2*bet

        bet = bet*2

    #Reguardless (Stay)
    if(getHandValue(player.hand) == 21):
        print("\n%s HAS BLACKJACK!\n" % player.name.upper())

    return bet


def main():
    print("Welcome to BlackJack! (Use CTRL+C to end at any time)")

    numPlayers = getNumber("Please Enter the Number of Players: (1-4) ",
                        "Invalid Number of Players.", 1, 4)

    #Create Players
    pArr = []
    pArr.append(CardPlayer("Dealer",52,10000))
    print("")
    for i in range(1,numPlayers + 1):
        name = input("Please Enter a Name for Player #%d: " % i)
        pArr.append(CardPlayer(name,52,500))

    #Create Deck
    deck = Deck()

    #Place Bets
    betArr = [0, 0, 0, 0, 0]
    print("")
    for i in range(1,numPlayers + 1):
        betArr[i] = getNumber("%s Please Make a Bet: (2-%d)" % (pArr[i].name, pArr[i].bank),
                                "Invalid Bet.", 2, pArr[i].bank)
        pArr[i].bank = pArr[i].bank - betArr[i]

    print("\nDealing players in...")

    #Reset
    deck.shuffle()
    for i in pArr:
        i.discardHand()

    #Deal Deck
    for i in range(0,2):
        for n in pArr:
            n.giveCard(deck.dealCard())

    #Take Turns
    for i in range(1,numPlayers + 1):
        betArr[i] = takeTurn(pArr[i], deck, betArr[i])

    #Dealer's Turn
    while(getHandValue(pArr[0].hand) < 17):
        pArr[0].giveCard(deck.dealCard())

    print("\nDealer's Turn:")

    print("\n%s" % pArr[0].handString())
    print("\nCurrent Maximum Point Evaulation: %d\n" % getHandValue(pArr[0].hand))

    if(getHandValue(pArr[0].hand) > 21):
        print("Dealer Busted!")
        betArr[0] = -1


    #Payout
    for i in range(1,numPlayers + 1):
        if(betArr[0] == -1 and betArr[i] > 0):
            print("%s wins $%d" % (pArr[i].name, betArr[i]))
            pArr[i].bank = pArr[i].bank + betArr[i]*2
        elif(getHandValue(pArr[0].hand) < getHandValue(pArr[i].hand) and betArr[i] > 0):
            print("%s wins $%d" % (pArr[i].name, betArr[i]))
            pArr[i].bank = pArr[i].bank + betArr[i]*2
        elif(getHandValue(pArr[i].hand) == getHandValue(pArr[0].hand) and betArr[i] > 0):
            print("%s breaks even." % pArr[i].name)
            pArr[i].bank = pArr[i].bank + betArr[i]
        elif(betArr[i] < 0):
            print("%s loses $%d" % (pArr[i].name, -1*betArr[i]))
        else:
            print("%s loses $%d" % (pArr[i].name, betArr[i]))

    print("")
    for i in pArr:
        print(i.toString() + "\n")



if __name__ == "__main__":
    main()
