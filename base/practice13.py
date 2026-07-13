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


"""
面向对象进阶：私有属性和动态属性
"""
#私有属性和动态属性
#在初始化方法中可以将属性添加为私有属性，即不对外公开，外部接口不能调用这个对象的属性。
#例如：self.__name = name,如果调用会引发 ⚠️AttributeError（属性错误）异常

#动态属性
#__slot__=()可以固定类属性，如果动态添加会引发 ⚠️AttributeError异常
#值得注意的是对象的方法本质也是属性，如果给对象发送一个无法接收的消息，引发的异常仍然是AttributeError。
class Fruit:
    """ 新建水果类 """
    __slot__ = ('name','is_ripe') #锁定水果两个属性
    def __init__(self,name,is_ripe):
        self.name = name
        self.is_ripe = is_ripe

    def ripen(self):
        """让水果成熟"""
        self.is_ripe = True
apple = Fruit('苹果',False)
print(f'这是{apple.name}')
# apple.color = '红色' 为苹果动态添加颜色属性

"""
面向对象进阶：静态方法和类方法 -> 将类视为对象
在面向对象中，对象方法、静态方法和类方法都可以通过类名.方法名()来调用
"""
class Triangle:
    """ 三角形 """
    def __init__(self,a,b,c):
        """
        三角形的边长
        """
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a,b,c):
        """ 检查三边能否构成三角形(静态方法) """
        return a + b > c and b + c > a and a + c > b
    # @classmethod
    # def is_valid(cls,a,b,c):
    #     """ 检查三边能否构成三角形(类方法) """
    #     return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        """ 计算三角形的周长 """
        return self.a + self.b + self.c
    @property
    def area(self):
        p = self.perimeter / 2
        return (p*(p-self.a)*(p-self.b)*(p-self.c)) ** 0.5

if Triangle.is_valid(3,4,5):
    t = Triangle(3,4,5)
    # print(f'三角形的周长：{t.perimeter()}') 给对象发消息调用周长方法
    # print(f'三角形的面积：{t.area()}') 给对象发消息调用面积方法
    print(f'三角形的周长：{t.perimeter}') # 调用周长和面积属性
    print(f'三角形的面积：{t.area}')

"""
继承
"""
class Person:
    """ 父类人 """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.age}在吃饭')

    def sleep(self):
        print(f'{self.name}在睡觉')


class Student(Person):
    """ 子类学生 """

    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self,course_name):
        print(f'{self.name}正在学习{course_name}')


class Teacher(Person):
    """ 子类老师 """

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def tech(self, course_name):
        print(f'{self.title}{self.name}正在教授{course_name}')


stu1 = Student('张三', 21)
stu2 = Student('李四', 20)
stu3 = Student('赵六',23)
teacher1 = Teacher('王五', 34, '副教授')
stu1.eat()
stu2.sleep()
stu3.study('C语言程序设计')
teacher1.tech('计算机网络原理')