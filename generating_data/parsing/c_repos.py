import requests
from plotly.graph_objs import Bar
from plotly import offline
language = 'C'
# Import the url from https://api.github.com/search/repositories?q=languages:python&sort=stars
url = 'https://api.github.com/search/repositories?q=language:'+language+'&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories Returned: {len(repo_dicts)}")

# Summarize all of the information about the repositories
print("Selected information about each repository:\n\n")
# Process results
repo_names, stars, labels, repo_links = [], [], [], []
for repo_dict in repo_dicts:
    # Examine each repository
    print("\nSelected information about first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Description: {repo_dict['description']}")
    print(f"URL: {repo_dict['url']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Repository: {repo_dict['owner']['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Pushed: {repo_dict['pushed_at']}")
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]

# Layout the plot and visualizations

my_layout = {
    'title': 'Most-Starred ' + language + ' Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {'title': 'Repository', 'titlefont': {'size': 24}, 'tickfont': {'size': 14}},
    'yaxis': {'title': 'Stars', 'titlefont': {'size': 24}, 'tickfont': {'size': 14}},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
offline.save(fig, filename='python_repos.html')

print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

# Process results.
print(response_dict.keys())
