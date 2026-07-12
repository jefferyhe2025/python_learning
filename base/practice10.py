from random import randint
from math import factorial as f

"""
输入m和n，计算组合数C(m,n)的值
version 1.0
"""
#引入函数

m = int(input('请输入m的值（m > n）:'))
n = int(input('请输入n的值：'))

#计算m的阶乘
fm = 1
for num in range(2,m+1):
    fm *= num
#计算n的阶乘
fn = 1
for num in range(2,n+1):
    fn *= num
#计算m-n的阶乘
fk = 1
for num in range(2,m-n+1):
    fk *= num

print(fm // fn // fk)

"""
输入m和n，计算组合数C(m,n)的值
Version: 1.1
"""
#使用函数重构
def fac(n):
    result = 1
    for n in range(2,n + 1):
        result *= n
    return  result

m = int(input('请输入m的值（m > n）:'))
n = int(input('请输入n的值：'))
print(fac(m) // fac(n) // fac(m-n))

"""
输入m和n，计算组合数C(m,n)的值
Version: 1.2
"""
m = int(input('请输入m的值（m > n）:'))
n = int(input('请输入n的值：'))
print(f(m) // f(n) // f(m-n))

"""
函数的参数：位置参数和关键字参数
"""
def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
#位置参数
print(make_judgement(2,4,8))
#关键字参数
print(make_judgement(c=4,a=8,b=5))
#强制位置参数
def make_judgement_1(a, b, c,/):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
print(make_judgement_1(1,2,3))
#强制命名参数
def make_judgement_2(*,a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
print(make_judgement_2(a=1,b=2,c=3))

#参数的默认值
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total
print(roll_dice())
print(roll_dice(3))
# 可变参数
def add(*agrs):
    total = 0
    for val in agrs:
        if type(val) in (float,int):
            total += val
    return total
print(add(1,2,3))
print(add(1,True,'hello',3.25,7))
#可变关键字参数
def foo(*args,**kwargs):
    print(args)
    print(kwargs)
foo(3, 2.1, True, name='冠臻', age=21, gpa=3.95)

