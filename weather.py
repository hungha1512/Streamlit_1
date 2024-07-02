import streamlit as st
import plotly.express as px
import requests

API_KEY = st.secrets["weather"]["key"]


def get_data(city, day):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8 * day]
    return filtered_data


st.set_page_config(page_title="Weather Forecast", layout="wide")
st.title("Weather Forecast")
with st.sidebar:
    place = st.text_input("Enter City")
    days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")
    option = st.selectbox("Select data to view", ("Temperature", "Humidity", "Wind"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature / humidity data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create temperature plot
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Humidity":
            humidity = [dict["main"]["humidity"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create humidity plot
            figure = px.line(x=dates, y=humidity, labels={"x": "Date", "y": "Humidity (%)"})
            st.plotly_chart(figure)

        if option == "Wind":
            rain = [dict["wind"]["speed"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create rain plot
            figure = px.line(x=dates, y=rain, labels={"x": "Date", "y": "Wind speed (km/h)"})
            st.plotly_chart(figure)

    except KeyError:
        st.error("That place does not exist.")
