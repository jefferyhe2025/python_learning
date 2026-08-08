import pandas as pd

import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('../weather_data/sitka_weather_2021_simple.csv')

# 提取最高温度、最低温度和日期
high_temp = list(df['TMAX'])
low_temp = list(df['TMIN'])
dates = pd.to_datetime(df['DATE'])

# 根据最高温、最低温绘图
plt.style.use('seaborn-v0_8-whitegrid')
fig,ax = plt.subplots()
ax.plot(dates,high_temp,color='red',alpha = 0.6)
ax.plot(dates,low_temp,color='blue',alpha = 0.6)
ax.fill_between(dates,high_temp,low_temp,facecolor='blue',alpha = 0.25)

ax.set_title('Daily High and Low Temperatures, 2021',fontsize=24)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel('Temperature(F)',fontsize=16)
fig.autofmt_xdate()
ax.tick_params(labelsize=16)

plt.show()