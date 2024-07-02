import streamlit as st
import folium
from streamlit_folium import st_folium
import json

# Load GeoJSON data
with open('vietnam.json', encoding='utf-8') as f:
    geojson_data = json.load(f)

# Create a folium map centered around Vietnam
m = folium.Map(location=[14.0583, 108.2772], zoom_start=5)

# Add GeoJSON overlay
folium.GeoJson(geojson_data).add_to(m)

# Display the map in Streamlit
st.title("Vietnam Map")
st_folium(m, width=700, height=500)

# Add title

