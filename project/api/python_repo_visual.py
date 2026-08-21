import requests

import plotly.express as px

url = "https://api.github.com/search/repositories"
params = {"q": "language:python stars:>10000", "sort": "stars", "order": "desc"}

headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2026-03-10",
}

r = requests.get(url,headers=headers,params=params)
print(f"Status:{r.status_code}")
r.raise_for_status()
response_dict = r.json()

#处理仓库信息
repo_dicts = response_dict['items']
stars = [ repo_dict['stargazers_count'] for repo_dict in repo_dicts]

#创建悬浮文本
hover_texts = [
    f"{repo_dict['owner']['login']}<br />{repo_dict['description'] or ''}"
    for repo_dict in repo_dicts
]

#创建可交互链接
repo_links = [
    f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}/</a>"
    for repo_dict in repo_dicts
]

#绘制柱形图
title = "Most-Starred Python Projects on Github"
labels = {'x':'Repositories','y':'Stars'}
fig = px.bar(
    x=repo_links,
    y=stars,
    title=title,
    labels=labels,
    hover_name=hover_texts,
             )

fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=16,
    yaxis_title_font_size=20
)
fig.update_traces(marker_color='SteelBlue',marker_opacity=0.6)

fig.show(renderer="browser")