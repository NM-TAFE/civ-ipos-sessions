from unittest.mock import Mock

def get_weather(city):
    # ... code to fetch weather for the city from an API
    pass

def test_get_weather():
    # Mock the real API call
    get_weather = Mock(return_value={"city": "Sydney", "temperature": 25})
    
    result = get_weather("Sydney")
    assert result == {"city": "Sydney", "temperature": 25}