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

# extract data out of the repositories for visual 
links, stargazers, hover_texts = [], [], []
for repo in high_rated:
    # get name and url and cover url with thath name
    name = repo["name"]
    url = repo["html_url"]
    link = f"<a href='{url}'>{name}"
    links.append(link) 

    # get description and owner and make an hover-text
    owner = repo["owner"]["login"]
    description = repo["description"]
    hover_text = f"{owner} - {description}"
    hover_texts.append(hover_text)

    # get stargazers
    stargazers.append(repo["stargazers_count"])


# make a visual 
title = "Popular python-repositories on GitHub"
labels = {"x": "Repo-links", "y": "Stargazer count"}
fig = px.bar(x=links, y=stargazers, title=title, labels=labels, 
            hover_name=hover_texts) 


fig.show()