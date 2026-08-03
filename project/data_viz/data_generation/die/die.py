from random import randint


class Die:
    """ 这是骰子类"""
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """ 掷骰子"""
        return randint(1,self.num_sides)

