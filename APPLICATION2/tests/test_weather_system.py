import unittest
import pandas as pd
from datetime import datetime
from src.data_retrieval import fetch_weather_data
from src.data_processing import calculate_daily_summary

class WeatherSystemTest(unittest.TestCase):

    def test_temperature_conversion(self):
        kelvin_temp = 300
        celsius_temp = kelvin_temp - 273.15
        self.assertEqual(celsius_temp, 26.85)

    def test_fetch_weather_data(self):
        city = 'Delhi'
        data = fetch_weather_data(city)
        self.assertIn('city', data)
        self.assertIn('temp', data)
        self.assertIn('main', data)

    def test_calculate_daily_summary(self):
        df = pd.DataFrame({
            'city': ['Delhi', 'Delhi'],
            'main': ['Clear', 'Rain'],
            'temp': [30, 32],
            'feels_like': [31, 33],
            'dt': [datetime.now().timestamp(), datetime.now().timestamp()]
        })
        summary = calculate_daily_summary(df)
        self.assertEqual(len(summary), 1)
        self.assertIn('avg_temp', summary)
        self.assertIn('dominant_condition', summary)

if __name__ == '__main__':
    unittest.main()
