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

def takeTurn(player, deck):
    print("\n%s's Turn:" % player.name)

    print("\n%s" % player.handString())
    print("\nCurrent Maximum Point Evaulation: %d\n" % getHandValue(player.hand))

    action = getResp("What would you like to do? (H - Hit, D - Double Down, S - Stand) ",
                        "That is not an available option.", ['h', 'd', 's'])

    print("Selected Action: " + action)


def main():
    print("Welcome to BlackJack! (Use CTRL+C to end at any time)")

    numPlayers = getNumber("Please Enter the Number of Players: (1-4) ",
                        "Invalid Number of Players.", 1, 4)

    pArr = []
    pArr.append(CardPlayer("Dealer",52,10000))
    print("")
    for i in range(1,numPlayers + 1):
        name = input("Please Enter a Name for Player #%d: " % i)
        pArr.append(CardPlayer(name,52,500))

    print("\nDealing players in...")

    deck = Deck()
    for i in range(0,2):
        for n in pArr:
            n.giveCard(deck.dealCard())

    for i in range(1,numPlayers + 1):
        takeTurn(pArr[i], deck)

    print("")
    for i in pArr:
        print(i.toString() + "\n")



if __name__ == "__main__":
    main()
