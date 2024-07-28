import requests
import pandas as pd
from datetime import datetime
from threading import Timer
from config import API_KEY, CITIES, INTERVAL

def fetch_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    weather_info = {
        'city': city,
        'main': data['weather'][0]['main'],
        'temp': data['main']['temp'] - 273.15,  # Kelvin to Celsius
        'feels_like': data['main']['feels_like'] - 273.15,
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'dt': data['dt']
    }
    return weather_info

def fetch_and_store_data():
    all_weather_data = []
    for city in CITIES:
        data = fetch_weather_data(city)
        all_weather_data.append(data)
    df = pd.DataFrame(all_weather_data)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    df.to_csv(f'data/weather_data_{timestamp}.csv', index=False)
    print(f"Data fetched and stored at {timestamp}")
    return df

def schedule_data_retrieval():
    fetch_and_store_data()
    Timer(INTERVAL, schedule_data_retrieval).start()
