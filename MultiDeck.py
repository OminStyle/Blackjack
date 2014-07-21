from Card import Card
from Deck import Deck


class MultiDeck(Deck):
    def __init__(self, numOfDecks):
        self.numOfDecks = numOfDecks
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = []
        self.numOfCards = 0
        for x in range(0, self.numOfDecks):
            for suit in Card.getPosSuits():
                for name in Card.getPosNames():
                    self.cards.append(Card(name, suit))
                    self.numOfCards += 1
        self.shuffle()
