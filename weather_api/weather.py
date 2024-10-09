import streamlit as st
import requests
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Weather Forecast App", page_icon="☀️", layout="centered")


def load_background():
    img = Image.open("background_weather.jpg")  # Make sure you have a nice background image saved as this
    st.image(img, use_column_width=True)

# Function to get weather data from Weatherstack API
def get_weather(city):
    api_key = '70b87f003dd90ec2721e750baeb69cf4'
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "location" in data and "current" in data:
            location = data['location']['name']
            temperature = data['current']['temperature']
            feels_like = data['current']['feelslike']
            description = data['current']['weather_descriptions'][0]
            return location, temperature, feels_like, description
        else:
            return None, None, None, "City not found. Please check the name and try again."
    else:
        return None, None, None, "There was a problem with the request. Please try again."


# Streamlit UI with a better layout
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🌤️ Weather Forecast App 🌤️</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray;'>Get the latest weather updates for any city worldwide</p>", unsafe_allow_html=True)

# Input section with more space and aligned in the center
with st.container():
    city_name = st.text_input(
        "Enter City Name:",
        "London",
        help="Type the name of a city (e.g., New York, Paris, Tokyo, etc.)",
    )

# Button for fetching the weather
if st.button("Get Weather 🌍"):
    location, temperature, feels_like, description = get_weather(city_name)
    
    if location:
        # Displaying weather information in a stylish way
        st.markdown(f"<h2 style='text-align: center;'>Weather in {location}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 20px;'>🌡️ Temperature: <strong>{temperature}°C</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 18px;'>Feels Like: <strong>{feels_like}°C</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 18px;'>🌥️ Condition: <strong>{description}</strong></p>", unsafe_allow_html=True)
    else:
        st.error(description)

# Footer for a more professional touch
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Weather data powered by WeatherStack</p>", unsafe_allow_html=True)
