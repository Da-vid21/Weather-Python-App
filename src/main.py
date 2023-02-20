'''
pip install geocoder
pip install requests
Change your api using api.txt or initialize it here
'''
import requests, json
import geocoder


def convertKtoF(old_temp):
    degC = old_temp-273.15
    degF = (degC * 9/5)+32
    return degF

with open("../api.txt") as f:
    api = f.readline()

# set our current location
geo = geocoder.ip('me')

lat = geo.latlng[0]
lon = geo.latlng[1]

#grab weather data from openweathermap.org
weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"
weather_data = requests.get(weather_url).json()
data = weather_data.values()
keys = weather_data.keys()

# location
print(f'Location: {geo.address}')

# temperature
temp = round(convertKtoF(weather_data['main']['temp']))
high = round(convertKtoF(weather_data['main']['temp_max']))
low = round(convertKtoF(weather_data['main']['temp_min']))
print(f'Temperature: {temp}°F (H: {high}°F, L: {low}°F)')

# weather
sky = weather_data['weather'][0]['main']
sky_desc = weather_data['weather'][0]['description']
print(f'Weather: {sky} ({sky_desc})')


