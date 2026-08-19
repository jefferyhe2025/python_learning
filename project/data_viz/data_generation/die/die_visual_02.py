import matplotlib.pyplot as plt
import pandas as pd

from die import Die

# 创建骰子实例
n_rolls = 50000
die_1 = Die()
die_2 = Die()
# 投掷50,000次骰子并保存数据
result = [die_1.roll() + die_2.roll() for _ in range(n_rolls)]

# 用value_counts统计所有出现数据的频率
freq = pd.Series(result).value_counts().sort_index()

plt.figure(figsize=(12,6))
plt.bar(freq.index,freq.values)

plt.title(f'Result of Rolling Two D6 {n_rolls} Times')# 标题
plt.xlabel('Result')
plt.ylabel('Frequencies of Result')
plt.xticks(freq.index)  # 每个整数刻度都显示
plt.tight_layout()
plt.show()