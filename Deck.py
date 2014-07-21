from Card import Card
from random import randrange


class Deck():

    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = []
        self.numOfCards = 0
        for suit in Card.getPosSuits():
            for name in Card.getPosNames():
                self.cards.append(Card(name, suit))
                self.numOfCards += 1
        self.shuffle()

    def getNumOfCards(self):
        return self.numOfCards

    def getAllCards(self):
        return self.cards

    def getNextCard(self):
        if self.getNumOfCards() <= 0:
            raise NameError("No more cards in the deck!")
            return
        card = self.cards[self.getNumOfCards()-1]
        self.cards[self.getNumOfCards()-1] = None
        self.numOfCards -= 1
        return card

    def shuffle(self):
        for x in range(0, self.getNumOfCards()):
            temp = self.cards[x]
            randNum = randrange(self.getNumOfCards())
            self.cards[x] = self.cards[randNum]
            self.cards[randNum] = temp
