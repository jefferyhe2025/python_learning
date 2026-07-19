"""
从1到100的整数求和

Version: 1.0
"""
import random

num1 = 0
for i in range(100):
    num1 += i
    print(num1)

"""
从1到100的偶数求和
Version: 1.0
"""
num2 =0
for i in range(100):
    if i % 2 == 0:
        num2 += i
        print(num2)


"""
从1到100的偶数求和
Version: 1.1
"""
num3 = 0
for i in range(2,100,2):
    num3 += i
    print(num3)


"""
从1到100的偶数求和
Version: 1.2
"""
print(sum(range(2,100,2)))


# While循环
"""
从1到100的整数求和
Version: 1.1
"""
num4 = 0
while num4 == 100:
    num4 += 1


"""
从1到100的偶数求和

Version: 1.3
"""
total = 0
i = 2
while i <= 100:
    total += i
    i += 2
print(total)


#Flag（标志）
prompt = '\nTell me something,and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program. "

active = True # 设置Flag控制程序是否进行
while active:
    message = input(prompt)

    if message == 'quit':
        active =False
        print('Would you like to replay?')
    else:
        print(message)

# break & continue
"""
从1到100的偶数求和
Version: 1.4
"""
total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)


"""
从1到100的偶数求和
Version: 1.5
"""
total = 0
for i in range(1,101):
    if i % 2 != 0:
        continue
    total += i
print(total)


#嵌套循环
"""
打印乘法口诀表
Version: 1.0
"""
for i  in range(1,10):
    for j in range(1, i +1):
        print(f'{i} x {j} = {i * j}',end='\t')
    print()


#循环的应用
"""
输入一个大于1的正整数判断它是不是素数
Version: 1.0
"""
num = int(input("请输入一个正整数："))
end = int(num ** 0.5)
is_prime = True
for i in range(2,end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')


"""
输入两个正整数求它们的最大公约数
Version: 1.0
"""
a = int(input("请输入一个正整数："))
b = int(input("请输入一个正整数："))
small = min(a,b)
for i in range(1,small+1):
    if a % i == 0 and b % i == 0:
        print(f'a和b的最大公约数为{i}')
        break

"""
输入两个正整数求它们的最大公约数

Version: 1.1
"""
a = int(input("请输入一个正整数："))
b = int(input("请输入一个正整数："))
while a % b != 0:
    a , b = b , a % b
print(f'最大公约数为{b}')

"""
猜数字小游戏

Version: 1.0

"""
num1 = random.randint(1,100)
count = 0
print('猜字游戏开始‼️')
while True:
    num2 = int(input("请输入数字："))
    count += 1
    if num1 > num2:
        print('猜小了')
    elif num1 < num2:
        print('猜大了')
    else:
        print('恭喜猜中了🎉')
        break
print(f'您一共猜了{count}次')


"""
熟食店
"""
sandwich_orders = [
    "tuna sandwich",
    "chicken sandwich",
    "pastrami",
    "pastrami sandwich",
    "veggie sandwich",
    "pastrami",
    "ham sandwich",
    "pastrami",
]
finished_sandwich = []
print('I am sorry,we are out of pastrami.')

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print()
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I am working on  your {sandwich}.')
    finished_sandwich.append(sandwich)

print()
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwich:
    print(sandwich)
