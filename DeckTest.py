from Deck import Deck
import unittest


class DeckTest(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_createDeck(self):
        self.assertEqual(52, self.deck.getNumOfCards())

    def test_shuffle(self):
        testDeck = self.deck.getAllCards()
        compareDeck = []
        for card in testDeck:
            compareDeck.append(card)
        numOfSameCards = 0
        for x in range(0, 52):
            if compareDeck[x] == testDeck[x]:
                numOfSameCards += 1
        self.assertEqual(52, numOfSameCards)
        self.deck.shuffle()
        numOfSameCards = 0
        for x in range(0, 52):
            if compareDeck[x] == testDeck[x]:
                numOfSameCards += 1
        self.assertNotEqual(52, numOfSameCards)

    def test_getNextCard(self):
        newDeck = Deck()
        for x in range(0, 52):
            newDeck.getNextCard()
        with self.assertRaises((NameError)):
            newDeck.getNextCard()

if __name__ == '__main__':
    unittest.main()
