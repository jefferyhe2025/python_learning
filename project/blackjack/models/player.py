from project.blackjack.models.card import Card
from project.blackjack.models.hand import Hand


class Player:
    """ 闲家 """
    def __init__(self,name,chips:int):
        self.name = name
        self.hand = Hand()
        self.chips = chips

    def place_bet(self,amount:int) -> None:
        """ 下注 （只对玩家筹码做计算，不涉及bet）"""
        if 0 < amount <= self.chips:
            self.chips -= amount
        else:
            raise ValueError(f'下注无效！')

    def receive_card(self,card:Card) -> None:
        """ 玩家拿牌 """
        self.hand.add(card)

    def clear_hand(self) -> None:
        """ 清空手牌 """
        self.hand.clear()

class Dealer:
    """ 庄家 """
    def __init__(self):
        self.hand = Hand()
        self.hole_revealed = False # 是否已翻开

    def should_hit(self) -> bool:
        """ 软17停止要牌 """
        return self.hand.best_value() < 17

    def reveal(self):
        """ 翻开暗牌 """
        self.hole_revealed = True

    def receive_card(self,card:Card) -> None:
        """ 庄家拿牌 """
        self.hand.add(card)

    def clear_hand(self) -> None:
        """ 清空手牌 """
        self.hole_revealed = False # 清空状态
        self.hand.clear()


