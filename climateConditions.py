import requests

lat = float(input())
lon = float(input())
API_KEY = '6347d0cc22d6544da03b02a8bc0e3264'

# Make a request to OpenWeatherMap API
url = f'https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={API_KEY}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    precipitation = data['weather'][0]['description']

    # Convert temperature from Kelvin to Celsius
    temperature_celsius = temperature - 273.15

    # Check if conditions are suitable for tigers
    if (temperature_celsius >= 20 and temperature_celsius <= 40) and humidity >= 50 and "rain" in precipitation:
        print("The climate conditions in this area could be suitable for tigers.")
    else:
        print("The climate conditions in this area might not be suitable for tigers.")
else:
    print(f"Error: {response.status_code}")
