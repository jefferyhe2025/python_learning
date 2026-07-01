print("hello world")
print("goodbye world")
print("I love python")


"""
author:何冠臻
date：2026/7/01
"""
# hello world
print("你好，世界")

"""
使用变量保存数据并进行加减乘除运算
author:何冠臻
date：2026/7/01
"""
a = 12
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)

"""
使用type函数检查变量的类型
author:何冠臻
date：2026/7/01
"""
a=12
b=3.14
c='hello world'
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

"""
变量的类型转换操作
author:何冠臻
date：2026/7/01
"""
a=12
b=3.14
c='hello world'
d='12'
e='3.14'
f=False
print(float(a))
print(int(b))
print(bool(c))
print(int(d,base=16))
print(float(d))
print(float(e))
print(str(f))


"""
算术运算符
author:何冠臻
date：2026/7/01
"""
print(12+14)
print(12-14)
print(12*14)
print(12/14)
print(12//14)
print(12%14)

"""
算术运算的优先级
author:何冠臻
date：2026/7/01
"""
a=12
b=14
print(a+b**2)
print((a+b)**2)
print((a+b)*5**2)

"""
赋值运算符和复合赋值运算符
author:何冠臻
date：2026/7/01
"""
a=12
b=14
a += b
print(a)
a *= a+b
print(a)

"""
海象运算符
author:何冠臻
date：2026/7/01
"""
print(a:=10)
print(a)

"""
比较运算符和逻辑运算符的使用
author:何冠臻
date：2026/7/01
"""
a=12 == 19
b=13 > 11
c=14 <13
d = a and b
e = not c
print(f'a={a},b={b},c={c},d={d},e={e}')
print(f'f={a or b}')



"""
将华氏温度转换为摄氏温度
author:何冠臻
version：1.0
date：2026/7/01
"""
F = float(input("请输入华氏温度:"))
C = (F-32)/1.8
print('摄氏温度为:%.2f'%C)
#  C = (F-32)/1.8
"""
将华氏温度转换为摄氏温度
author:何冠臻
version：1.1
date：2026/7/01
"""
F = float(input("请输入华氏温度:"))
C = (F-32)/1.8
print(f'摄氏温度为：{C:.2f}')

"""
输入半径计算圆的周长和面积
author:何冠臻
version：1.0
date：2026/7/01
"""
r = float(input("请输入圆的半径："))
perimeter = 2 * 3.14 * r
area = 3.14 * r**2
print('周长：%.2f'%perimeter)
print('面积:%.2f'%r)

"""
输入半径计算圆的周长和面积
author:何冠臻
version：1.1
date：2026/7/01
"""
r = float(input("请输入圆的半径："))
perimeter = 2 * 3.14 * r
area = 3.14 * r**2
print(f'周长：{perimeter:.2f}')
print(f'面积：{area:.2f}')

"""
输入年份，闰年输出True，平年输出False
"""
year = int(input("请输入年份："))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f"is_leap = {is_leap}")
print(f'{is_leap = }')


