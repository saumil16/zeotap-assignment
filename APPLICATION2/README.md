# Weather Monitoring System

## Overview
This project is a real-time weather monitoring system that retrieves weather data from the OpenWeatherMap API for major cities in India, processes the data, and generates daily summaries and alerts based on user-defined thresholds.

## Features
- **Real-time weather data retrieval**
- **Temperature conversion from Kelvin to Celsius**
- **Daily weather summaries with average, maximum, and minimum temperatures**
- **Dominant weather condition determination**
- **Alerting system for user-defined thresholds**
- **Visualization of daily summaries**
- **Support for additional weather parameters (humidity, wind speed) in daily summaries (Bonus)**

## Project Structure

- `src/`: Contains the main application code.
  - `__init__.py`: Initializes the src package.
  - `config.py`: Configuration file with constants and settings.
  - `data_retrieval.py`: Handles fetching weather data from the API.
  - `data_processing.py`: Processes the fetched data and calculates daily summaries.
  - `alerting.py`: Checks for alert conditions based on the processed data.
  - `visualization.py`: Generates visualizations for the weather data.
  - `main.py`: Main script to run the system.
- `data/`: Directory for storing retrieved weather data and summaries.
- `logs/`: Directory for storing logs.
- `tests/`: Contains unit tests.
  - `__init__.py`: Initializes the tests package.
  - `test_weather_system.py`: Test cases to validate the system's functionality.
- `.env`: Environment file to store the OpenWeatherMap API key.
- `requirements.txt`: Lists the dependencies.
- `README.md`: This documentation file.
- `plot_weather_summary.py`: Script to generate and display visualizations of the daily weather summary.

## Instructions
### Prerequisites
    - Python 3.8 or higher
    - An OpenWeatherMap API key

### Build and Install
### Create a virtual environment 
     python -m venv venv
### Initialize the virtual environment 
     venv/Scripts/activate
### Install the required packages:
     pip install -r requirements.txt
### Create a `.env` file in the root directory with your OpenWeatherMap API key:
     API_KEY=<your_actual_api_key_here>

Configure the system by updating `src/config.py` with other settings if needed.

### Running the Application
     python src/main.py

This will generate the csv containing all the data in the `data` folder. User can analyze all the data in the csv generated in the `data` folder.

### Visualizing the data
     python plot_weather_summary.py

This will plot the graph to visualize the data
