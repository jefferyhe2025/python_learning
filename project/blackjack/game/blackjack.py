from project.blackjack.models.deck import Deck
from project.blackjack.models.player import Player, Dealer
from project.blackjack.ui.console import ConsoleUI


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

    def _settle_player_bust(self):
        print(f'\n你爆了，输掉：{self.bet},还剩筹码：{self.player.chips}')

    def play_round(self):
        """ 单局流程"""
        if self.deck.current == 0:
            # 第一局先洗牌
            self.deck.shuffle()
        self._place_bet()
        self._ensure_deck()
        self._deal_initial()
        if self._player_turn():
            self._settle_player_bust()
            return
        print('stand,庄家回合')

