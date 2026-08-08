import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('../weather_data/sitka_weather_2021_full.csv')
rain_falls = list(df['PRCP'])
dates = pd.to_datetime(df['DATE'])

plt.style.use('seaborn-v0_8-whitegrid')
fig,ax = plt.subplots()
ax.plot(dates,rain_falls,color='blue')

ax.set_title('Daily Rain Falls,2021',fontsize=24)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel('Rainfall (in)',fontsize=16)
fig.autofmt_xdate()
ax.tick_params(labelsize=16)

plt.show()