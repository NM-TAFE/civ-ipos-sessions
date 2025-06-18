import logging
import requests
import traceback
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='./logs/api_app.log')

# Load API key from environment variables
# API_KEY = os.getenv("OPENWEATHER_API_KEY")
API_KEY = '7761a681'  # Replace with your actual API key

def get_weather(lat, lon):
    """Fetches weather data for the specified latitude and longitude."""
    try:
        # url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API_KEY}"
        logging.debug(f"Requesting weather data for coordinates: lat={lat}, lon={lon}")
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        logging.info("Weather data received: %s", data)
        return data
    except requests.exceptions.HTTPError as http_err:
        logging.error("HTTP error occurred: %s", http_err)
        logging.error(traceback.format_exc())
    except Exception as err:
        logging.error("An error occurred: %s", err)
        logging.error(traceback.format_exc())

def main():
    # Latitude and Longitude for Perth, Australia
    latitude = -31.9505
    longitude = 115.8605
    weather_data = get_weather(latitude, longitude)
    if weather_data:
        print(f"Current temperature in Perth, Australia: {weather_data['main']['temp']}°C")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
