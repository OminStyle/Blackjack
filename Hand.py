from Card import Card


class Hand():
    def __init__(self):
        self.cards = []

    def addToHand(self, card):
        self.cards.append(card)

    def numOfCards(self):
        return len(self.cards)

    def showHand(self):
        return cards

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
            if value <= 10:
                numOfAce -= 1
                value += 10     # Originally added 1
        return value
