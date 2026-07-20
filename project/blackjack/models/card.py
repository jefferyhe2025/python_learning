from project.blackjack.models.suite import Suite


class Card:
    def __init__(self,suite:Suite,face:int):
        """ 花色和牌面 """
        self.suite = suite
        self.face = face

    def __repr__(self):
        """ 打印牌 """
        _FACES = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{self.suite.symbol}{_FACES[self.face]}'

    def __lt__(self, other:'Card'):
        """ 理牌"""
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.order < other.suite.order

