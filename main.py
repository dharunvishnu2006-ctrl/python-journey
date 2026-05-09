import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
city = input("Enter city name:")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()
if data["cod"] == 200:

    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
 
else:
    print(f"Invalid city.")  