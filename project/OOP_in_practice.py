"""
扑克牌游戏：扑克只有52张牌（没有大小王），
游戏需要将 52 张牌发到 4 个玩家的手上，每个玩家手上有 13 张牌，
按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能。
"""
import random
from abc import ABCMeta,abstractmethod
from enum import Enum


class Suite(Enum):
    """ 花色的文字符号 """
    SPADE,HEART,CLUB,DIAMOND = range(4) #用枚举的方式将文字符号替代数字🔢

class Card:
    def __init__(self,suite,face):
        """
        :param suite: 花色
        :param face:  点数
        """
        self.suite = suite
        self.face = face

    def __repr__(self):
        """ 与__str__类似，打印对象内容（面向开发者）"""
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self, other):
        """ 比较牌的大小 """
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value

class Decker:
    """ 牌堆相关的功能 """
    def __init__(self):
        """ 创建52张牌，记录发牌位置"""
        self.cards = [Card(suite,face)
                      for suite in Suite
                      for face in range(1,14)]
        self.current = 0

    def shuffle(self) -> None:
        """ 洗牌 """
        self.current = 0
        random.shuffle(self.cards) #返回值为None，不用return

    def deal(self):
        """ 发牌 """
        card = self.cards[self.current]
        self.current += 1
        return  card

    @property
    def has_next(self):
        """ 判断还有没有牌可以发 """
        return self.current < len(self.cards)

class Player:
    """ 玩家 """
    def __init__(self,name):
        self.name = name
        self.cards = []

    def get_one(self,card) -> None:
        """ 摸牌 """
        self.cards.append(card) #返回值为None，不用return

    def arrange_card(self) -> None:
        """ 理牌 """
        self.cards.sort() #返回值为None，不用return
        #📝这里整理排序会对牌堆中Card类进行比大小，故而在Card类中添加了__lt__魔法方法

decker = Decker()
decker.shuffle()
players = [Player('张三'),Player('李四'),Player('王五'),Player('赵六')]
#发牌
for _ in range(13):
    for player in players:
        player.get_one(decker.deal())
#玩家理牌
for player in players:
    player.arrange_card()
    print(f'{player.name}:',end='')
    print(player.cards)

"""
工资结算系统
"""
#要求：某公司有三种类型的员工，分别是部门经理、程序员和销售员。
# 需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
# 其中，部门经理的月薪为固定 15000 元；
# 程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；
# 销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。
class Employee(metaclass=ABCMeta):
    """ 抽象父类员工"""
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    """ 部门经理 """
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """ 程序员 """
    def __init__(self,name,work_hours):
        super().__init__(name)
        self.work_hours = work_hours

    def get_salary(self):
        return 200 * self.work_hours

class Salesman(Employee):
    """ 销售 """
    def __init__(self,name,sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05

#创建员工实例
emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]
for emp in emps:
    if isinstance(emp,Programmer): #判断员工类型
        emp.work_hours = int(input('请输入工作时间：'))
    elif isinstance(emp,Salesman):
        emp.sales = int(input('请输入销售额：'))
    print(f'{emp.name}本月工资为￥{emp.get_salary():.2f}元')





