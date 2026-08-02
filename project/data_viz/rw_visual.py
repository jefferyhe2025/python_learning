import matplotlib.pyplot as plt

from random_walk import RadomWalk

while True:
    # 创建随机行走实例
    rw = RadomWalk(5000)
    rw.fill_walk()

    plt.style.use('seaborn-v0_8-talk')
    fig, ax = plt.subplots(figsize=(9,9),dpi=100)
    point_numbers = range(rw.num_point)
    ax.scatter(rw.x_values, rw.y_values,
               c = point_numbers,cmap='Blues',edgecolors='none',s=15)
    ax.set_aspect('equal')
    fig.tight_layout(pad=0.2)

    # 突出起终点
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_walking = input('Make another walk?(y/n)')
    if keep_walking == 'n':
        break
