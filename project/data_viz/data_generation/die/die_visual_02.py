import matplotlib.pyplot as plt

from die import Die

# 创建骰子实例
die_1 = Die(6)
die_2 = Die(6)
# 投掷50,000次骰子并保存数据
result = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]

# 计算每个点数的出现的总次数
poss_result = range(2,die_1.num_sides + die_2.num_sides +1)
frequencies = [result.count(value) for value in poss_result]

plt.figure(figsize=(12,6))
plt.bar(poss_result,frequencies)

plt.title('Result of Rolling Two D6 50,000 Times')# 标题
plt.xlabel('Result')
plt.ylabel('Frequencies of Result')
plt.xticks(poss_result)  # 每个整数刻度都显示
plt.tight_layout()
plt.show()