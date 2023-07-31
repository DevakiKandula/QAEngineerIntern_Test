import requests

def fetch_weather_data(api_url):
    # Make an HTTP GET request to the API URL and fetch the weather data
    response = requests.get(api_url)
    # Convert the JSON response to a Python dictionary and extract the "list" key
    return response.json()["list"]

def get_weather_for_date(weather_data, target_date):
    for item in weather_data:
        date_str = item["dt_txt"].split()[0]  # Extract date from "dt_txt" key
        if date_str == target_date:
            return item["main"]["temp"]
    return None

def get_wind_speed_for_date(weather_data, target_date):
    for item in weather_data:
        date_str = item["dt_txt"].split()[0]  # Extract date from "dt_txt" key
        if date_str == target_date:
            return item["wind"]["speed"]
    return None

def get_pressure_for_date(weather_data, target_date):
    for item in weather_data:
        date_str = item["dt_txt"].split()[0]  # Extract date from "dt_txt" key
        if date_str == target_date:
            return item["main"]["pressure"]
    return None

def main():
    # Set the API URL for the OpenWeatherMap hourly forecast for London
    api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    weather_data = fetch_weather_data(api_url)

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            target_date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather_for_date(weather_data, target_date)
            if temperature is not None:
                print(f"Temperature on {target_date}: {temperature} °C")
            else:
                print("Data not available for the selected date.")
        elif choice == 2:
            target_date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_for_date(weather_data, target_date)
            if wind_speed is not None:
                print(f"Wind Speed on {target_date}: {wind_speed} m/s")
            else:
                print("Data not available for the selected date.")
        elif choice == 3:
            target_date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_for_date(weather_data, target_date)
            if pressure is not None:
                print(f"Pressure on {target_date}: {pressure} hPa")
            else:
                print("Data not available for the selected date.")
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
