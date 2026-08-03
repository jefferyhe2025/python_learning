from random import choice

class RadomWalk:
    """ 随机行走"""
    def __init__(self,num_point=5000):
        self.num_point = num_point

        # 设置初始坐标（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """ 游走的距离和方向"""
        direction = choice([-1, 1])
        distance = choice([1, 2, 3, 4,])
        return direction * distance

    def fill_walk(self):
        """ 计算随机游走包含的所有点"""
        while len(self.x_values) < self.num_point:
            """ 游走范围不能超过指定范围"""
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的坐标
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # 将坐标保存在列表中
            self.x_values.append(x)
            self.y_values.append(y)
