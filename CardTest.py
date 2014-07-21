from Card import Card
import unittest


class CardTest(unittest.TestCase):
    def test_standardCard(self):
        card = Card('K', 'hearts')
        self.assertEqual('K', card.getName())
        self.assertEqual('hearts', card.getSuit())
        self.assertEqual(10, card.getValue())

    def test_badName(self):
        with self.assertRaises((NameError)):
            Card('B', 'spades')

    def test_badSuits(self):
        with self.assertRaises((NameError)):
            Card('B', 'golds')

if __name__ == '__main__':
    unittest.main()
