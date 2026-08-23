import requests
import plotly.express as px
from operator import itemgetter

r = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
print(f'Status_code:{r.status_code}')

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:25]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url).json()

    # 忽略招聘帖子（这类帖子通常没有 'descendants' 字段，会抛 KeyError）
    try:
        submission_dict = {
            "title": r['title'],
            "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
            "comments": r['descendants']
        }
    except KeyError:
        print(f"ID:{submission_id},没有评论可能是招聘帖，跳过")
        continue          # 跳过，不要再执行下面的 append
    submission_dicts.append(submission_dict)

article_titles, article_links, article_comments = [], [], []
for s in sorted(submission_dicts, key=itemgetter('comments'), reverse=True):
    article_titles.append(s['title'])
    article_links.append(s['hn_link'])
    article_comments.append(s['comments'])

# 横轴只显示缩短的标题，完整标题放进悬停提示，避免长标签把图挤小
short_titles = [t[:18] + '…' if len(t) > 18 else t for t in article_titles]

fig = px.bar(
    x=short_titles,
    y=article_comments,
    hover_name=article_links,       # 悬停时显示文章链接
    custom_data=[article_titles],   # 把完整标题也带进悬停
)
# 自定义悬停内容：完整标题 + 评论数 + 可点击的链接
fig.update_traces(
    hovertemplate="<b>%{customdata[0]}</b><br>评论数：%{y}<br><a href='%{hovertext}' target='_blank'>打开文章 ↗</a><extra></extra>"
)

fig.update_layout(
    title='Hacker News 讨论度最高的文章',
    xaxis_title='文章',
    yaxis_title='评论数',
    title_font_size=25,
    xaxis_title_font_size=15,
    yaxis_title_font_size=16,
    height=800,                    # 固定更大的画布，防止被浏览器窗口挤小
    width=1200,
    margin=dict(l=60, r=40, t=80, b=160),  # 底部留出放斜标签的空间
)
fig.update_xaxes(tickangle=-45, tickfont=dict(size=11))

fig.write_html('Hacker News 讨论度最高的文章.html')
