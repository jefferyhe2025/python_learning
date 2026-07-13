"""
面向对象
"""
import time


#定义一个学生类
class Student:
    def __init__(self,name,age):
        """
        初始化
        :param name: 姓名
        :param age: 年龄
        """
        self.name = name
        self.age = age

    def study(self,course_name):
        """
        学习方法
        :param course_name: 学习的课程
        """
        print(f'学生正在学习：{course_name}')

    def play(self):
        """ 玩乐方法 """
        print('学生正在玩耍')

#创建和使用对象
student1 = Student('何冠臻',20)
Student.study(student1,'C语言程序设计')
student2 = Student('郭顶',42)
student2.play()

#📝面向对象的三大支柱：封装、继承和多态
#💻面向对象的三步法：1.定义类 2.创建对象 3. 给对象发消息

"""
面向对象案例
例一：时钟
"""

class Clock:
    """ 数字时钟🕰️"""
    def __init__(self,hour,minute,second):
        """
        初始化
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        """ 走字 """
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """ 展示时间 """
        print(f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}')

#创建时钟对象
clock1 = Clock(23,59,58)
# while True:
#     clock1.show()
#     #模拟时钟停顿1秒
#     time.sleep(1)
#     clock1.run()

"""
例2：平面上的点
"""
class Point:
    """ 平面上的点 """
    def __init__(self,x=0,y=0):
        """
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x,self.y = x,y

    def distance_to(self,other):
        """
        计算点到另外一个点的距离
        :param other: 坐标系中另外一个点
        :return: 两点间的距离
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** 0.5

    def __str__(self):
        """ 魔法方法（可读字符串表示，常用于print（对象）"""
        return f'({self.x},{self.y})'

#创建平面上的两点
p1 = Point(3,4)
p2 = Point(5,6)
print(p1,p2) # 调用魔法方法
print(f'p1到p2的距离为：{p1.distance_to(p2):.2f}')
