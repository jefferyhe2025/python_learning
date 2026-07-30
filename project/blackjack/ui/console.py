class ConsoleUI:
    """ 打印界面 """
    def ask_bet(self, chips):
        while True:
            s = input(f'\n您的筹码为{chips},请下注： ')
            try:
                amount = int(s)
            except ValueError:
                print(f'\n请输入整数！')
                continue
            if 0 < amount <= chips:
                return amount
            print('\n下注额不能超过您当前的筹码且必须是正数。')

    def ask_continue(self) -> bool:
        """ 是否继续游戏"""
        while True:
            s = input(f'\n是否继续游戏?(y/n): ').strip().lower()
            if s in ('y','yes','是'):
                return True
            if s in ('n','no','否'):
                return False
            print(f'\n请输入y/n')

    def ask_hit_or_stand(self):
        while True:
            s = input("hit/stand: ").strip().lower()
            if s not in ('hit','stand'):
                print(f'请输入hit/stand')
                continue
            return s

    def show_table(self, player_cards, player_value, dealer_upcard):
        """ 打印玩家回合的牌桌 """
        print(f'\n您的手牌：{player_cards}, 最佳点数：{player_value}')
        print(f'庄家明牌：{dealer_upcard}')

    def show_dealer_hand(self, cards, value):
        """ 打印庄家回合的牌桌 """
        print(f'\n庄家明牌！')
        print(f'庄家手牌：{cards},最佳点数：{value}')

    def show_round_result(self, outcome, bet, chips, note=None):
        """ 打印筹码结算 """
        if note:
            print(f'\n{note}')
        print(f'\n结果：{outcome.name}，本局注：{bet}，剩余筹码：{chips}')

    def show_session_end(self, reason, chips):
        """ 游戏结束 """
        if reason == 'quit':
            print(f'\n您已退出游戏,剩余筹码{chips}')
        elif reason == 'bankrupt':
            print(f'\n您已破产！')
        else:
            print(f'\n游戏结束，剩余筹码{chips}')
