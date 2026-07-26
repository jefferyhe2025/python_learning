from enum import Enum, auto
from project.blackjack.models.deck import Deck
from project.blackjack.models.player import Player, Dealer
from project.blackjack.ui.console import ConsoleUI


class Outcome(Enum):
    """ 打印结果"""
    LOSE = auto()
    WIN = auto()
    PUSH = auto()
    BLACKJACK = auto()


class BlackJackGame:
    """ 游戏流程 """
    def __init__(self,deck:Deck,player:Player,dealer:Dealer,ui:ConsoleUI):
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.ui = ui
        self.bet = 0

    def _place_bet(self):
       amount =  self.ui.ask_bet(self.player.chips) #
       self.player.place_bet(amount) # 扣除筹码
       self.bet = amount # 下注
       self.player.clear_hand()
       self.dealer.clear_hand()

    def _ensure_deck(self):
        """ 检查牌堆，避免中途少牌 """
        remaining = len(self.deck.cards) - self.deck.current # 牌堆中剩下的牌
        if remaining < 20:
            self.deck.shuffle()

    def _deal_initial(self):
        """ 先发四张牌"""
        self.player.receive_card(self.deck.deal())
        self.dealer.receive_card(self.deck.deal())
        self.player.receive_card(self.deck.deal())
        self.dealer.receive_card(self.deck.deal())

    def _check_natural(self):
        """ 开局检查是否有自然blackjack"""
        p = self.player.hand.is_blackjack()
        d = self.dealer.hand.is_blackjack()

        if not p and not d:
            # 回合继续
            return False
        if p and d:
            # 平局
            self._settle(Outcome.PUSH)
        elif p:
            # 玩家赢
            self._settle(Outcome.BLACKJACK)
        else:
            # 庄家赢
            self._settle(Outcome.LOSE)
        return True # 结束

    def _player_turn(self):
        """ 玩家回合，True = 爆牌 """
        while True:
            # 临时显示牌面和最佳点数
            print(self.player.hand.my_card, self.player.hand.best_value())
            action = self.ui.ask_hit_or_stand()
            if action == "stand":
                return False
            self.player.receive_card(self.deck.deal())
            if self.player.hand.is_bust:
                return True

    def _dealer_turn(self):
        """ 庄家回合 """
        self.dealer.reveal()
        while self.dealer.should_hit():
            """ 点数不满17，一直hit"""
            self.dealer.receive_card(self.deck.deal())

    def _settle(self,outcome):
        """ 结算bet """
        bet = self.bet
        if outcome is Outcome.LOSE:
            pass #输了扣除bet
        elif outcome is Outcome.WIN:
            self.player.chips += bet * 2 # 退本 + 1:1
        elif outcome is Outcome.PUSH:
            self.player.chips += bet # 退本
        elif outcome is Outcome.BLACKJACK:
            self.player.chips += bet + bet * 3 // 2
        else:
            raise ValueError(outcome)

        print(f"结果：{outcome.name}，本局注：{bet}，剩余筹码：{self.player.chips}")

    def play_round(self):
        """ 单局流程"""
        if self.deck.current == 0:
            # 第一局先洗牌
            self.deck.shuffle()
        self._place_bet() # 下注
        self._ensure_deck()
        self._deal_initial() # 闲家、庄家各发两张牌
        if self._check_natural():
            return
        if self._player_turn():
            # 玩家回合
            self._settle(Outcome.LOSE)
            print('你爆了，扣除赌注！')
            return
        print('stand,庄家回合')
        self._dealer_turn()
        # 比点数
        pv,dv = self.player.hand.best_value(),self.dealer.hand.best_value()

        if self.dealer.hand.is_bust:
            # 庄家爆牌，玩家胜利
            outcome = Outcome.WIN
        elif pv > dv:
            # 玩家点数大，玩家获胜
            outcome = Outcome.WIN
        elif pv < dv:
            # 庄家点数大，玩家输了
            outcome = Outcome.LOSE
        else:
            # 点数相同，平局
            outcome = Outcome.PUSH
        self._settle(outcome) # 结算
