import json
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout


# Explore the structure of the data.

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
mags, lons, lats = [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)

print(mags[:10])
print(lons[:5])
print(lats[:5])

print(len(all_eq_dicts))

# Map the Earthquakes.

data = [{'type': 'scattergeo',
         'lon': lons,
         'lat': lats,
         'marker': {'size': [5*mag for mag in mags]}}]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
offline.savefig(filename='global_earthquakes.png')

""" readable_file = 'data/readable_eq_data.json'
with open(readable_file) as f:
    json.dump(all_eq_data, f, indent=4) """
