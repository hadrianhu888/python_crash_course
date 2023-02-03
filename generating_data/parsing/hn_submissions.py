from operator import itemgetter
import requests
import plotly
from plotly.graph_objs import Bar
from plotly import offline

# Make API request and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True)

comments, labels, hovertext = [], [], []
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
    comments.append(submission_dict['comments'])
    owner = submission_dict['title']
    label = submission_dict['hn_link']
    labels.append(label)

# Make visualization

data = [{
    'type': 'bar',
    'x': [submission_dict['title'] for submission_dict in submission_dicts],
    'y': comments,
    'hovertext': [submission_dict['hn_link'] for submission_dict in submission_dicts],
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Commented on Hacker News',
    'xaxis': {'title': 'Title'},
    'yaxis': {'title': 'Number of Comments'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions.html')
offline.save(fig, filename='hn_submissions.html')
