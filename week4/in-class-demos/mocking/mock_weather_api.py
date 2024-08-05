from unittest.mock import Mock

# Notes: If testing a function that retrieves weather data from an API, 
# instead of making a real API call, use a Mock.
# The mock can be set up to return a sample weather report.
# This ensures the test is quick, doesn't rely on network connectivity, and doesn't consume API calls.

def get_weather(city):
    # ... code to fetch weather for the city from an API
    pass

def test_get_weather():
    # Mock the real API call
    get_weather = Mock(return_value={"city": "Sydney", "temperature": 25})
    
    result = get_weather("Sydney")
    assert result == {"city": "Sydney", "temperature": 25}