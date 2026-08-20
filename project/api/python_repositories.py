import requests

url = "https://api.github.com/search/repositories"
url +="?q=language:python+sort:stars+stars:>10000"

headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2026-03-10",
}

r = requests.get(url,headers=headers)
print(f"Status:{r.status_code}")

response_dict = r.json()
print(response_dict.keys())

#打印有关字典的信息
print(f"Total repositories:{response_dict['total_count']}")
print(f"Complete_results:{not response_dict['incomplete_results']}")

#打印有关仓库信息
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")


print("\nSelected information about each repositories:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")