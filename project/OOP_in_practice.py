"""
扑克牌游戏：扑克只有52张牌（没有大小王），
游戏需要将 52 张牌发到 4 个玩家的手上，每个玩家手上有 13 张牌，
按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能。
"""
from enum import Enum


class Suite(Enum):
    """ 花色的文字符号 """
    SPADE,HEART,CLUB,DIMOND = range(4) #用枚举的方式将文字符号替代数字🔢

for suite in Suite:
    print(f'{suite}: {suite.value}')

class Card:
    def __init__(self,suite,face):
        """
        :param suite: 花色
        :param face:  点数
        """
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1)  # ♠5
print(card2)  # ♥K