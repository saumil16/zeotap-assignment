import os
import pandas as pd
from datetime import datetime
from config import TEMP_THRESHOLD

def calculate_daily_summary(df):
    df['date'] = pd.to_datetime(df['dt'], unit='s').dt.date
    summary = df.groupby('date').agg(
        avg_temp=('temp', 'mean'),
        max_temp=('temp', 'max'),
        min_temp=('temp', 'min'),
        avg_humidity=('humidity', 'mean'),
        max_humidity=('humidity', 'max'),
        min_humidity=('humidity', 'min'),
        avg_wind_speed=('wind_speed', 'mean'),
        max_wind_speed=('wind_speed', 'max'),
        min_wind_speed=('wind_speed', 'min'),
        dominant_condition=('main', lambda x: x.mode()[0])
    ).reset_index()
    summary.to_csv('data/daily_summary.csv', index=False)
    return summary

def check_alerts(df):
    for index, row in df.iterrows():
        if row['temp'] > TEMP_THRESHOLD:
            print(f"Alert! Temperature in {row['city']} exceeded {TEMP_THRESHOLD}C")

def process_weather_data():
    files = [f for f in os.listdir('data') if f.startswith('weather_data')]
    all_data = pd.concat([pd.read_csv(f'data/{file}') for file in files])
    daily_summary = calculate_daily_summary(all_data)
    check_alerts(all_data)
    return daily_summary
