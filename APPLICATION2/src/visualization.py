import pandas as pd
import matplotlib.pyplot as plt

def plot_daily_summary():
    df = pd.read_csv('data/daily_summary.csv')
    df['date'] = pd.to_datetime(df['date'])
    
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['avg_temp'], label='Average Temperature')
    plt.plot(df['date'], df['max_temp'], label='Maximum Temperature')
    plt.plot(df['date'], df['min_temp'], label='Minimum Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Temperature Summary')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['avg_humidity'], label='Average Humidity')
    plt.plot(df['date'], df['max_humidity'], label='Maximum Humidity')
    plt.plot(df['date'], df['min_humidity'], label='Minimum Humidity')
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')
    plt.title('Daily Humidity Summary')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['avg_wind_speed'], label='Average Wind Speed')
    plt.plot(df['date'], df['max_wind_speed'], label='Maximum Wind Speed')
    plt.plot(df['date'], df['min_wind_speed'], label='Minimum Wind Speed')
    plt.xlabel('Date')
    plt.ylabel('Wind Speed (m/s)')
    plt.title('Daily Wind Speed Summary')
    plt.legend()
    plt.show()
