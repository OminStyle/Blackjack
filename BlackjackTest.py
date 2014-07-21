from Blackjack import Blackjack
import unittest


class BlackjackTest(unittest.TestCase):
    def setUp(self):
        self.game = Blackjack()

    def test_setNumOfDecks(self):
        self.game.setNumOfDecks(3)
        self.assertEquals(3, self.game.getNumOfDecks())

    def test_setNumOfPlayers(self):
        self.game.setNumOfPlayers(3)
        self.assertEquals(3, self.game.getNumOfPlayers())

    def test_removePlayer(self):
        self.assertEquals(False, self.game.removePlayer('XYZ'))
        self.assertEquals(True, self.game.removePlayer('Player1'))

if __name__ == '__main__':
    unittest.main()
