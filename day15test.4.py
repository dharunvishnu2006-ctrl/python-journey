import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
def weather_alert(city,threshold):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    temp = data['main']['temp']
    if temp > threshold:
       print(f"ALERT! {city} is too hot! {temp}°C")
    else:
       print(f"{city} is safe! {temp}°C")
weather_alert("Chennai", 30)   
weather_alert("Mumbai", 35) 
weather_alert("Erode", 25)     