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
if 18.5 <= bmi <= 25:
    print('你的身材很曼妙😍')
elif bmi < 18.5:
    print('瘦成啥样了😱')
elif bmi < 25:
    print('小心变成大胃袋🤦')
elif bmi < 30:
    print('你成为小胃袋🫢')
else:
    print('已经是合格大胃袋😇')


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
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f'{grade = }')

"""
计算三角形的周长和面积

Version: 1.0
"""
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    s = perimeter / 2
    area  = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'{perimeter = }')
    print(f'{area = }')
else:
    print('三条边不能构成三角形')