import requests

def get_current_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed']
        }
    else:
        return None

# Example usage
api_key = '9e8dc194d286ea7893a08d41b61e336e'  # Replace with your actual API key
city = 'pune'
weather = get_current_weather(city, api_key)

if weather:
    print(f"Current weather in {city}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Description: {weather['description']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Pressure: {weather['pressure']} hPa")
    print(f"Wind Speed: {weather['wind_speed']} m/s")
else:
    print("Failed to get weather data")
