
class Card():

    def __init__(self, name, suit):
        posNames = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        posSuits = ['spades', 'hearts', 'diamonds', 'clubs']
        if name not in posNames:
            raise NameError("'" + name +
                            "' is not found in standard playing cards.")
        if suit not in posSuits:
            raise NameError("'" + suit +
                            "' is not found in standard playing cards.")
        self.name = name
        self.suit = suit
        if name == 'A':
            self.value = 1
        elif name == 'J' or name == 'Q' or name == 'K':
            self.value = 10
        else:
            self.value = value

    def getName(self):
        return self.name

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value
