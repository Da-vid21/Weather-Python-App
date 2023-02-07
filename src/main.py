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


loc = geocoder.ip('me').latlng


lat = loc[0]
lon = loc[1]

weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"

weather_data = requests.get(weather_url).json()
data = weather_data.values()
keys = weather_data.keys()
current_temp = weather_data['main']['temp']
tempF = round(convertKtoF(current_temp),1)
print(f'{tempF}°F')
