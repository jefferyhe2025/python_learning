import requests

top_ids= requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()

for item_id in top_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
    item = requests.get(url).json()
    print(f"\nTitle:{item['title']}"
          f"URL:{item.get('url', '')}")
