from Card import Card
from Player import Player
import unittest


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player('Charles')
        self.player.addToHand(Card(2, 'hearts'))
        self.player.addToHand(Card(9, 'hearts'))

    def test_numOfCards(self):
        self.assertEquals(2, self.player.numOfCards())

    def test_getValue1(self):
        self.assertEquals(11, self.player.getValue())

    def test_aceGetValue(self):
        player = Player('Charles')
        player.addToHand(Card('A', 'spades'))
        player.addToHand(Card('A', 'diamonds'))
        self.assertEquals(12, player.getValue())

    def test_showCredits(self):
        self.assertEquals(100, self.player.showCredits())

    def test_addCredits(self):
        self.player.addCredits(100)
        self.assertEquals(200, self.player.showCredits())

    def test_bet(self):
        self.assertEquals(True, self.player.bet(10))
        self.assertEquals(90, self.player.showCredits())
        self.assertEquals(False, self.player.bet(91))

    def test_getName(self):
        self.assertEquals('Charles', self.player.getName())

if __name__ == '__main__':
    unittest.main()
