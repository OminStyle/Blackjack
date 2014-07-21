from MultiDeck import MultiDeck
from Hand import Hand
from Player import Player


class Blackjack(object):
    def __init__(self):
        self.players = []
        self.setNumOfPlayers(1)
        self.setNumOfDecks(1)
        self.dealer = Hand()

    def setNumOfDecks(self, numOfDecks):
        self.numOfDecks = numOfDecks
        self.deck = MultiDeck(self.numOfDecks)

    def setNumOfPlayers(self, numOfPlayers):
        self.numOfPlayers = numOfPlayers
        self.players = []
        for i in range(1, self.getNumOfPlayers()+1):
            self.players.append(Player("Player"+str(i)))

    def removePlayer(self, playerName):
        for player in self.players:
            if player.getName() == playerName:
                self.players.remove(player)
                self.numOfPlayers -= 1
                return True
        return False

    def setUp(self):
        correctInput = False
        numOfPlayers = 0
        while not correctInput:
            input = raw_input("please enter number of players: ")
            try:
                correctInput = True
                numOfPlayers = int(input)
            except ValueError:
                print("That's not a number!")
                correctInput = False
                continue
            else:
                if numOfPlayers > 0:
                    self.setNumOfPlayers(numOfPlayers)
                else:
                    correctInput = False

        correctInput = False
        numOfDecks = 0
        while not correctInput:
            input = raw_input("please enter number of decks: ")
            try:
                correctInput = True
                numOfDecks = int(input)
            except ValueError:
                print("That's not a number!")
                correctInput = False
                continue
            else:
                if numOfDecks > 0:
                    self.setNumOfDecks(numOfDecks)
                else:
                    correctInput = False

    def startNewGame(self):
        if self.deck.getNumOfCards() < self.getNumOfDecks() * 52 / 2:
            self.deck.shuffle()
        self.dealer.resetHand()
        for player in self.players:
            player.resetHand()
        self.playersBet()
        self.dealCards()
        self.dealCards()
        for player in self.players:
            print(player.getName() + "'s hand: ")
            player.printHand()
        print("Dealer's hand:")
        self.dealer.printHand()
        print("\n\n")
        self.gameplay()

    def gameplay(self):
        for player in self.players:
            print(player.getName() + "'s hand: ")
            player.printHand()
            hold = False
            while player.getValue() < 21 and not hold:
                input = raw_input("Would you like to hit? (y/n): ")
                if input == 'y':
                    nextCard = self.deck.getNextCard()
                    player.addToHand(nextCard)
                    player.printHand()
                if input == 'n':
                    hold = True
            print('\n')
        while self.dealer.getValue() <= 17:
            nextCard = self.deck.getNextCard()
            self.dealer.addToHand(nextCard)
        print("Dealer's final hand:")
        self.dealer.printHand()
        self.payout()
        input = ''
        while input != 'y' and input != 'n':
            input = raw_input("Would you like to play again? (y/n): ")
        if input == 'y':
            self.startNewGame()

    def playersBet(self):
        self.bets = {}
        if self.numOfPlayers <= 0:
            print('Not enough players...')
            return
        for player in self.players:
            if player.showCredits() > 0:
                correctAmount = False
                amount = 0
                while not correctAmount:
                    input = raw_input(player.getName() +
                                      " please enter betting amount: ")
                    try:
                        correctAmount = True
                        amount = int(input)
                    except ValueError:
                        print("That's not a number!")
                        correctAmount = False
                        continue
                    else:
                        correctAmount = player.bet(amount)
                self.bets[player.getName()] = amount
            else:
                self.removePlayer(player.getName())

    def payout(self):
        for player in self.players:
            if (player.getValue() <= 21 and
                player.getValue() > self.dealer.getValue()) or\
                    (player.getValue() <= 21 and self.dealer.getValue() > 21):
                player.addCredits(self.bets[player.getName()]*2)
            elif player.getValue() == self.dealer.getValue():
                player.addCredits(self.bets[player.getName()])
        for player in self.players:
            print(player.getName() + " has " + str(player.showCredits()) +
                  " credits.")

    def dealCards(self):
        for player in self.players:
            nextCard = self.deck.getNextCard()
            player.addToHand(nextCard)
        nextCard = self.deck.getNextCard()
        self.dealer.addToHand(nextCard)

    def getNumOfPlayers(self):
        return self.numOfPlayers

    def getNumOfDecks(self):
        return self.numOfDecks

if __name__ == '__main__':
    game = Blackjack()
    game.setUp()
    game.startNewGame()
