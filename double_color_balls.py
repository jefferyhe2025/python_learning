"""
双色球随机选号程序
version1.0
"""
import random
import rich
from rich import Console
from rich.ansi import console
from rich.table import Table

red_balls = list(range(1,34))
selected_balls = []

for _ in range(6):
    index = random.randrange(len(red_balls))
    selected_balls.append(red_balls.pop(index))

selected_balls.sort()

for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')

blue_ball = random.randint(1,17)
print(f'\033[034m{blue_ball:0>2d}\033[0m')

"""
双色球随机选号程序
version1.1
"""
red_balls = [i for i in range(34)]
blue_balls = [i for i in range(17)]

selected_balls = random.sample(red_balls,6)
selected_balls.sort()

for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m',end=' ')

blue_ball = random.choice(blue_balls)
print(f'\033[034m{blue_ball:0>2d}\033[0m')

"""
双色球随机选号程序
version1.2
"""
# 创建控制台，强制启用颜色（PyCharm Run 窗口也能显示）
console = Console(color_system="standard", force_terminal=True)

n = int(input('需要生成几注号码：'))
red_balls = [i for i in range(34)]
blue_balls = [i for i in range(17)]


table = Table(show_header=True) #创建表格并编写表头
for col_name in ('序号','红球','蓝球'):
    table.add_column(col_name,justify='center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    table.add_row(
        str(i+1),
        f'[red]{" ".join(f'{ball:0>2d}'for ball in selected_balls)}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )
console.print(table)