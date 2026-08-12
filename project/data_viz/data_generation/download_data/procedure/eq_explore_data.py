from pathlib import Path
import json,plotly.express as px,pandas as pd

# 读取数据
path = Path('../eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# 提取地震信息
all_eq_dict = all_eq_data['features']
mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dict]
titles = [eq_dict['properties']['title'] for eq_dict in all_eq_dict]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dict]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dict]

data = pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
)
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title=all_eq_data['metadata']['title'],
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置'
)
fig.write_html('global_earthquakes.html')
fig.show()