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
        # 是否继续游戏
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

