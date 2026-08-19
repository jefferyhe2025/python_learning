import plotly.express as px
import pandas as pd

from die import Die

# 创建骰子实例
n_rolls = 50000
die_1 = Die()
die_2 = Die(10)
# 投掷50,000次骰子并保存数据
result = [die_1.roll() * die_2.roll() for _ in range(n_rolls)]

# 用value_counts统计所有出现数据的频率
freq = pd.Series(result).value_counts().sort_index()

title = f'Result of Rolling D6 and D10 {n_rolls} Times' # 标题
label = {'x':'Result','y':'Frequencies of Result'} # 坐标轴名称
fig = px.bar(x=freq.index,y=freq.values,title=title,labels=label)

fig.update_layout(
    xaxis_dtick=1,
    xaxis_tickangle=0,
    xaxis_tickfont=dict(size=8)
) # 柱形图下标


fig.show(renderer="browser")