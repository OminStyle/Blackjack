from Card import Card
from Hand import Hand
import unittest


class HandTest(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()
        self.hand.addToHand(Card(2, 'hearts'))
        self.hand.addToHand(Card(9, 'hearts'))

    def test_numOfCards(self):
        self.assertEqual(2, self.hand.numOfCards())

    def test_getValue1(self):
        self.assertEquals(11, self.hand.getValue())

    def test_aceGetValue(self):
        hand = Hand()
        hand.addToHand(Card('A', 'spades'))
        hand.addToHand(Card('A', 'diamonds'))
        self.assertEquals(12, hand.getValue())

    def test_resetHand(self):
        self.hand.resetHand()
        self.assertEquals(0, self.hand.numOfCards())

if __name__ == '__main__':
    unittest.main()
