from MultiDeck import MultiDeck
import unittest


class MultiDeckTest(unittest.TestCase):

    def setUp(self):
        self.deck = MultiDeck(3)

    def test_createDeck(self):
        self.assertEqual(156, self.deck.getNumOfCards())

    def test_shuffle(self):
        testDeck = self.deck.getAllCards()
        compareDeck = []
        for card in testDeck:
            compareDeck.append(card)
        numOfSameCards = 0
        for x in range(0, 156):
            if compareDeck[x] == testDeck[x]:
                numOfSameCards += 1
        self.assertEqual(156, numOfSameCards)
        self.deck.shuffle()
        numOfSameCards = 0
        for x in range(0, 156):
            if compareDeck[x] == testDeck[x]:
                numOfSameCards += 1
        self.assertNotEqual(156, numOfSameCards)

if __name__ == '__main__':
    unittest.main()
