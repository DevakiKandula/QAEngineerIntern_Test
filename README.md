# QAEngineerIntern_Test
Hourly Weather Forecast Program-

This is a simple Python program that interacts with the OpenWeatherMap API to provide hourly weather forecast information for the city of London. 
The program allows the user to query weather-related data based on their choice:

1)Get weather: Retrieve the temperature (in Celsius) for a specific date.
2)Get Wind Speed: Retrieve the wind speed (in meters per second) for a specific date.
3)Get Pressure: Retrieve the atmospheric pressure (in hectopascals) for a specific date.
4)Exit: Terminate the program.

Requirements:-
1)Python 3.x
2)requests library

How to Use:-
1)Clone the repository to your local machine or download the code as a ZIP file.
2)Install the required requests library by running the following command in your terminal or command prompt:
CODE- pip install requests.

How it wroks:-
1)The program will display the menu options. Choose the desired option by entering the corresponding number (1, 2, 3, or 0 for exit).
2)If you choose option 1, you will be prompted to enter a date in the format YYYY-MM-DD. The program will then fetch and display the temperature for that specific date.
3)If you choose option 2, you will be prompted to enter a date in the format YYYY-MM-DD. The program will then fetch and display the wind speed for that specific date.
4)If you choose option 3, you will be prompted to enter a date in the format YYYY-MM-DD. The program will then fetch and display the atmospheric pressure for that specific date.
5)To exit the program, choose option 0.

API URL:-
The program uses the OpenWeatherMap API to fetch hourly weather forecast data for London. The API URL is set as follows:
URL- https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22

Contributions:-
Feel free to contribute to this project by opening issues or pull requests. Your feedback and suggestions are appreciated!





