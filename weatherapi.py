import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "75cdc003e132864b83559fc2cff8d480"
CITY = "Chicago"


def kelvin_to_fahrenheit_celsius(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit
   

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()


temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_fahrenheit_celsius(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_fahrenheit, feels_like_celsius = kelvin_to_fahrenheit_celsius(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])



print(f"Temperature in {CITY}: {temp_fahrenheit:.2f}˚F or {temp_celsius:.2f}˚C")
print(f"Temperature in {CITY} feels like: {feels_like_fahrenheit:.2f}˚F or {feels_like_celsius:.2f}˚C")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"General Weather in {CITY}: {description}%")
print(f"Sun rises in {CITY} at {sunrise_time} local time.")
print(f"Sun sets in {CITY} at {sunset_time} local time.")