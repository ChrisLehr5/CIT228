#---------------------------------------Hands On #2---------------------------------------#
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explore the structure of the data.
filename = 'Chapter16/data/weekly_earthquake.json'
#adding encoding as char map failing on larger datasets
#Weekly earthquake file was culled of all negative magnitude earthquakes -otherwise size marker would fail  
with open(filename, encoding="utf-8") as f:
   weekly_earthquake_data = json.load(f)

readable_file = 'Chapter16/data/weekly_earthquake.json'
with open(readable_file, 'w') as f:
   json.dump(weekly_earthquake_data, f, indent=4)

all_eq_dicts = weekly_earthquake_data['features']
print(len(all_eq_dicts))

#Extracting magnitudes, location data 
mags, lons, lats= [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

#Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,     
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,

        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Weekly Worldwide Earthquakes 3/6/21-3/13/21')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')