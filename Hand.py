from Card import Card


class Hand(object):
    def __init__(self):
        self.cards = []

    def addToHand(self, card):
        self.cards.append(card)

    def numOfCards(self):
        return len(self.cards)

    def showHand(self):
        return cards

    def printHand(self):
        for card in self.cards:
            print(str(card.getName()) + " of " + card.getSuit())

    def getValue(self):
        value = 0
        numOfAce = 0
        for card in self.cards:
            if card.getName() == 'A':
                numOfAce += 1
                value += 1
            elif card.getName() == 'J' or card.getName() == 'Q' \
                    or card.getName() == 'K':
                value += 10
            else:
                value += card.getName()
        if numOfAce:
            if value <= 11:
                numOfAce -= 1
                value += 10     # Originally added 1 so 1 + 10 = 11
        return value

    def resetHand(self):
        self.cards = []
