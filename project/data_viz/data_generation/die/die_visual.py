import plotly.express as px

from die import Die

# 创建骰子实例
die_1 = Die(6)
die_2 = Die(10)
# 投掷50,000次骰子并保存数据
result = [die_1.roll() * die_2.roll() for roll_num in range(50_000)]

# 计算每个点数的出现的总次数
poss_result = range(1,die_1.num_sides * die_2.num_sides +1)
frequencies = [result.count(value) for value in poss_result]

title = 'Result of Rolling D6 and D10 50,000 Times' # 标题
label = {'x':'Result','y':'Frequencies of Result'} # 坐标轴名称
fig = px.bar(x=poss_result,y=frequencies,title=title,labels=label)

fig.update_layout(xaxis_dtick=1) # 柱形图下标

fig.show(renderer="browser")