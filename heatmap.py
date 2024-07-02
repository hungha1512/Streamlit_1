import streamlit as st
import folium
import json
import urllib
import requests
from folium.plugins import HeatMap
from streamlit_folium import st_folium

where = urllib.parse.quote_plus("""
{
    "name": {
        "$exists": true
    },
    "population": {
        "$exists": true
    },
    "location": {
        "$exists": true
    }
}
""")
url = ('https://parseapi.back4app.com/classes/Vietnam_City?count=1&order=name&keys=name,population,location,'
       'cityId&where=%s') % where
headers = {
    'X-Parse-Application-Id': '9u59dtvsJZE3U7vG2DD477jRMM3KHV2k8RbJzuJM',  # This is your app's application id
    'X-Parse-REST-API-Key': 'UlRFD86olzUZeoCuaTKOdhV1yqhETt5u5CFn45jg'  # This is your app's REST API key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8'))  # Here you have the data that you need

# Extract the relevant information
locations = []
populations = []
for city in data['results']:
    location = city['location']
    population = city['population']
    locations.append([location['latitude'], location['longitude'], population])
    populations.append(population)

# Create a folium map centered around Vietnam
m = folium.Map(location=[14.0583, 108.2772], zoom_start=6)

# Add heatmap to the map
HeatMap(locations).add_to(m)

# Display the heatmap in Streamlit
st.title("Vietnam City Population Heatmap")
st_folium(m, width=700, height=500)


