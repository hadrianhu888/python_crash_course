import requests
import json

# Make API call, and store the response
url = 'http://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore information about the article
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'r') as f:
    json.dump(response_dict, f, indent=4)
