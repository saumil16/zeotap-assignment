# Weather Monitoring System

This project is a real-time weather monitoring system that retrieves weather data from the OpenWeatherMap API for major cities in India, processes the data, and generates daily summaries and alerts based on user-defined thresholds.

## Features
- Real-time weather data retrieval
- Temperature conversion from Kelvin to Celsius
- Daily weather summaries with average, maximum, and minimum temperatures
- Dominant weather condition determination
- Alerting system for user-defined thresholds
- Visualization of daily summaries

## Bonus Features
- Support for additional weather parameters (humidity, wind speed) in daily summaries

## Setup
1.  Create a virtual environment 
        python -m venv venv
    Initialize the virtual environment 
        venv/Scripts/activate

2. Install the required packages:
    pip install -r requirements.txt

3. Create a `.env` file in the root directory with your OpenWeatherMap API key:
    API_KEY=<your_actual_api_key_here>

4. Configure the system by updating `src/config.py` with other settings if needed.

### Running the Main Script
    python src/main.py

This will generate the csv containing all the data in the `data` folder.

### Visualizing the data
    python plot_weather_summary.py

This will plot the graph to visualize the data
