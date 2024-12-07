# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def get_weather(city):
#     api_key = os.getenv("WEATHER_API_KEY")
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return {
#             "temperature": data["main"]["temp"],
#             "description": data["weather"][0]["description"],
#             "humidity": data["main"]["humidity"]
#         }
#     else:
#         return {"error": "Unable to fetch weather data"}
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
    else:
        return {"error": "Unable to fetch weather data"}
