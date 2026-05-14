import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
city = input("Enter city name:")

def get_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    temp = data['main']['temp']
    humidity = data['main']['humidity']
    if temp > 35:
        status = "HOT"
    elif 25 <= temp <= 35:
        status = "WARM"
    else:
        status = "COOL"

    print(f"City: {city}")
    print(f"Temp: {temp:.2f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Status: {status}")
get_forecast(city)    