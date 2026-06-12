import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
cities = ["chennai","mumbai","delhi","erode"]

def check_multiple_cities(cities):
    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json() 

        temp = data['main']['temp']
        humidity = data['main']['humidity']

        if temp >= 30:
            status = "WARM"
        elif temp >= 20:
            status = "NORMAL"
        else:
            status = "COLD"

        print(f"{city:<12} {temp:<10.2f} {str(humidity)+'%':<10} {status}")

check_multiple_cities(cities)        