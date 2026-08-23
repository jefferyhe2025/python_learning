import requests
from operator import itemgetter

r = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
print(f'Status_code:{r.status_code}')

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url).json()

    # 忽略招聘帖子
    try:
        submission_dict = {
            "title": r['title'],
            "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
            "comments": r['descendants']
        }
    except KeyError:
        print(f"ID:{submission_id},没有评论可能是广告。")

    submission_dicts.append(submission_dict)

# 排序
for s in sorted(submission_dicts,key=itemgetter('comments'),reverse=True):
    print(f"\ntitle:{s['title']}")
    print(f"hn_link:{s['hn_link']},")
    print(f"comments:{s['comments']}")