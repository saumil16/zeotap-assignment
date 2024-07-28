from data_retrieval import schedule_data_retrieval
from data_processing import process_weather_data

if __name__ == '__main__':
    # Start data retrieval process
    schedule_data_retrieval()

    # Schedule daily processing
    from threading import Timer
    def schedule_daily_processing():
        process_weather_data()
        Timer(86400, schedule_daily_processing).start()  # 24 hours 

    schedule_daily_processing()
