import matplotlib.pyplot as plt

from random_walk import RadomWalk

while True:
    # 创建随机行走实例
    rw = RadomWalk(900)
    rw.fill_walk()

    #模拟花粉在水滴表面的运动路径
    plt.style.use('seaborn-v0_8-talk')
    fig, ax = plt.subplots(figsize=(9,9),dpi=100)
    point_numbers = range(rw.num_point)
    ax.plot(rw.x_values, rw.y_values, linewidth=0.4, color='#1f77b4', alpha=0.45)
    ax.scatter(rw.x_values, rw.y_values, c=range(rw.num_point),
               cmap='Blues', s=10, edgecolors='none')
    ax.set_aspect('equal') # 轴刻度相等
    fig.tight_layout(pad=0.2) # 去掉图像周围黑边

    # 突出起终点
    ax.scatter(0, 0, c='green', s=40, zorder=3)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=40, zorder=3)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.axis('off')

    plt.show()

    keep_walking = input('Make another walk?(y/n)')
    if keep_walking == 'n':
        break
