"""
输出100以内的素数
"""
for num in range(2,101):
    is_prime = True
    end = int(num ** 0.5)
    for i in range(2,end + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


"""
输出斐波那契数列中的前20个数
"""
a,b=0,1
for _ in range(20):
    a,b=b,a+b
    print(a)

"""
求1000以内的水仙花数
"""
for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == high ** 3 + mid ** 3 + low ** 3:
        print(num)

"""
正整数的反转
"""
num = int(input("请输入一个正整数："))
reversed_num = 0
while num >=0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(f'翻转后的数字:{reversed_num}')

"""
百鸡百钱
"""

for x in range(0,21):
    for y in range(0,34):
        z = 100-x-y
        if x * 5 + y * 3 + z / 3 == 100:
            print(f'公鸡有{x}只,母鸡有{y}只,小鸡有{z}只')

"""
Craps赌博游戏
"""

import random

money = 1000
print(f'🟢你有{money}$')

while money > 0:
    while True:
        debt = int(input("🟡🟡🟡请下注："))
        if 0 < debt <= money:
            break
    print('--------- GAME START‼️---------')
    first_point = random.randrange(1,7) +random.randrange(1,7)
    print(f'玩家摇出{first_point}点')
    if first_point == 7 or first_point == 11:
        print('玩家赢💵\n')
        money += debt
    elif first_point == 2 or first_point== 3 or  first_point == 12:
        print('庄家赢💸\n')
        money -= debt
    else:
        print('--------- 下一轮‼️ ---------')
        while True:
            current_point = random.randrange(1,7) +random.randrange(1,7)
            print(f'玩家摇出{current_point}点')
            if current_point == 7:
                print('庄家赢💸\n')
                money -= debt
                break
            else:
                if current_point == first_point:
                    print('玩家赢💵\n')
                    money += debt
                    break
print('你已经破产了⚠️')
