import random
from project.blackjack.models.card import Card
from project.blackjack.models.suite import Suite


class Deck:
    def __init__(self):
        # 创建52张牌
        self.cards = [Card(suite,face)
                     for suite in Suite
                     for face in range(14)]
        self.current = 0

    def shuffle(self):
        """ 洗牌 """
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """ 发牌 """
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """ 检查还有没有牌可发 """
        return self.current < len(self.cards)
