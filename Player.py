from Hand import Hand


class Player(Hand):
    def __init__(self, name):
        self.name = name
        self.credits = 100
        super(Player, self).__init__()

    def showCredits(self):
        return self.credits

    def addCredits(self, credits):
        self.credits += credits

    def bet(self, amount):
        if amount <= 0:
            print('You cannot bet negative amount!')
            return False
        if self.credits - amount < 0:
            print('You do not enough credits!')
            return False
        else:
            self.credits -= amount
            return True

    def getName(self):
        return self.name
