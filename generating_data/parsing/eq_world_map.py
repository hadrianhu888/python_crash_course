import json
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout

# Refactor getting the data from the json file.


def get_json_all_data(filename):
    """Get all the data from the JSON file."""
    with open(filename) as f:
        all_eq_data = json.load(f)
    return all_eq_data

# Refactor the ability to get magnitude, longitude, latitude, and hover text from the JSON file.


def get_json_data(filename, all_eq_data, all_eq_dicts, mags, lons, lats, hover_texts):
    """Get the magnitude, longitude, latitude, and hover text from the JSON file."""
    with open(filename) as f:
        all_eq_data = json.load(f)
    all_eq_dicts = all_eq_data['features']
    mags, lons, lats, hover_texts = [], [], [], []
    for eq_dict in all_eq_dicts:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        title = eq_dict['properties']['title']
        hover_texts.append(title)
        lons.append(lon)
        lats.append(lat)
        mags.append(mag)
    return mags, lons, lats, hover_texts

# Refactor the ability to create the map.


def create_map_from_json_data(mags, lons, lats, hover_texts):
    """Create a map from the JSON data."""
    data = [{'type': 'scattergeo',
             'lon': lons,
             'lat': lats,
             'text': hover_texts,
             'marker': {'size': [5*mag for mag in mags],
                        'color': mags,
                        'colorscale': 'Viridis',
                        'reversescale': True,
                        'colorbar': {'title': 'Magnitude'}}}]
    my_layout = Layout(title='Global Earthquakes')
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='global_earthquake_30_days.html')


# get json title from json

def get_json_title(filename):
    """Get the title from the JSON file."""
    with open(filename) as f:
        all_eq_data = json.load(f)
    all_eq_dicts = all_eq_data['features']
    title = all_eq_data['metadata']['title']
    return title

# Explore the structure of the data.


filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    hover_texts.append(title)
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)

print(mags[:10])
print(lons[:5])
print(lats[:5])
print(hover_texts[:5])

print(len(all_eq_dicts))

# Map the Earthquakes.

data = [{'type': 'scattergeo',
         'lon': lons,
         'text': hover_texts,
         'lat': lats,
         'marker': {'size': [5*mag for mag in mags],
                    'color': mags,
                    'colorscale': 'Viridis',
                    'reversescale': True,
                    'colorbar': {'title': 'Magnitude'}}}]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquake_30_days.html')

# Refactor the code to create a function to create the map.
