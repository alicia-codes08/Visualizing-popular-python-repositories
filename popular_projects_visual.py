import requests
import plotly.express as px 

# Send request and get answer
url = "https://api.github.com/search/repositories?q=language:python"
headers = {"Accept": "application/vnd.github+json"}
request_answer = requests.get(url, headers=headers)
print(f"Status code: {request_answer.status_code}") 

# convert answer into python-object
converted_answer = request_answer.json()
repositories = converted_answer["items"]

# get highest rated python-repos (above 150'000 stargazers)
high_rated = []
for repo in repositories:
    stargazers_count = repo["stargazers_count"]
    if stargazers_count > 150_000:
        high_rated.append(repo)

print(high_rated) 