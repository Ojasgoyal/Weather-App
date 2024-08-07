import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY environment variable not set.")


def get_weather(city,country):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city},{country}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError(f"Error: Received status code {response.status_code}")
    return response.json()


def main():

    print("*" * 20)
    print("Weather APP")
    print("*" * 20)
    print("To exit the app type exit and press enter\n\n")

    while True:
        try:
            city = input("Enter city name: ").lower()
            if city == "exit":
                print('\nClosing the app')
                break

            country = input("Enter country name: ").lower()
            if country == "exit":
                print('\nClosing the app')
                break

            data = get_weather(city,country)
            
            if "error" in data:
                raise ValueError
            else:
                temp = data['current']['temp_c']
                weather = data['current']['condition']['text']
                print(f"Temperature: {temp}°C")
                print(f"Weather: {weather}\n")

        except:
            print("Could not fetch weather data")
        


if __name__ == "__main__":
    main()