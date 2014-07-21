from Card import Card
import unittest


class CardTest(unittest.TestCase):
    def test_standardCard(self):
        card1 = Card('K', 'hearts')
        self.assertEqual('K', card1.getName())
        self.assertEqual('hearts', card1.getSuit())
        self.assertEqual(10, card1.getValue())
        card2 = Card(2, 'spades')
        self.assertEqual(2, card2.getValue())

    def test_badName(self):
        with self.assertRaises((NameError)):
            Card('B', 'spades')

    def test_badSuits(self):
        with self.assertRaises((NameError)):
            Card('B', 'golds')

if __name__ == '__main__':
    unittest.main()
