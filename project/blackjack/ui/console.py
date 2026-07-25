class ConsoleUI:
    """ 打印界面 """
    def ask_bet(self, chips):
        # 能跑通后再改成 while True + input 校验
        return 100

    def ask_hit_or_stand(self):
        s = input("hit/stand: ").strip().lower()
        return s