from project.blackjack.models.card import Card

class Hand:
    """ 持有手牌 + 点数计算器 """
    def __init__(self):
        self.my_card = [] # 持有手牌列表

    def add(self,card) -> None:
        """ 加牌 """
        self.my_card.append(card)

    def clear(self) -> None:
        """ 局间清空 """
        self.my_card.clear()

    def base_point(self,card:Card) -> int:
        """ A只算1点 """
        if card.face == 1:
            return 1
        if card.face > 10:
            return 10
        return card.face


    def best_value(self) -> int:
        """
        最优点数
        """
        total = 0
        ace_count = 0
        #没有牌返回0
        if not self.my_card:
            return 0
        # 基础分(A只算1点)
        for card in self.my_card:
            total += self.base_point(card)
            if card.face == 1: # 牌面A的值为1
                ace_count += 1
        # 若total + 10 < 21 ,则将A变为11（一般只会将A抬一次）
        while total + 10 <= 21 and ace_count > 0:
            total += 10
            ace_count -=1
        return total

    @property
    def is_bust(self):
        """ 有没有超出21点 """
        return self.best_value() > 21

    def is_blackjack(self):
        """是不是正好两张且相加为21点 """
        return len(self.my_card) == 2 and self.best_value() == 21
