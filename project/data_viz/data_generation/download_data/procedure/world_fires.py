import pandas as pd

import plotly.express as px

df = pd.read_csv('../fire_data/world_fires_7_day.csv')
data = df[df['confidence'] >= 80]

fig = px.scatter_geo(
    data,
    lon='longitude', lat='latitude',
    color='brightness',
    color_continuous_scale='YlOrRd',
    opacity=0.55,
    hover_data={'frp': ':.1f', 'confidence': True},
    projection='natural earth',
    title='World Fires (confidence ≥ 80)',
)
fig.update_traces(marker=dict(size=3))
fig.update_layout(width=1200, height=600, margin=dict(l=0, r=0, t=50, b=0))
fig.write_html('world_fires_2022.html', include_plotlyjs='cdn')