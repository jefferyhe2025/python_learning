"""
BMI计算器
Version: 1.0
"""
weight = float(input("请输入你的体重（kg）："))
height = float(input("请输入你的身高（cm）："))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18.5:
    print('你的身材很曼妙~')


"""
BMI计算器
Version: 1.1
"""
weight = float(input("请输入你的体重（kg）："))
height = float(input("请输入你的身高（cm）："))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18.5:
    print('你的身材很曼妙~')
else:
    print('你的身材一般般~')

"""
BMI计算器
Version: 1.2
"""
weight = float(input("请输入你的体重（kg）："))
height = float(input("请输入你的身高（cm）："))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if 18.5 < bmi <= 25:
    print('你的身材很曼妙😍')
elif 25 < bmi <= 30:
    print('小心变成大胃袋🤦')
elif 30 < bmi:
    print('合格的大胃袋😇')
else:
    print('瘦成啥了')


"""
分段函数求值

Version: 1.0
"""

x = int(input("请输入x的值："))
if x < -1:
    y = 5 * x + 3
    print(f'{y = }')
elif x > 1:
    y = 3 * x - 5
    print(f'{y = }')
else:
    y = x + 2
    print(f'{y = }')

"""
分段函数求值

Version: 1.1
"""
x = int(input("请输入x的值："))
if x < -1:
    y = 5 * x + 3
    print(f'{y = }')
else:
    if x > 1:
        y = 3 * x - 5
    else:
        y = x + 2
print(f'{y = }')

"""
百分制成绩转换为等级制成绩

Version: 1.0
"""
score = int(input("请输入你的成绩:"))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

"""
计算三角形的周长和面积

Version: 1.0
"""
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a + b > c and a + c > b and b + c > a:
    perimeter  = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'{perimeter = :.1f}')
    print(f'{area = :.1f}')
else:
    print('三边不能构成三角形')