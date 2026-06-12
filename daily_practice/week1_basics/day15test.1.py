import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
city1 = input("Enter city :")
city2 = input("Enter city :")

def compare_weather(city1,city2):
    url1 = f"https://api.openweathermap.org/data/2.5/weather?q={city1}&appid={api_key}&units=metric"
    data1 = requests.get(url1).json()
    temp1 = data1['main']['temp']

    url2 = f"https://api.openweathermap.org/data/2.5/weather?q={city2}&appid={api_key}&units=metric"
    data2 = requests.get(url2).json()
    temp2 = data2['main']['temp']


    if temp1 > temp2:
        print(f"{city1} is hotter! {temp1}°C vs {temp2}°C")
    else:
        print(f"{city2} is hotter! {temp2}°C vs {temp1}°C")

compare_weather(city1, city2)
