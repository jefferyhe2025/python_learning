from enum import Enum


class Suite(Enum):
    """ 花色 """
    SPADE = ('♠', 0)
    HEART = ('♥', 1)
    CLUB = ('♣', 2)
    DIAMOND = ('♦', 3)

    def __init__(self,symbol:str,order:int):
        self.symbol = symbol #花色
        self.order = order # 顺序
